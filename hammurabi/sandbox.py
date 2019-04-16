from akkadian import *
import hammurabi.us.fed.tax.indiv.withholding as w4
import hammurabi.shared.fam as fam


# result = ApplyRules([(w4.child_tax_credit_w_o_spouse, 'Jim')], [
#     Fact('total_income', 'Jim', None, 23423234400),
#     Fact('number_children_pub_972', 'Jim', None, 2)
# ])

Investigate([(fam.is_married, 'Jim')])

# print(result)

# print(Pretty(
    # w4.ctc_w_o_spouse('Jim')
    # w4.temj_wksht_required_couple('Jim', 'Sandy')
    # w4.form_w4_complete('Jim', 'Tanya')
    # w4.num_children('Jim')
#     w4.total_income('Jim')
# ))

