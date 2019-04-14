from akkadian import *
import hammurabi.us.fed.tax.indiv.withholding as w4


result = ApplyRules([(w4.child_tax_credit_w_o_spouse, 'Jim')], [
    Fact('total_income', 'Jim', None, 23423234400),
    Fact('number_children_pub_972', 'Jim', None, 2)
])

# print(result)

print(Pretty(
    # w4.child_tax_credit_w_o_spouse('Jim')
    # w4.form_w4_complete('Jim', 'Tanya')
    # w4.num_children('Jim')
#     w4.total_income('Jim')
))

