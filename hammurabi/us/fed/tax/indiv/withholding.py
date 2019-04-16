from akkadian import *


# https://www.irs.gov/pub/irs-pdf/fw4.pdf
# IRS Form W4 (2019) rules

# The following abbreviations are used in the rules below:
#
#   p = person
#   s = person's spouse
#   pa_wksht = Personal Allowances Worksheet
#   daai_wksht = Deductions, Adjustments, and Additional Income Worksheet
#   temj_wksht = Two-Earners/Multiple Jobs Worksheet
#   ctc = Child Tax Credit
#   mfj = Married filing jointly
#   mfs = Married filing separately
#   hoh = Head of household
#   dep = dependent


############### source rules ###############
def form_w4_complete(p, s):
    return And(pa_wksht_complete(p, s),
               Or(Not(itemizing(p)),
                  daai_wksht_complete(p)),
               Or(Not(temj_wksht_required(p, s)),
                  temj_wksht_complete(p, s)))


#######PERSONAL ALLOWANCES WORKSHEET#######


# can we make person/spouse global?
def pa_wksht_complete(p, s):
    # check complete if line h is known?
    return pa_wksht_line_h(p, s) >= 0


# • You’re single, or married filing separately, and have only one job; or
# •  You’re married filing jointly, have only one job, and your spouse doesn’t work; or
# • Your wages from a second job or your spouse’s wages (or the total of both) are $1,500 or less
def only_job_or_low_wage_second(p, s):
    # dev question, could we infer "only one job" as one active wages/employment record? Probably a question for policy team.
    return Or(
            And(
                Or(is_single(p),
                   mfs(p, s)),
                has_only_one_job(p)),
            And(mfj(p),
                has_only_one_job(p),
                spouse_unemployed(s)),
            combined_couple_wages(p, s) <= 1500)


# Child tax credit. See Pub. 972, Child Tax Credit, for more information.
# • If your total income will be less than $71,201 ($103,351 if married filing jointly), enter 4 for each eligible child.
# • If your total income will be from $71,201 to $179,050 ($103,351 to $345,850 if married filing jointly), enter 2 for each
# eligible child.
# • If your total income will be from $179,051 to $200,000 ($345,851 to $400,000 if married filing jointly), enter 1 for
# each eligible child.
# • If your total income will be higher than $200,000 ($400,000 if married filing jointly), enter -0- . . . . . . .
def ctc_count(p, s):
    If(And(s is not None, mfj(p)), ctc_w_spouse(p, s),
       ctc_w_o_spouse(p))


def ctc_w_spouse(p, s):
    return If(marital_income(p, s) < 103351, 4 * num_children(p),
              marital_income(p, s) <= 345850, 2 * num_children(p),
              marital_income(p, s) <= 400000, num_children(p),
              0)


def ctc_w_o_spouse(p):
    return If(total_income(p) < 71201, 4 * num_children(p),
              total_income(p) <= 179051, 2 * num_children(p),
              total_income(p) <= 200000, num_children(p),
              0)


# Credit for other dependents. See Pub. 972, Child Tax Credit, for more information.
# • If your total income will be less than $71,201 ($103,351 if married filing jointly), enter “1” for each eligible dependent.
# • If your total income will be from $71,201 to $179,050 ($103,351 to $345,850 if married filing jointly), enter “1” for every
# two dependents (for example, “-0-” for one dependent, “1” if you have two or three dependents, and “2” if you have
# four dependents).
# • If your total income will be higher than $179,050 ($345,850 if married filing jointly), enter “-0-” . . . . . .
def credit_for_other_deps(p, s):
    If(s is not None,
       And(credit_for_other_deps_w_spouse(p, s), mfj(p)),
       credit_for_other_deps_w_o_spouse(p))


def credit_for_other_deps_w_spouse(p, s):
    return If(marital_income(p, s) < 103351, num_dependents(p),
              marital_income(p, s) <= 345850, Floor(num_dependents(p) / 2),
              marital_income(p, s) > 345850, 0)


def credit_for_other_deps_w_o_spouse(p):
    return If(total_income(p) < 71201, num_dependents(p),
              total_income(p) <= 179051, Floor(num_dependents(p) / 2),
              total_income(p) > 179050, 0)


# Total on line h
def pa_wksht_line_h(p, s):
    return Boole(is_claiming_self(p)) \
           + Boole(mfj(p)) \
           + Boole(hoh(p)) \
           + Boole(only_job_or_low_wage_second(p, s)) \
           + ctc_count(p, s) \
           + credit_for_other_deps(p, s) \
           + other_credits_pub505(p)


#######Deductions, Adjustments, and Additional Income Worksheet#######


# Note: Use this worksheet only if you plan to itemize deductions, claim certain adjustments to income, or have a large amount of nonwage
# income not subject to withholding.
def daai_wksht_complete(p):
    return ded_adj_adtl_inc_line_10(p, "TODO") >= 0


# Enter an estimate of your 2019 itemized deductions. These include qualifying home mortgage interest,
# charitable contributions, state and local taxes (up to $10,000), and medical expenses in excess of 10% of
# your income. See Pub. 505 for details . . . . . . . . . . . . . . . . . . . . . .
def ded_adj_adtl_inc_line_1(p):
    return itemized_deductions_2019(p)


# 2 Enter: { $24,400 if you’re married filing jointly or qualifying widow(er)
# $18,350 if you’re head of household
# $12,200 if you’re single or married filing separately } . .
def ded_adj_adtl_inc_line_2(p):
    return If(Or(filing_jointly(p), qualifying_widower(p)), 24400,
              hoh(p), 18350,
              Or(is_single(p), filing_separately(p)), 12200)


# Subtract line 2 from line 1. If zero or less, enter “-0-”
def ded_adj_adtl_inc_line_3(p, s):
    return If(ded_adj_adtl_inc_line_1(p) - ded_adj_adtl_inc_line_2(p) >= 0,
              ded_adj_adtl_inc_line_1(p) - ded_adj_adtl_inc_line_2(p),
              False)


# Enter an estimate of your 2019 adjustments to income, qualified business income deduction, and any
# additional standard deduction for age or blindness (see Pub. 505 for information about these items) . .
def ded_adj_adtl_inc_line_4(p):
    return estimate_2019_adj_to_inc_qual_bus_inc_ded_addtl_std_ded(p)


# Add lines 3 and 4 and enter the total
def ded_adj_adtl_inc_line_5(p, s):
    return ded_adj_adtl_inc_line_3(p, s) + ded_adj_adtl_inc_line_4(p)


# Enter an estimate of your 2019 nonwage income not subject to withholding (such as dividends or interest) .
def ded_adj_adtl_inc_line_6(p):
    return estimate_2019_nonwage_inc_not_subj_to_withholding(p)


# Subtract line 6 from line 5. If zero, enter “-0-”. If less than zero, enter the amount in parentheses
def ded_adj_adtl_inc_line_7(p, s):
    return ded_adj_adtl_inc_line_5(p, s) - ded_adj_adtl_inc_line_6(p)


# Divide the amount on line 7 by $4,200 and enter the result here. If a negative amount, enter in parentheses.
# Drop any fraction
def ded_adj_adtl_inc_line_8(p, s):
    return Floor(ded_adj_adtl_inc_line_7(p, s) / 4200)


# Enter the number from the Personal Allowances Worksheet, line H, above
def ded_adj_adtl_inc_line_9(p, s):
    return pa_wksht_line_h(p, s)


# Add lines 8 and 9 and enter the total here. If zero or less, enter “- 0 -”. If you plan to use the Two-Earners/
# Multiple Jobs Worksheet, also enter this total on line 1 of that worksheet on page 4. Otherwise, stop here
# and enter this total on Form W-4, line 5, page 1
def ded_adj_adtl_inc_line_10(p, s):
    return Max([ded_adj_adtl_inc_line_8(p, s) + ded_adj_adtl_inc_line_9(p, s), 0])


###############Two Earners/Multiple Jobs Wksht###############


# Note: Use this worksheet only if the instructions under line H from the Personal Allowances Worksheet direct you here.

# If you have more than one job at a time
# or are married filing jointly and you and your spouse both work,
# and the combined earnings from all jobs exceed $53,000 ($24,450 if married filing jointly), see the
# Two-Earners/Multiple Jobs Worksheet on page 4 to avoid having too little tax withheld.
def temj_wksht_required(p, s):
    return Or(temj_wksht_required_single(p),
              temj_wksht_required_couple(p, s))


# complete if line 9 is known
def temj_wksht_complete(p, s):
    return temj_wksht_line_9(p, s)


def temj_wksht_required_single(p):
    return And(count_of_jobs(p) > 1,
               total_income(p) > 53000)


def temj_wksht_required_couple(p, s):
    return And(is_married(p),
               filing_jointly(p),
               couple_both_work(p, s),
               combined_couple_wages(p, s) > 24450)


# Enter the number from the Personal Allowances Worksheet, line H, page 3 (or, if you used the
# Deductions, Adjustments, and Additional Income Worksheet on page 3, the number from line 10 of that
# worksheet)
# tbd, logic to figure out which wksht has been completed
def temj_wksht_line_1(p, s):
    return If(itemizing(p), ded_adj_adtl_inc_line_10(p, s),
              pa_wksht_line_h(p, s))


# Find the number in Table 1 below that applies to the LOWEST paying job and enter it here. However, if you’re
# married filing jointly and wages from the highest paying job are $75,000 or less and the combined wages for
# you and your spouse are $107,000 or less, don’t enter more than “3”
def temj_wksht_line_2(p, s):
    return If(And(is_married(p),
                  filing_jointly(p),
                  highest_earning_job_from_couple(p, s) <= 75000,
                  combined_couple_wages(p, s)),
              # assumes only one job, needs to be expanded
              Min([3, temj_wksht_table_1_mfj_lookup(Min([persons_wages(p), persons_wages(s)]))]),
              (mfj(p),
               temj_wksht_table_1_mfj_lookup(combined_couple_wages(p, s))),
              temj_wksht_table_1_others_lookup(persons_wages(p)))


# If line 1 is more than or equal to line 2, subtract line 2 from line 1. Enter the result here (if zero, enter “-0-”)
# and on Form W-4, line 5, page 1. Do not use the rest of this worksheet
def temj_wksht_line_3(p, s):
    return If(temj_wksht_line_1(p, s) >= temj_wksht_line_2(p, s),
              temj_wksht_line_2(p, s) - temj_wksht_line_1(p, s),
              temj_wksht_line_4(p, s))


# Note: If line 1 is less than line 2, enter “-0-” on Form W-4, line 5, page 1. Complete lines 4 through 9 below to
# figure the additional withholding amount necessary to avoid a year-end tax bill.
# Enter the number from line 2 of this worksheet
def temj_wksht_line_4(p, s):
    return temj_wksht_line_2(p, s)


# Enter the number from line 1 of this worksheet
def temj_wksht_line_5(p, s):
    return temj_wksht_line_1(p, s)


# 6 Subtract line 5 from line 4
def temj_wksht_line_6(p, s):
    return temj_wksht_line_4(p, s) - temj_wksht_line_5(p, s)


# Find the amount in Table 2 below that applies to the HIGHEST paying job and enter it here
def temj_wksht_line_7(p, s):
    return If(mfj(p),
              # assumes one job, needs to be expanded
              temj_wksht_table_2_mfj_lookup(Max([persons_wages(p), persons_wages(s)])),
              temj_wksht_table_2_others_lookup(persons_wages(p)))


# Multiply line 7 by line 6 and enter the result here. This is the additional annual withholding needed
def temj_wksht_line_8(p, s):
    return temj_wksht_line_6(p, s) * temj_wksht_line_7(p, s)


# Divide line 8 by the number of pay periods remaining in 2019. For example, divide by 18 if you’re paid every
# 2 weeks and you complete this form on a date in late April when there are 18 pay periods remaining in
# 2019. Enter the result here and on Form W-4, line 6, page 1. This is the additional amount to be withheld
# from each paycheck
def temj_wksht_line_9(p, s):
    return Trunc(temj_wksht_line_8(p, s) / pay_periods_remaining_in_year(p))


def highest_earning_job_from_couple(p, s):
    return Max([highest_earning_job_wages(p), highest_earning_job_wages(s)])


def temj_wksht_table_2_mfj_lookup(wages):
    return If(wages <= 24900, 420,
              wages <= 84450, 500,
              wages <= 173900, 910,
              wages <= 326950, 1000,
              wages <= 413700, 1330,
              wages <= 617851, 1450,
              1540)


def temj_wksht_table_2_others_lookup(wages):
    return If(wages <= 7200, 420,
              wages <= 36975, 500,
              wages <= 81700, 910,
              wages <= 158225, 1000,
              wages <= 201600, 1330,
              wages <= 507800, 1450,
              1540)


def temj_wksht_table_1_mfj_lookup(wages):
    return If(wages <= 5000, 0,
              wages <= 9500, 1,
              wages <= 19500, 2,
              wages <= 35000, 3,
              wages <= 40000, 4,
              wages <= 46000, 5,
              wages <= 55000, 6,
              wages <= 60000, 7,
              wages <= 70000, 8,
              wages <= 75000, 9,
              wages <= 85000, 10,
              wages <= 95000, 11,
              wages <= 125000, 12,
              wages <= 155000, 13,
              wages <= 165000, 14,
              wages <= 175000, 15,
              wages <= 180000, 16,
              wages <= 195000, 17,
              wages <= 205000, 18,
              19)


def temj_wksht_table_1_others_lookup(wages):
    return If(wages <= 7000, 0,
              wages <= 13000, 1,
              wages <= 27500, 2,
              wages <= 32000, 3,
              wages <= 40000, 4,
              wages <= 60000, 5,
              wages <= 75000, 6,
              wages <= 85000, 7,
              wages <= 95000, 8,
              wages <= 100000, 9,
              wages <= 110000, 10,
              wages <= 115000, 11,
              wages <= 125000, 12,
              wages <= 135000, 13,
              wages <= 145000, 14,
              wages <= 160000, 15,
              wages <= 180000, 16,
              17)


# FILING STATUSES


# Are the taxpayer and their spouse married filing jointly?
def mfj(p):
    return And(is_married(p),
               filing_jointly(p))


# Are the taxpayer and their spouse married filing separately?
def mfs(p, s):
    return And(is_married(p),
               filing_separately(p))


def filing_separately(p):
    return Not(filing_jointly(p))


# Status selected is MFJ
def filing_jointly(p):
    return tax_status(p) == "Married Filing Jointly"


# FAMILY STATUS


def is_married(p):
    return marital_status(p) == "Married"


# certainty < 1, is single single or is single/widowed single?
def is_single(p):
    return Or(marital_status(p) == "Single, unmarried, or legally separated",
              marital_status(p) == "Widowed (spouse died during the tax year)",
              marital_status(p) == "Widowed (spouse died before the tax year)")


# HOUSEHOLD EMPLOYMENT AND INCOME


def spouse_unemployed(s):
    return employment_status(s) != "Employed"


# Total income of a person and their spouse
def marital_income(p, s):
    return total_income(p) + total_income(s)


def combined_couple_wages(p, s):
    # wages from person's first job, wages from spouse's job
    return If(is_single(p), wages_from_second_job(p),
              wages_from_second_job(p) + persons_wages(s))


def has_only_one_job(p):
    return count_of_jobs(p) == 1


############### base input rules ###############
# base level attributes? Can we make these "fall out"?


def marital_status(p):
    return (In("str", "marital_status", p, None, "What is {0}'s marital status?"))


def tax_status(p):
    return In("str", "tax_status", p, None, "How does {0} plan to file taxes?")


def hoh(p):
    return (In("bool", "head_of_household", p, None, "Is {0} the head of their household?"))


def is_claiming_self(p):
    return (In("bool", "claim_self", p, None, "Does {0} intend to claim themself?"))


def employment_status(p):
    return (In("str", "employment_status", p, None, "What is {0}'s employment status?"))


def wages_from_second_job(p):
    return In("num", "second_job_wages", p, None,
              "What was the total sum of wages for {0} from their second job last year?")


def persons_wages(p):
    return In("num", "wages", p, None, "What was the total sum of wages for {0} last year?")


def count_of_jobs(p):
    return In("num", "number_of_jobs", p, None, "How many jobs did {0} simultaneously hold last year?")


def other_credits_pub505(p):
    return In("num", "other_credits_pub505", p, None,
              "How many other credits does {0} have from Worksheet 1-6 of Pub. 505? (Enter 0 if none.)")


# temporal?
def itemized_deductions_2019(p):
    return In("num", "itemized_deductions_2019", p, None,
              "Please enter the an estimate of {0}'s 2019 itemized deductions. "
              + "These include qualifying home mortgage interest, "
              + "charitable contributions, state and local taxes (up to $10,000), and medical expenses in excess of 10% of "
              + "your income. See Pub. 505 for details")


def estimate_2019_adj_to_inc_qual_bus_inc_ded_addtl_std_ded(p):
    return In("num", "itemized_deductions_2019", p, None, "Enter an estimate of {0}'s 2019 adjustments to income, "
              + "qualified business income deduction, and any additional standard deduction for age or blindness "
              + "(see Pub. 505 for information about these items) . . ")


def estimate_2019_nonwage_inc_not_subj_to_withholding(p):
    return In("num", "itemized_deductions_2019", p, None,
              "Enter an estimate of {0}'s 2019 nonwage income not subject to withholding (such as dividends or interest)")


def highest_earning_job_wages(p):
    return In("num", "highest_earning_job_total_wages", p, None, "Enter the wages from {0}'s highest earning job.")


def itemizing(p):
    return In("bool", "plans_to_itemize_or_claim_adjustments", p, None,
              "Does {0} plan  to itemize or claim adjustments to income and want to reduce "
              + "their withholding, or if do they have a large amount of nonwage income not subject to withholding and want to increase their withholding.")


def couple_both_work(p, s):
    return In("bool", "couple_both_work", p, s, "Do {0} and {1} both work?")


def pay_periods_remaining_in_year(p):
    return In("num", "pay_periods_remaining", p, None,
              "Enter the number of pay periods remaining in the year for {0}, " +
              "For example, divide by 18 if you’re paid every 2 weeks and you complete this form on a date in late April when " +
              "there are 18 pay periods remaining in the year")


def total_income(p):
    return In("num", "total_income", p, None, "Enter the total expected annual income for {0}")


def num_children(p):
    return In("num", "number_children_pub_972", p, None,
              "Enter the number of eligible children from Publication 972, Child Tax Credit for {0}")


def num_dependents(p):
    return In("num", "num_dep_pub_972", p, None,
              "Enter the number of eligible dependents from Publication 972, Child Tax Credit for {0}")


def qualifying_widower(p):
    return In("bool", "qualifying_widower", p, None, "Is {0} a qualifying widower?")
