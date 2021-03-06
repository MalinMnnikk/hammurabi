import unittest

from akkadian import *


class TestDSL(unittest.TestCase):

    # _internal_asof

    def test_internal_asof_1(self):
        self.assertEqual(internal_asof(1, {1: "a", 234: "b", 1351: "c"}), "a")

    def test_internal_asof_2(self):
        self.assertEqual(internal_asof(5, {1: "a", 234: "b", 1351: "c"}), "a")

    def test_internal_asof_3(self):
        self.assertEqual(internal_asof(234, {1: "a", 234: "b", 1351: "c"}), "b")

    def test_internal_asof_4(self):
        self.assertEqual(internal_asof(238, {1: "a", 234: "b", 1351: "c"}), "b")

    def test_internal_asof_5(self):
        self.assertEqual(internal_asof(1351, {1: "a", 234: "b", 1351: "c"}), "c")

    def test_internal_asof_6(self):
        self.assertEqual(internal_asof(1400, {1: "a", 234: "b", 1351: "c"}), "c")

    # AsOf

    def test_asof_1(self):
        self.assertEqual(AsOf(Now, TS({Dawn: "a", '2002-02-02': "c"})), "c")

    def test_asof_2(self):
        self.assertEqual(Pretty(AsOf(TS({Dawn: Dawn, '2002-02-02': '2010-02-02'}), TS({Dawn: "a", '2002-02-02': "c"}))),
                         Pretty(TS({Dawn: "a", '2002-02-02': "c"})))

    def test_asof_3(self):
        self.assertEqual(Pretty(AsOf(TS({Dawn: Stub, '2002-02-02': '2010-02-02'}), TS({Dawn: "a", '2002-02-02': "c"}))),
                         Pretty(TS({Dawn: Stub, '2002-02-02': "c"})))

    def test_asof_4(self):
        self.assertEqual(Pretty(AsOf(TS({Dawn: Null, '2002-02-02': '2010-02-02'}), TS({Dawn: "a", '2002-02-02': "c"}))),
                         Pretty(TS({Dawn: Null, '2002-02-02': "c"})))

    def test_asof_5(self):
        self.assertEqual(Pretty(AsOf(TS({Dawn: Null, '2002-02-02': Stub}), TS({Dawn: "a", '2002-02-02': "c"}))),
                         Pretty(TS({Dawn: Null, '2002-02-02': Stub})))

    def test_asof_6(self):
        self.assertEqual(Pretty(AsOf(TS({Dawn: Null, '2002-02-02': Null}), TS({Dawn: "a", '2002-02-02': "c"}))),
                         Pretty(TS({Dawn: Null})))

    def test_asof_7(self):
        self.assertEqual(Pretty(AsOf(TS({Dawn: Null, '2002-02-02': Null}), TS({Dawn: "a", '2002-02-02': "c"}))),
                         Pretty(Eternal(Null)))

    def test_asof_8(self):
        self.assertEqual(Pretty(AsOf(Null, TS({Dawn: "a", '2002-02-02': "c"}))),
                         Pretty(Eternal(Null)))

    def test_asof_9(self):
        self.assertEqual(Pretty(AsOf(Now, TS({Dawn: "a", '2002-02-02': Stub}))),
                         Pretty(Eternal(Stub)))

    def test_asof_10(self):
        self.assertEqual(Pretty(AsOf(Now, Stub)),
                         Pretty(Eternal(Stub)))

    def test_asof_11(self):
        self.assertEqual(Pretty(AsOf(Null, Stub)),
                         Pretty(Eternal(Stub)))

    def test_asof_12(self):
        self.assertEqual(Pretty(AsOf(Stub, Null)),
                         Pretty(Eternal(Stub)))

    # Date conversions

    def test_date_conversions_1(self):
        self.assertEqual(date_to_ordinal(ordinal_to_date(32)), 32)

    def test_date_conversions_2(self):
        self.assertEqual(str_date_to_ordinal('2001-02-02'), 730518)

    # internal_ts_trim

    def test_internal_ts_trim_1(self):
        self.assertEqual(Pretty(TimeSeries(internal_ts_trim({1: Value("a"), 234: Value("a"), 1351: Value("c")}))),
                         Pretty(TimeSeries({1: Value("a"), 1351: Value("c")})))

    def test_internal_ts_trim_2(self):
        self.assertEqual(Pretty(TimeSeries(internal_ts_trim({1: Value("a"), 234: Value("b"), 1351: Value("c")}))),
                         Pretty(TimeSeries({1: Value("a"), 234: Value("b"), 1351: Value("c")})))

    # internal_ts_thread

    def test_internal_ts_thread_1(self):
        self.assertEqual(internal_ts_thread({1: 8234, 234: 921, 1351: 44},
                                            {1: 56, 1100: 32}),
                         {1: [8234, 56], 234: [921, 56], 1100: [921, 32], 1351: [44, 32]})

    # internal_ts_map

    def test_internal_ts_map_1(self):
        self.assertEqual(internal_ts_map_binary_fcn(operator.add, {1: [8234, 56], 234: [921, 56], 1100: [921, 32], 1351: [44, 32]}),
                         {1: 8290, 234: 977, 1100: 953, 1351: 76})

    # internal_and

    def test_internal_and_1(self):
        self.assertEqual(internal_and(Value(True), Value(False)).value, False)

    def test_internal_and_2(self):
        self.assertEqual(internal_and(Value(True), Value(True)).value, True)

    def test_internal_and_3(self):
        self.assertEqual(internal_and(Value(False), Value(False)).value, False)

    def test_internal_and_4(self):
        self.assertEqual(internal_and(Value(False), Value(True)).value, False)

    def test_internal_and_5(self):
        self.assertEqual(internal_and(Null, Value(True)).value, "Null")

    def test_internal_and_6(self):
        self.assertEqual(internal_and(Null, Value(False)).value, False)

    def test_internal_and_7(self):
        self.assertEqual(internal_and(Value(False), Null).value, False)

    def test_internal_and_8(self):
        self.assertEqual(internal_and(Value(True), Null).value, "Null")

    def test_internal_and_10(self):
        self.assertEqual(internal_and(Null, Null).value, "Null")

    def test_internal_and_11(self):
        self.assertEqual(internal_and(Value(True), True).value, True)

    def test_internal_and_12(self):
        self.assertEqual(internal_and(True, Value(True)).value, True)

    def test_internal_and_13(self):
        self.assertEqual(internal_and(False, Value(True)).value, False)

    def test_internal_and_14(self):
        self.assertEqual(internal_and(False, Null).value, False)

    def test_internal_and_17(self):
        self.assertEqual(internal_and(Stub, Value(True)).value, "Stub")

    def test_internal_and_18(self):
        self.assertEqual(internal_and(Value(True), Stub).value, "Stub")

    def test_internal_and_19(self):
        self.assertEqual(internal_and(Stub, Value(False)).value, False)

    def test_internal_and_20(self):
        self.assertEqual(internal_and(Value(False), Stub).value, False)

    def test_internal_and_21(self):
        self.assertEqual(internal_and(Stub, Null).value, "Null")

    def test_internal_and_22(self):
        self.assertEqual(internal_and(Null, Stub).value, "Null")

    # internal_or

    def test_internal_or_1(self):
        self.assertEqual(internal_or(Value(True), Value(False)).value, True)

    def test_internal_or_2(self):
        self.assertEqual(internal_or(Value(True), Value(True)).value, True)

    def test_internal_or_3(self):
        self.assertEqual(internal_or(Value(False), Value(False)).value, False)

    def test_internal_or_4(self):
        self.assertEqual(internal_or(Value(False), Value(True)).value, True)

    def test_internal_or_5(self):
        self.assertEqual(internal_or(Null, Value(True)).value, True)

    def test_internal_or_6(self):
        self.assertEqual(internal_or(Null, Value(False)).value, "Null")

    def test_internal_or_7(self):
        self.assertEqual(internal_or(Value(False), Null).value, "Null")

    def test_internal_or_8(self):
        self.assertEqual(internal_or(Value(True), Null).value, True)

    def test_internal_or_9(self):
        self.assertEqual(internal_or(Null, Null).value, "Null")

    def test_internal_or_10(self):
        self.assertEqual(internal_or(True, Value(True)).value, True)

    def test_internal_or_11(self):
        self.assertEqual(internal_or(False, Value(True)).value, True)

    def test_internal_or_12(self):
        self.assertEqual(internal_or(False, Null).value, "Null")

    def test_internal_or_13(self):
        self.assertEqual(internal_or(True, Null).value, True)

    def test_internal_or_14(self):
        self.assertEqual(internal_or(True, Value(False)).value, True)

    def test_internal_or_15(self):
        self.assertEqual(internal_or(Stub, Value(True)).value, True)

    def test_internal_or_16(self):
        self.assertEqual(internal_or(Value(True), Stub).value, True)

    def test_internal_or_17(self):
        self.assertEqual(internal_or(Stub, Value(False)).value, "Stub")

    def test_internal_or_18(self):
        self.assertEqual(internal_or(Value(False), Stub).value, "Stub")

    def test_internal_or_19(self):
        self.assertEqual(internal_or(Stub, Null).value, "Null")

    def test_internal_or_20(self):
        self.assertEqual(internal_or(Null, Stub).value, "Null")

    # internal_not

    def test_internal_not_1(self):
        self.assertEqual(internal_not(Value(True)).value, False)

    def test_internal_not_2(self):
        self.assertEqual(internal_not(Value(False)).value, True)

    def test_internal_not_3(self):
        self.assertEqual(internal_not(Null).value, "Null")

    def test_internal_not_4(self):
        self.assertEqual(internal_not(True).value, False)

    def test_internal_not_5(self):
        self.assertEqual(internal_not(False).value, True)

    def test_internal_not_6(self):
        self.assertEqual(internal_not(Stub).value, "Stub")

    # internal_ge

    def test_internal_ge_1(self):
        self.assertEqual(internal_ge(Value(99), Value(70)).value, True)

    def test_internal_ge_2(self):
        self.assertEqual(internal_ge(Value(70), Value(70)).value, True)

    def test_internal_ge_3(self):
        self.assertEqual(internal_ge(Value(99), Value(170)).value, False)

    def test_internal_ge_4(self):
        self.assertEqual(internal_ge(Value(99.023), Value(170)).value, False)

    def test_internal_ge_5(self):
        self.assertEqual(internal_ge(Value(99), 70).value, True)

    def test_internal_ge_6(self):
        self.assertEqual(internal_ge(354, Value(70)).value, True)

    def test_internal_ge_7(self):
        self.assertEqual(internal_ge(354, Value(670)).value, False)

    def test_internal_ge_8(self):
        self.assertEqual(internal_ge(354, Null).value, "Null")

    def test_internal_ge_9(self):
        self.assertEqual(internal_ge(Null, 34).value, "Null")

    def test_internal_ge_10(self):
        self.assertEqual(internal_ge(Null, Null).value, "Null")

    def test_internal_ge_11(self):
        self.assertEqual(internal_ge(Stub, Null).value, "Stub")

    def test_internal_ge_12(self):
        self.assertEqual(internal_ge(Null, Stub).value, "Stub")

    def test_internal_ge_13(self):
        self.assertEqual(internal_ge(Stub, 34).value, "Stub")

    def test_internal_ge_14(self):
        self.assertEqual(internal_ge(44, Stub).value, "Stub")

    # internal_gt

    def test_internal_gt_1(self):
        self.assertEqual(internal_gt(Value(99), Value(70)).value, True)

    def test_internal_gt_2(self):
        self.assertEqual(internal_gt(Value(70), Value(70)).value, False)

    def test_internal_gt_3(self):
        self.assertEqual(internal_gt(Value(99), Value(170)).value, False)

    def test_internal_gt_4(self):
        self.assertEqual(internal_gt(Value(99.023), Value(170)).value, False)

    def test_internal_gt_5(self):
        self.assertEqual(internal_gt(Value(99), 70).value, True)

    def test_internal_gt_6(self):
        self.assertEqual(internal_gt(354, Value(70)).value, True)

    def test_internal_gt_7(self):
        self.assertEqual(internal_gt(354, Value(670)).value, False)

    def test_internal_gt_8(self):
        self.assertEqual(internal_gt(354, Null).value, "Null")

    def test_internal_gt_9(self):
        self.assertEqual(internal_gt(Null, 34).value, "Null")

    def test_internal_gt_10(self):
        self.assertEqual(internal_gt(Null, Null).value, "Null")

    def test_internal_gt_11(self):
        self.assertEqual(internal_gt(Value('2000-01-01'), Value('1999-02-02')).value, True)

    def test_internal_gt_12(self):
        self.assertEqual(internal_gt(Value('2000-01-01'), Value('2010-02-02')).value, False)

    def test_internal_gt_13(self):
        self.assertEqual(internal_gt('2000-01-01', Value('1999-02-02')).value, True)

    def test_internal_gt_14(self):
        self.assertEqual(internal_gt('2000-01-01', Value('2010-02-02')).value, False)

    def test_internal_gt_15(self):
        self.assertEqual(internal_gt(Value('2000-01-01'), '1999-02-02').value, True)

    def test_internal_gt_16(self):
        self.assertEqual(internal_gt(Value('2000-01-01'), '2010-02-02').value, False)

    # internal_le

    def test_internal_le_1(self):
        self.assertEqual(internal_le(Value(99), Value(70)).value, False)

    def test_internal_le_2(self):
        self.assertEqual(internal_le(Value(70), Value(70)).value, True)

    def test_internal_le_3(self):
        self.assertEqual(internal_le(Value(99), Value(170)).value, True)

    def test_internal_le_4(self):
        self.assertEqual(internal_le(Value(99.023), Value(170)).value, True)

    def test_internal_le_5(self):
        self.assertEqual(internal_le(Value(99), 70).value, False)

    def test_internal_le_6(self):
        self.assertEqual(internal_le(354, Value(70)).value, False)

    def test_internal_le_7(self):
        self.assertEqual(internal_le(354, Value(670)).value, True)

    def test_internal_le_8(self):
        self.assertEqual(internal_le(354, Null).value, "Null")

    def test_internal_le_9(self):
        self.assertEqual(internal_le(Null, 34).value, "Null")

    def test_internal_le_10(self):
        self.assertEqual(internal_le(Null, Null).value, "Null")

    # internal_lt

    def test_internal_lt_1(self):
        self.assertEqual(internal_lt(Value(99), Value(70)).value, False)

    def test_internal_lt_2(self):
        self.assertEqual(internal_lt(Value(70), Value(70)).value, False)

    def test_internal_lt_3(self):
        self.assertEqual(internal_lt(Value(99), Value(170)).value, True)

    def test_internal_lt_4(self):
        self.assertEqual(internal_lt(Value(99.023), Value(170)).value, True)

    def test_internal_lt_5(self):
        self.assertEqual(internal_lt(Value(99), 70).value, False)

    def test_internal_lt_6(self):
        self.assertEqual(internal_lt(354, Value(70)).value, False)

    def test_internal_lt_7(self):
        self.assertEqual(internal_lt(354, Value(670)).value, True)

    def test_internal_lt_8(self):
        self.assertEqual(internal_lt(354, Null).value, "Null")

    def test_internal_lt_9(self):
        self.assertEqual(internal_lt(Null, 34).value, "Null")

    def test_internal_lt_10(self):
        self.assertEqual(internal_lt(Null, Null).value, "Null")

    # internal_eq

    def test_internal_eq_1(self):
        self.assertEqual(internal_eq(Value(99), Value(70)).value, False)

    def test_internal_eq_2(self):
        self.assertEqual(internal_eq(Value(70), Value(70)).value, True)

    def test_internal_eq_3(self):
        self.assertEqual(internal_eq(Value(99), 70).value, False)

    def test_internal_eq_4(self):
        self.assertEqual(internal_eq(354, Value(70)).value, False)

    def test_internal_eq_5(self):
        self.assertEqual(internal_eq(354, Value(354)).value, True)

    def test_internal_eq_6(self):
        self.assertEqual(internal_eq(354, Null).value, "Null")

    def test_internal_eq_7(self):
        self.assertEqual(internal_eq(Null, 34).value, "Null")

    def test_internal_eq_8(self):
        self.assertEqual(internal_eq(Null, Null).value, "Null")

    def test_internal_eq_9(self):
        self.assertEqual(internal_eq(Value("hello"), Value("hello")).value, True)

    def test_internal_eq_10(self):
        self.assertEqual(internal_eq(Value("hello"), Value("meow")).value, False)

    def test_internal_eq_11(self):
        self.assertEqual(internal_eq(Null, Value("meow")).value, "Null")

    def test_internal_eq_12(self):
        self.assertEqual(internal_eq(Value("hello"), Null).value, "Null")

    def test_internal_eq_13(self):
        self.assertEqual(internal_eq("hello", Null).value, "Null")

    def test_internal_eq_14(self):
        self.assertEqual(internal_eq("hello", Value("hello")).value, True)

    # internal_ne

    def test_internal_ne_1(self):
        self.assertEqual(internal_ne(Value(99), Value(70)).value, True)

    def test_internal_ne_2(self):
        self.assertEqual(internal_ne(Value(70), Value(70)).value, False)

    def test_internal_ne_3(self):
        self.assertEqual(internal_ne(Value(99), 70).value, True)

    def test_internal_ne_4(self):
        self.assertEqual(internal_ne(354, Value(70)).value, True)

    def test_internal_ne_5(self):
        self.assertEqual(internal_ne(354, Value(354)).value, False)

    def test_internal_ne_6(self):
        self.assertEqual(internal_ne(354, Null).value, "Null")

    def test_internal_ne_7(self):
        self.assertEqual(internal_ne(Null, 34).value, "Null")

    def test_internal_ne_8(self):
        self.assertEqual(internal_ne(Null, Null).value, "Null")

    def test_internal_ne_9(self):
        self.assertEqual(internal_ne(Value("hello"), Value("hello")).value, False)

    def test_internal_ne_10(self):
        self.assertEqual(internal_ne(Value("hello"), Value("meow")).value, True)

    def test_internal_ne_11(self):
        self.assertEqual(internal_ne(Null, Value("meow")).value, "Null")

    def test_internal_ne_12(self):
        self.assertEqual(internal_ne(Value("hello"), Null).value, "Null")

    # internal_add

    def test_internal_add_1(self):
        self.assertEqual(internal_add(Value(5), Value(7)).value, 12)

    def test_internal_add_2(self):
        self.assertEqual(internal_add(Value(4), Value(-9)).value, -5)

    def test_internal_add_3(self):
        self.assertEqual(internal_add(Value(99), 70).value, 169)

    def test_internal_add_4(self):
        self.assertEqual(internal_add(1, Value(70)).value, 71)

    def test_internal_add_5(self):
        self.assertEqual(internal_add(1, Value(354)).value, 355)

    def test_internal_add_6(self):
        self.assertEqual(internal_add(1, Null).value, "Null")

    def test_internal_add_7(self):
        self.assertEqual(internal_add(Null, 34).value, "Null")

    def test_internal_add_8(self):
        self.assertEqual(internal_add(Null, Null).value, "Null")

    # internal_mul

    def test_internal_mul_1(self):
        self.assertEqual(internal_mul(Value(5), Value(7)).value, 35)

    def test_internal_mul_2(self):
        self.assertEqual(internal_mul(Value(4), Value(-9)).value, -36)

    def test_internal_mul_3(self):
        self.assertEqual(internal_mul(Value(9), 7).value, 63)

    def test_internal_mul_4(self):
        self.assertEqual(internal_mul(1, Value(7)).value, 7)

    def test_internal_mul_5(self):
        self.assertEqual(internal_mul(1, Value(34)).value, 34)

    def test_internal_mul_6(self):
        self.assertEqual(internal_mul(1, Null).value, "Null")

    def test_internal_mul_7(self):
        self.assertEqual(internal_mul(Null, 34).value, "Null")

    def test_internal_mul_8(self):
        self.assertEqual(internal_mul(Null, Null).value, "Null")

    def test_internal_mul_9(self):
        self.assertEqual(internal_mul(Null, 0).value, 0)

    def test_internal_mul_10(self):
        self.assertEqual(internal_mul(0, Null).value, 0)

    def test_internal_mul_11(self):
        self.assertEqual(internal_mul(Stub, 0).value, 0)

    def test_internal_mul_12(self):
        self.assertEqual(internal_mul(0, Stub).value, 0)

    def test_internal_mul_13(self):
        self.assertEqual(internal_mul(Stub, 5).value, "Stub")

    def test_internal_mul_14(self):
        self.assertEqual(internal_mul(5, Stub).value, "Stub")

    # internal_sub

    def test_internal_sub_1(self):
        self.assertEqual(internal_sub(Value(5), Value(7)).value, -2)

    def test_internal_sub_2(self):
        self.assertEqual(internal_sub(Value(4), Value(-9)).value, 13)

    def test_internal_sub_3(self):
        self.assertEqual(internal_sub(Value(9), 7).value, 2)

    def test_internal_sub_4(self):
        self.assertEqual(internal_sub(1, Value(7)).value, -6)

    def test_internal_sub_5(self):
        self.assertEqual(internal_sub(1, Value(34)).value, -33)

    def test_internal_sub_6(self):
        self.assertEqual(internal_sub(1, Null).value, "Null")

    def test_internal_sub_7(self):
        self.assertEqual(internal_sub(Null, 34).value, "Null")

    def test_internal_sub_8(self):
        self.assertEqual(internal_sub(Null, Null).value, "Null")

    # internal_div

    def test_internal_div_1(self):
        self.assertEqual(internal_div(Value(6), Value(2)).value, 3)

    def test_internal_div_2(self):
        self.assertEqual(internal_div(Value(6), Value(-2)).value, -3)

    def test_internal_div_3(self):
        self.assertEqual(internal_div(Value(9), 3).value, 3)

    def test_internal_div_4(self):
        self.assertEqual(internal_div(12, Value(3)).value, 4)

    def test_internal_div_5(self):
        self.assertEqual(internal_div(12, Value(1)).value, 12)

    def test_internal_div_6(self):
        self.assertEqual(internal_div(1, Null).value, "Null")

    def test_internal_div_7(self):
        self.assertEqual(internal_div(Null, 34).value, "Null")

    def test_internal_div_8(self):
        self.assertEqual(internal_div(Null, Null).value, "Null")

    # internal_or (CFs)

    def test_cf_or_1(self):
        self.assertEqual(internal_or(Value(True, 1), Value(True, 1)).cf, 1)

    def test_cf_or_2(self):
        self.assertEqual(internal_or(Value(True, 0), Value(True, 1)).cf, 1)

    def test_cf_or_3(self):
        self.assertEqual(internal_or(Value(True, 0), Value(True, 0)).cf, 0)

    def test_cf_or_4(self):
        self.assertEqual(internal_or(Value(True, 1), Value(False, 1)).cf, 1)

    def test_cf_or_5(self):
        self.assertEqual(internal_or(Value(True, 0), Value(False, 1)).cf, 0)

    def test_cf_or_6(self):
        self.assertEqual(internal_or(Value(True, 1), Value(False, 0)).cf, 1)

    def test_cf_or_7(self):
        self.assertEqual(internal_or(Value(True, 0), Value(False, 0)).cf, 0)

    def test_cf_or_8(self):
        self.assertEqual(internal_or(Value(False, 1), Value(False, 1)).cf, 1)

    def test_cf_or_9(self):
        self.assertEqual(internal_or(Value(False, 0), Value(False, 1)).cf, 0)

    def test_cf_or_10(self):
        self.assertEqual(internal_or(Value(False, 0), Value(False, 0)).cf, 0)

    def test_cf_or_11(self):
        self.assertEqual(internal_or(Value(True, 1), Value(True, .7)).cf, 1)

    def test_cf_or_12(self):
        self.assertEqual(internal_or(Value(True, 0), Value(True, .7)).cf, .7)

    def test_cf_or_13(self):
        self.assertEqual(internal_or(Value(True, .3), Value(True, .7)).cf, .7)

    def test_cf_or_14(self):
        self.assertEqual(internal_or(Value(True, 1), Value(False, .4)).cf, 1)

    def test_cf_or_15(self):
        self.assertEqual(internal_or(Value(True, .4), Value(False, 1)).cf, .4)

    def test_cf_or_16(self):
        self.assertEqual(internal_or(Value(True, 0), Value(False, .4)).cf, 0)

    def test_cf_or_17(self):
        self.assertEqual(internal_or(Value(True, .2), Value(False, 0)).cf, .2)

    def test_cf_or_18(self):
        self.assertEqual(internal_or(Value(True, .4), Value(False, .5)).cf, .4)

    def test_cf_or_19(self):
        self.assertEqual(internal_or(Value(False, 1), Value(False, .4)).cf, .4)

    def test_cf_or_20(self):
        self.assertEqual(internal_or(Value(False, 0), Value(False, .4)).cf, 0)

    def test_cf_or_21(self):
        self.assertEqual(internal_or(Value(False, .6), Value(False, .4)).cf, .4)

    def test_cf_or_22(self):
        self.assertEqual(internal_or(Value("Null", cf=.6, null=True), Value("Null", cf=.4, null=True)).cf, .6)

    def test_cf_or_23(self):
        self.assertEqual(internal_or(Value("Null", cf=.6, null=True), Value("Stub", cf=.4, stub=True)).cf, .6)

    def test_cf_or_24(self):
        self.assertEqual(internal_or(Value("Stub", cf=.6, stub=True), Value("Stub", cf=.4, stub=True)).cf, .6)

    # internal_and (CFs)

    def test_cf_and_1(self):
        self.assertEqual(internal_and(Value(True, 1), Value(True, 1)).cf, 1)

    def test_cf_and_2(self):
        self.assertEqual(internal_and(Value(True, 0), Value(True, 1)).cf, 0)

    def test_cf_and_3(self):
        self.assertEqual(internal_and(Value(True, 0), Value(True, 0)).cf, 0)

    def test_cf_and_4(self):
        self.assertEqual(internal_and(Value(True, 1), Value(False, 1)).cf, 1)

    def test_cf_and_5(self):
        self.assertEqual(internal_and(Value(True, 0), Value(False, 1)).cf, 1)

    def test_cf_and_6(self):
        self.assertEqual(internal_and(Value(True, 1), Value(False, 0)).cf, 0)

    def test_cf_and_7(self):
        self.assertEqual(internal_and(Value(True, 0), Value(False, 0)).cf, 0)

    def test_cf_and_8(self):
        self.assertEqual(internal_and(Value(False, 1), Value(False, 1)).cf, 1)

    def test_cf_and_9(self):
        self.assertEqual(internal_and(Value(False, 0), Value(False, 1)).cf, 1)

    def test_cf_and_10(self):
        self.assertEqual(internal_and(Value(False, 0), Value(False, 0)).cf, 0)

    def test_cf_and_11(self):
        self.assertEqual(internal_and(Value(True, 1), Value(True, .7)).cf, .7)

    def test_cf_and_12(self):
        self.assertEqual(internal_and(Value(True, 0), Value(True, .7)).cf, 0)

    def test_cf_and_13(self):
        self.assertEqual(internal_and(Value(True, .3), Value(True, .7)).cf, .3)

    def test_cf_and_14(self):
        self.assertEqual(internal_and(Value(True, 1), Value(False, .4)).cf, .4)

    def test_cf_and_15(self):
        self.assertEqual(internal_and(Value(True, .4), Value(False, 1)).cf, 1)

    def test_cf_and_16(self):
        self.assertEqual(internal_and(Value(True, 0), Value(False, .4)).cf, .4)

    def test_cf_and_17(self):
        self.assertEqual(internal_and(Value(True, .2), Value(False, 0)).cf, 0)

    def test_cf_and_18(self):
        self.assertEqual(internal_and(Value(True, .4), Value(False, .5)).cf, .5)

    def test_cf_and_19(self):
        self.assertEqual(internal_and(Value(False, 1), Value(False, .4)).cf, 1)

    def test_cf_and_20(self):
        self.assertEqual(internal_and(Value(False, 0), Value(False, .4)).cf, .4)

    def test_cf_and_21(self):
        self.assertEqual(internal_and(Value(False, .6), Value(False, .4)).cf, .6)

    def test_cf_and_22(self):
        self.assertEqual(internal_and(Value("Null", cf=.6, null=True), Value("Null", cf=.4, null=True)).cf, .6)

    def test_cf_and_23(self):
        self.assertEqual(internal_and(Value("Null", cf=.6, null=True), Value("Stub", cf=.4, stub=True)).cf, .6)

    def test_cf_and_24(self):
        self.assertEqual(internal_and(Value("Stub", cf=.6, stub=True), Value("Stub", cf=.4, stub=True)).cf, .6)

   # internal_X (CFs)

    def test_cf_other_1(self):
        self.assertEqual(internal_add(Value(9, .5), Value(23, .7)).cf, 0.5)

    def test_cf_other_2(self):
        self.assertEqual(internal_not(Value(True, .4)).cf, 0.4)

    def test_cf_other_3(self):
        self.assertEqual(internal_mul(Value(3, .6), Value(0, .4)).cf, .4)

    def test_cf_other_4(self):
        self.assertEqual(internal_mul(Value(3, .3), Value(0, .4)).cf, .4)

    def test_cf_other_5(self):
        self.assertEqual(internal_mul(Value(0, .6), Value(0, .4)).cf, .6)

    def test_cf_other_6(self):
        self.assertEqual(internal_add(Value(8, .6), Value(1, .4)).cf, .4)

    def test_cf_other_7(self):
        self.assertEqual(internal_add(Value("Null", cf=.6, null=True), Value(1, .4)).cf, .6)

    def test_cf_other_8(self):
        self.assertEqual(internal_add(Value("Null", cf=.6, null=True), Value("Null", cf=.4, null=True)).cf, .6)

    def test_cf_other_9(self):
        self.assertEqual(internal_add(Value("Stub", cf=.6, stub=True), Value(1, .4)).cf, .6)

    def test_cf_other_10(self):
        self.assertEqual(internal_add(Value("Stub", cf=.6, stub=True), Value("Stub", cf=.4, stub=True)).cf, .6)

    def test_cf_other_11(self):
        self.assertEqual(internal_add(Value("Stub", cf=.6, stub=True), Value("Null", cf=.4, null=True)).cf, .6)

    # def test_list_contains_none_1(self):
    #     self.assertEqual(list_contains_none([3, V(None), 8]), True)
    #
    # def test_list_contains_none_2(self):
    #     self.assertEqual(list_contains_none([3, 4, 8]), False)
    #
    # def test_list_contains_none_3(self):
    #     self.assertEqual(list_contains_none([]), False)

    # Constructing time series

    def test_ts_construction_1(self):
        self.assertEqual(Pretty(EffectiveFrom('2020-01-01')),
                         Pretty(TS({Dawn: False, '2020-01-01': True})))

    def test_ts_construction_2(self):
        self.assertEqual(Pretty(EffectiveUntil('2020-01-01')),
                         Pretty(TS({Dawn: True, '2020-01-02': False})))

    def test_ts_construction_3(self):
        self.assertEqual(Pretty(EffectiveBetween('2020-01-01', '2021-01-01')),
                         Pretty(TS({Dawn: False, '2020-01-01': True, '2021-01-02': False})))

    def test_ts_construction_4(self):
        self.assertEqual(Pretty(TS({Dawn: False, '2020-01-01': True, '2021-01-01': True})),
                         Pretty(TS({Dawn: False, '2020-01-01': True})))

    # Time series AND

    def test_ts_and_1(self):
        self.assertEqual(Pretty(And(tsbool1, tsbool2)),
                         Pretty(TS({Dawn: False,
                                     '2020-01-01': True,
                                     '2021-01-01': Null,
                                     '2023-01-01': False,
                                     '2024-01-01': Null})))

    def test_ts_and_2(self):
        self.assertEqual(Pretty(And(tsbool2, Stub)),
                         Pretty(TS({Dawn: Stub,
                                    '2023-01-01': False,
                                    '2024-01-01': Stub})))

    def test_ts_and_3(self):
        self.assertEqual(Pretty(And(tsbool1, Stub)),
                         Pretty(TS({Dawn: False,
                                    '2020-01-01': Stub,
                                    '2021-01-01': Null})))

    def test_ts_and_4(self):
        self.assertEqual(Pretty(And(True,
                                    TS({Dawn: Stub,
                                        '1997-09-01': False,
                                        '2008-07-24': True}))),
                         Pretty(TS({Dawn: Stub,
                                    '1997-09-01': False,
                                    '2008-07-24': True})))

    def test_ts_and_5(self):
        self.assertEqual(Pretty(And(False, TS({Dawn: Stub,
                                                 '1997-09-01': False,
                                                 '2008-07-24': True}))),
                         Pretty(TimeSeries({1: Value(False)})))

    def test_ts_and_6(self):
        self.assertEqual(Pretty(And(Stub, False)),
                         Pretty(Eternal(False)))

    def test_ts_and_7(self):
        self.assertEqual(Pretty(And(False, Null, True)), Pretty(Eternal(False)))

    # Time series OR

    def test_ts_or_1(self):
        self.assertEqual(Pretty(Or(tsbool1, tsbool2)),
                         Pretty(TS({Dawn: True,
                                    '2023-01-01': Null})))

    def test_ts_or_2(self):
        self.assertEqual(Pretty(Or(tsbool2, Stub)),
                         Pretty(TS({Dawn: True,
                                    '2023-01-01': Stub})))

    def test_ts_or_3(self):
        self.assertEqual(Pretty(Or(tsbool1, Stub)),
                         Pretty(TS({Dawn: Stub,
                                    '2020-01-01': True,
                                    '2021-01-01': Null})))

    def test_ts_or_4(self):
        self.assertEqual(Pretty(Or(False,
                                   TS({Dawn: Stub,
                                       '1997-09-01': False,
                                       '2008-07-24': True}))),
                         Pretty(TS({Dawn: Stub,
                                    '1997-09-01': False,
                                    '2008-07-24': True})))

    def test_ts_or_5(self):
        self.assertEqual(Pretty(Or(True,
                                   TS({Dawn: Stub,
                                       '1997-09-01': False,
                                       '2008-07-24': True}))),
                         Pretty(Eternal(True)))

    # Time series NOT

    def test_ts_not_1(self):
        self.assertEqual(Pretty(Not(tsbool1)),
                         Pretty(TS({Dawn: True, '2020-01-01': False, '2021-01-01': Null})))

    def test_ts_not_2(self):
        self.assertEqual(Pretty(Not(tsbool2)),
                         Pretty(TS({Dawn: False, '2023-01-01': True, '2024-01-01': Stub})))

    def test_ts_not_3(self):
        self.assertEqual(Pretty(Not(Eternal(True))),
                         Pretty(Eternal(False)))

    def test_ts_not_4(self):
        self.assertEqual(Pretty(Not(True)),
                         Pretty(Eternal(False)))

    # Time series addition

    def test_ts_add_1(self):
        self.assertEqual(Pretty(tsnum1 + tsnum2),
                         Pretty(TS({Dawn: 28,
                                    '2020-01-01': 32,
                                    '2021-01-01': Null,
                                    '2024-01-01': Stub})))

    # Time series subtraction

    def test_ts_sub_1(self):
        self.assertEqual(Pretty(tsnum1 - tsnum2),
                         Pretty(TS({Dawn: -20,
                                    '2020-01-01': -16,
                                    '2021-01-01': Null,
                                    '2024-01-01': Stub})))

    # Time series multiplication

    def test_ts_mult_1(self):
        self.assertEqual(Pretty(tsnum1 * tsnum2),
                         Pretty(TS({Dawn: 96,
                                    '2020-01-01': 192,
                                    '2021-01-01': Null,
                                    '2024-01-01': Stub})))

    def test_ts_mult_2(self):
        self.assertEqual(Pretty(tsnum1 * 0),
                         Pretty(Eternal(0)))

    def test_ts_mult_3(self):
        self.assertEqual(Pretty(TS({Dawn: 0, '2020-01-01': 8}) * 5),
                         Pretty(TS({Dawn: 0, '2020-01-01': 40})))

    # Equality of two time series

    def test_ts_eq_1(self):
        self.assertEqual(Pretty(tsnum1 == tsnum2),
                         Pretty(TS({Dawn: False,
                                    '2021-01-01': Null,
                                    '2024-01-01': Stub})))

    def test_ts_eq_2(self):
        self.assertEqual(Pretty(TS({Dawn: 5}) == Eternal(5)),
                         Pretty(Eternal(True)))

    # Time series comparison

    def test_ts_cmp_1(self):
        self.assertEqual(Pretty(TS({Dawn: 4, '2020-01-01': 8}) > 5),
                         Pretty(TS({Dawn: False,
                                    '2020-01-01': True})))

    def test_ts_cmp_2(self):
        self.assertEqual(Pretty(TS({Dawn: 4, '2020-01-01': 8}) >= 5),
                         Pretty(TS({Dawn: False, '2020-01-01': True})))

    def test_ts_cmp_3(self):
        self.assertEqual(Pretty(TS({Dawn: 4, '2020-01-01': 8}) >= 3),
                         Pretty(TS({Dawn: True})))

    def test_ts_cmp_4(self):
        self.assertEqual(Pretty(Eternal(3) >= 3),
                         Pretty(Eternal(True)))

    def test_ts_cmp_5(self):
        self.assertEqual(Pretty(TS({Dawn: 4, '2020-01-01': 8}) != 3),
                         Pretty(TS({Dawn: True})))

    def test_ts_cmp_6(self):
        self.assertEqual(Pretty(TS({Dawn: 4, '2020-01-01': 8}) != 4),
                         Pretty(TS({Dawn: False, '2020-01-01': True})))

    # AddDays

    def test_adddays_1(self):
        self.assertEqual(
            Pretty(AddDays2(TS({Dawn: '2001-02-02', '2010-08-03': '2020-08-10'}),
                            TS({Dawn: 23, '2010-02-03': 234}))),
            Pretty(TS({Dawn: '2001-02-25',
                       '2010-02-03': '2001-09-24',
                       '2010-08-03': '2021-04-01'})))

    def test_adddays_2(self):
        self.assertEqual(
            Pretty(AddDays2('2000-01-01', TS({Dawn: 23, '2010-02-03': 234}))),
            Pretty(TS({Dawn: '2000-01-24', '2010-02-03': '2000-08-22'})))

    def test_adddays_3(self):
        self.assertEqual(
            Pretty(AddDays2('2000-01-01', 5232)),
            Pretty(Eternal('2014-04-29')))

    def test_adddays_4(self):
        self.assertEqual(
            Pretty(AddDays2('2000-01-01', Stub)),
            Pretty(Eternal(Stub)))

    def test_adddays_5(self):
        self.assertEqual(
            Pretty(AddDays2('2000-01-01', Null)),
            Pretty(Eternal(Null)))

    def test_adddays_6(self):
        self.assertEqual(
            Pretty(AddDays2('2000-01-01', TS({Dawn: 23, '2010-02-03': Null}))),
            Pretty(TS({Dawn: '2000-01-24', '2010-02-03': Null})))

    # AddYears

    def test_addyears_1(self):
        self.assertEqual(
            Pretty(AddYears2('2000-01-01', 4)),
            Pretty(Eternal('2004-01-01')))

    def test_addyears_2(self):
        self.assertEqual(
            Pretty(AddYears2('2000-01-01', -4)),
            Pretty(Eternal('1996-01-01')))

    # Pretty

    def test_pretty_1(self):
        self.assertEqual(Pretty(TimeSeries({1: Value(5)})), "5 (100% certain)")


    # if_for_values

    def test_if_for_values_1(self):
        self.assertEqual(if_for_values(Null, 1, 2).value, "Null")

    def test_if_for_values_2(self):
        self.assertEqual(if_for_values(Value(True), 1, 2).value, 1)

    def test_if_for_values_3(self):
        self.assertEqual(if_for_values(True, 1, 2).value, 1)

    def test_if_for_values_4(self):
        self.assertEqual(if_for_values(Value(False), 1, 2).value, 2)

    def test_if_for_values_5(self):
        self.assertEqual(if_for_values(False, 1, 2).value, 2)

    def test_if_for_values_6(self):
        self.assertEqual(if_for_values(Stub, 1, 2).value, "Stub")

    def test_if_for_values_7(self):
        self.assertEqual(if_for_values(True, Stub, 2).value, "Stub")

    # if_for_values (CFs)

    def test_if_cf_1(self):
        self.assertEqual(if_for_values(Value(True,.8), Value(1, .9),
                                       Value(True,.3), Value(1, .5),
                                       Value(True,.6), Value(1, .2)).cf, .8)

    def test_if_cf_2(self):
        self.assertEqual(if_for_values(Value(True,.8), Value(1, .2),
                                       Value(True,.3), Value(1, .5),
                                       Value(True,.6), Value(1, .2)).cf, .2)

    def test_if_cf_3(self):
        self.assertEqual(if_for_values(Value(False,.8), Value(1, .9),
                                       Value(True,.3), Value(1, .5),
                                       Value(True,.6), Value(1, .2)).cf, .3)

    def test_if_cf_4(self):
        self.assertEqual(if_for_values(Value(False,.8), Value(1, .9),
                                       Value(True,.6), Value(1, .5),
                                       Value(True,.6), Value(1, .2)).cf, .5)

    def test_if_cf_5(self):
        self.assertEqual(if_for_values(Value(False,.8), Value(1, .9),
                                       Value(False,.6), Value(1, .5),
                                       Value(True,.6), Value(1, .2)).cf, .2)

    def test_if_cf_6(self):
        self.assertEqual(if_for_values(Value(False,.8), Value(1, .9),
                                       Value(False,.1), Value(1, .5),
                                       Value(True,.6), Value(1, .2)).cf, .1)

    def test_if_cf_7(self):
        self.assertEqual(if_for_values(Value(False,.8), Value(1, .9),
                                       Value(False,.6), Value(1, .5),
                                       Value(True,.5), Value(1, .9)).cf, .5)

    # If

    def test_if_1(self):
        self.assertEqual(Pretty(If(Null, 1, 2)),
                         Pretty(Eternal(Null)))

    def test_if_2(self):
        self.assertEqual(Pretty(If(True, 1, 2)),
                         Pretty(Eternal(1)))

    def test_if_3(self):
        self.assertEqual(Pretty(If(False, 1, 2)),
                         Pretty(Eternal(2)))

    def test_if_4(self):
        self.assertEqual(Pretty(If(Eternal(True), 1, 2)),
                         Pretty(Eternal(1)))

    def test_if_5(self):
        self.assertEqual(Pretty(If(Eternal(False), 1, 2)),
                         Pretty(Eternal(2)))

    def test_if_6(self):
        self.assertEqual(Pretty(If(Eternal(False), Eternal(1), Eternal(2))),
                         Pretty(Eternal(2)))

    # internal_map

    def test_internal_map_1(self):
        self.assertEqual(internal_map(lambda x: x * 8, [3, 5, 8]).value, [24, 40, 64])

    def test_internal_map_2(self):
        self.assertEqual(internal_map(lambda x: x * 8, Value([3, 5, 8])).value, [24, 40, 64])

    def test_internal_map_3(self):
        self.assertEqual(internal_map(lambda x: x * 8, Null).value, "Null")

    def test_internal_map_4(self):
        self.assertEqual(internal_map(lambda x: x * 8, Stub).value, "Stub")

    def test_internal_map_5(self):
        self.assertEqual(internal_map(lambda x: x * 8, [3, Null, 8]).value, "Null")

    def test_internal_map_6(self):
        self.assertEqual(internal_map(lambda x: x * 8, Value([3, Null, 8])).value, "Null")

    def test_internal_map_7(self):
        self.assertEqual(internal_map(lambda x: x * 8, Stub).value, "Stub")

    # MAP

    def test_map_1(self):
        self.assertEqual(Pretty(Map(lambda x: x * 8, [3, 5, 8])),
                         Pretty(Eternal([24, 40, 64])))

    # internal_any

    def test_internal_any_1(self):
        self.assertEqual(internal_any([3, 5, 8]).value, False)

    def test_internal_any_2(self):
        self.assertEqual(internal_any(Value([3, 5, 8])).value, False)

    def test_internal_any_3(self):
        self.assertEqual(internal_any(Value([3, 5, True])).value, True)

    def test_internal_any_4(self):
        self.assertEqual(internal_any(Value([3, 5, Value(True)])).value, True)

    def test_internal_any_5(self):
        self.assertEqual(internal_any([3, 5, Value(True)]).value, True)

    def test_internal_any_6(self):
        self.assertEqual(internal_any([3, 5, Value(False)]).value, False)

    def test_internal_any_7(self):
        self.assertEqual(internal_any([3, 5, Null]).value, "Null")

    def test_internal_any_8(self):
        self.assertEqual(internal_any(Null).value, "Null")

    def test_internal_any_9(self):
        self.assertEqual(internal_any([3, 5, Stub]).value, "Stub")

    def test_internal_any_10(self):
        self.assertEqual(internal_any(Stub).value, "Stub")

    def test_internal_any_11(self):
        self.assertEqual(internal_any([3, True, Stub]).value, True)

    def test_internal_any_12(self):
        self.assertEqual(internal_any([True, Stub]).value, True)

    def test_internal_any_13(self):
        self.assertEqual(internal_any([Value(True), Stub]).value, True)

    def test_internal_any_14(self):
        self.assertEqual(internal_any([False, False, True]).value, True)

    # ANY

    def test_any_1(self):
        self.assertEqual(Pretty(Any(Eternal([True, False, False]))),
                         Pretty(Eternal(True)))

    # internal_all

    def test_internal_all_1(self):
        self.assertEqual(internal_all([3, 5, 8]).value, False)

    def test_internal_all_2(self):
        self.assertEqual(internal_all(Value([3, 5, 8])).value, False)

    def test_internal_all_3(self):
        self.assertEqual(internal_all(Value([3, 5, True])).value, False)

    def test_internal_all_4(self):
        self.assertEqual(internal_all(Value([3, 5, Value(True)])).value, False)

    def test_internal_all_5(self):
        self.assertEqual(internal_all([3, 5, Value(True)]).value, False)

    def test_internal_all_6(self):
        self.assertEqual(internal_all([3, 5, Value(False)]).value, False)

    def test_internal_all_7(self):
        self.assertEqual(internal_all([Value(True), Value(True), Value(True)]).value, True)

    def test_internal_all_8(self):
        self.assertEqual(internal_all([Value(True), True, Value(True)]).value, True)

    def test_internal_all_9(self):
        self.assertEqual(internal_all([3, 5, Stub]).value, "Stub")

    def test_internal_all_10(self):
        self.assertEqual(internal_all(Stub).value, "Stub")

    def test_internal_all_11(self):
        self.assertEqual(internal_all([3, False, Stub]).value, False)

    def test_internal_all_12(self):
        self.assertEqual(internal_all([False, Stub]).value, False)

    def test_internal_all_13(self):
        self.assertEqual(internal_all([Value(False), Stub]).value, False)

    # ALL

    def test_all_1(self):
        self.assertEqual(Pretty(All(Eternal([True, False, False]))),
                         Pretty(Eternal(False)))

    def test_all_2(self):
        self.assertEqual(Pretty(All(Eternal([True, True, True]))),
                         Pretty(Eternal(True)))

    # EXISTS

    def test_exists_1(self):
        self.assertEqual(Exists(lambda x: x > 6, Eternal([3, 5, 8])), True)

    def test_exists_2(self):
        self.assertEqual(Exists(lambda x: x > 16, Eternal([3, 5, 8])), False)

    # FORALL

    def test_forall_1(self):
        self.assertEqual(ForAll(lambda x: x > 6, Eternal([3, 5, 8])), False)

    def test_forall_2(self):
        self.assertEqual(ForAll(lambda x: x > 1, Eternal([3, 5, 8])), True)

    # ComposeTS

    def test_compose_ts_1(self):
        self.assertEqual(Pretty(ComposeTS([Dawn,'2003-04-02','2009-03-04'], [3,4,5])),
                         Pretty(TS({Dawn: 3, '2003-04-02': 4, '2009-03-04': 5})))

    # IsNull

    def test_is_null_1(self):
        self.assertEqual(Pretty(IsNull(TS({Dawn: 3, '2003-04-02': Null, '2009-03-04': 5}))),
                         Pretty(TS({Dawn: False, '2003-04-02': True, '2009-03-04': False})))

    def test_is_null_2(self):
        self.assertEqual(Pretty(IsNull(TS({Dawn: 3, '2003-04-02': 4, '2009-03-04': 5}))),
                         Pretty(TS({Dawn: False})))

    def test_is_null_3(self):
        self.assertEqual(Pretty(IsNull(TS({Dawn: Null}))),
                         Pretty(TS({Dawn: True})))

    # Manipulating CFs

    def test_get_cf_1(self):
        self.assertEqual(Pretty(GetCF(TS({Dawn: 3, '2003-04-02': Null, '2009-03-04': 5}))),
                         Pretty(TS({Dawn: 1})))

    def test_get_cf_2(self):
        self.assertEqual(Pretty(GetCF(TS({Dawn: Value(3,cf=.8), '2003-04-02': Value(3,cf=.2), '2009-03-04': Value(3,cf=.1)}))),
                         Pretty(TS({Dawn: .8, '2003-04-02': .2, '2009-03-04': .1})))

    def test_get_cf_3(self):
        self.assertEqual(Pretty(GetCF(TS({Dawn: Value(3,cf=.2), '2003-04-02': Value(3,cf=.2), '2009-03-04': Value(3,cf=.2)}))),
                         Pretty(Eternal(.2)))

    def test_set_cf_1(self):
        self.assertEqual(Pretty(SetCF(TS({Dawn: 3, '2003-04-02': 4}),
                                      TS({Dawn: .2, '2005-04-02': .8}))),
                         Pretty(TS({Dawn: Value(3, cf=.2), '2003-04-02': Value(4, cf=.2), '2005-04-02': Value(4, cf=.8)})))

    def test_set_cf_2(self):
        self.assertEqual(Pretty(SetCF(TS({Dawn: 3, '2003-04-02': 4}), Eternal(.7))),
                         Pretty(TS({Dawn: Value(3, cf=.7), '2003-04-02': Value(4, cf=.7)})))

    def test_set_cf_3(self):
        self.assertEqual(Pretty(SetCF(TS({Dawn: 3, '2003-04-02': 4}), .7)),
                         Pretty(TS({Dawn: Value(3, cf=.7), '2003-04-02': Value(4, cf=.7)})))

    def test_set_cf_4(self):
        self.assertEqual(Pretty(SetCF(234, .7)),
                         Pretty(TS({Dawn: Value(234, cf=.7)})))

    def test_rescale_cf_1(self):
        self.assertEqual(Pretty(RescaleCF(TS({Dawn: Value(3, cf=1), '2003-04-02': Value(4, cf=.5)}), .5)),
                         Pretty(TS({Dawn: Value(3, cf=.5), '2003-04-02': Value(4, cf=.25)})))

    # Simple mathematical functions

    def test_math_1(self):
        self.assertEqual(Pretty(Ceil(TS({Dawn: 3, '2003-04-02': Null, '2009-03-04': 5}))),
                         Pretty(TS({Dawn: 3, '2003-04-02': Null, '2009-03-04': 5})))

    def test_math_2(self):
        self.assertEqual(Pretty(Ceil(TS({Dawn: 3.5, '2003-04-02': Stub, '2009-03-04': 5.0}))),
                         Pretty(TS({Dawn: 4, '2003-04-02': Stub, '2009-03-04': 5})))

    def test_math_3(self):
        self.assertEqual(Pretty(Ceil(Eternal(3.4))),
                         Pretty(Eternal(4)))

    def test_math_4(self):
        self.assertEqual(Pretty(Ceil(3.4)),
                         Pretty(Eternal(4)))

    def test_math_5(self):
        self.assertEqual(Pretty(Floor(3.4)),
                         Pretty(Eternal(3)))

    def test_math_6(self):
        self.assertEqual(Pretty(Pow(TS({Dawn: 2, '2003-04-02': Stub, '2009-03-04': 3}), 2)),
                         Pretty(TS({Dawn: 4.0, '2003-04-02': Stub, '2009-03-04': 9.0})))

    # DayDelta

    def test_day_delta_1(self):
        self.assertEqual(Pretty(DayDelta('2000-01-01', TS({Dawn: '2003-04-02', '2013-04-02': '2023-04-02'}))),
                         Pretty(TS({Dawn: 1187, '2013-04-02': 8492})))

    def test_day_delta_2(self):
        self.assertEqual(Pretty(DayDelta('2000-01-01', '2000-01-03')),
                         Pretty(Eternal(2)))

    def test_day_delta_3(self):
        self.assertEqual(Pretty(DayDelta('2000-01-01', Stub)),
                         Pretty(Eternal(Stub)))

    # Date decomposition

    def test_date_decomp_1(self):
        self.assertEqual(Pretty(Year(TS({Dawn: '2003-04-02', '2013-04-02': '2023-04-02'}))),
                         Pretty(TS({Dawn: 2003, '2013-04-02': 2023})))

    def test_date_decomp_2(self):
        self.assertEqual(Pretty(Month(TS({Dawn: '2003-04-02', '2013-04-02': '2023-04-02'}))),
                         Pretty(Eternal(4)))

    def test_date_decomp_3(self):
        self.assertEqual(Pretty(Day(TS({Dawn: '2003-04-02', '2013-04-02': '2023-04-02'}))),
                         Pretty(Eternal(2)))

    # internal_min

    def test_internal_min_1(self):
        self.assertEqual(internal_min([3, 5, 8]).value, 3)

    def test_internal_min_2(self):
        self.assertEqual(internal_min([13, 5, 8]).value, 5)

    def test_internal_min_3(self):
        self.assertEqual(internal_min([13, Stub, 8]).value, "Stub")

    def test_internal_min_4(self):
        self.assertEqual(internal_min([13, Stub, Null]).value, "Stub")

    def test_internal_min_5(self):
        self.assertEqual(internal_min([13, 6, Null]).value, "Null")

    def test_internal_min_6(self):
        self.assertEqual(internal_min(Null).value, "Null")

    # Min

    def test_min_1(self):
        self.assertEqual(Pretty(Min([3, 5, 8])),
                         Pretty(Eternal(3)))

    def test_min_2(self):
        self.assertEqual(Pretty(Min(Eternal([3, 5, 8]))),
                         Pretty(Eternal(3)))

    def test_min_3(self):
        self.assertEqual(Pretty(Min(Stub)),
                         Pretty(Eternal(Stub)))

    def test_min_4(self):
        self.assertEqual(Pretty(Min([3, Eternal(5), 8])),
                         Pretty(Eternal(3)))

    def test_min_5(self):
        self.assertEqual(Pretty(Min([Stub, Eternal(5), 8])),
                         Pretty(Eternal(Stub)))

    # normalize_list_of_ts

    def test_normalize_list_of_ts_1(self):
        self.assertEqual(Pretty(normalize_list_of_ts([3, 4])),
                         Pretty(Eternal([3, 4])))

    def test_normalize_list_of_ts_2(self):
        self.assertEqual(Pretty(normalize_list_of_ts([3, Eternal(4), 5])),
                         Pretty(Eternal([3, 4, 5])))

    # ToScalar

    def test_to_scalar_1(self):
        self.assertEqual(ToScalar(Eternal("a")), "a")

    def test_to_scalar_2(self):
        self.assertEqual(ToScalar("a"), "a")

    def test_to_scalar_3(self):
        self.assertEqual(ToScalar(TS({Dawn: 32, '2011-01-01': 44})), 32)

    def test_to_scalar_4(self):
        self.assertEqual(ToScalar(TS({Dawn: 32, Now: 44})), 32)

    # Intersection

    def test_intersection_1(self):
        self.assertEqual(Pretty(Intersection([4, 5, 6], [5, TS({Dawn: 9, '2002-02-02': 2})])),
                         Pretty(Eternal([5])))

    def test_intersection_2(self):
        self.assertEqual(Pretty(Intersection([4, 5, 6], [5, 6, 7])),
                         Pretty(Eternal([5, 6])))

    def test_intersection_3(self):
        self.assertEqual(Pretty(Intersection([4, 5, 6], [8, 2])),
                         Pretty(Eternal([])))

    def test_intersection_4(self):
        self.assertEqual(Pretty(Intersection([4, 5, 6, 2], [5, TS({Dawn: 9, '2002-02-02': 2})])),
                         Pretty(TS({Dawn: [5], '2002-02-02': [2, 5]})))

    def test_intersection_5(self):
        self.assertEqual(Pretty(Intersection(Null, [5, TS({Dawn: 9, '2002-02-02': 2})])),
                         Pretty(Eternal(Null)))

    def test_intersection_6(self):
        self.assertEqual(Pretty(Intersection(Stub, [5, TS({Dawn: 9, '2002-02-02': 2})])),
                         Pretty(Eternal(Stub)))

    def test_intersection_7(self):
        self.assertEqual(Pretty(Intersection([4, 5, 6, 2], [5, TS({Dawn: Stub, '2002-02-02': 2})])),
                         Pretty(TS({Dawn: Stub, '2002-02-02': [2, 5]})))

    def test_intersection_8(self):
        self.assertEqual(Pretty(Intersection([4, 5, 6, 2], [5, TS({Dawn: 9, '2002-02-02': Stub})])),
                         Pretty(TS({Dawn: [5], '2002-02-02': Stub})))

    def test_intersection_9(self):
        self.assertEqual(Pretty(Intersection([4, Stub, 6, 2], [5, TS({Dawn: 9, '2002-02-02': Stub})])),
                         Pretty(Eternal(Stub)))

    def test_intersection_10(self):
        self.assertEqual(Pretty(Intersection(Null, Stub)),
                         Pretty(Eternal(Stub)))

    # Union

    def test_union_1(self):
        self.assertEqual(Pretty(Union([4, 5, 6], [5, 6, 7])),
                         Pretty(Eternal([4, 5, 6, 7])))

    # IsSubsetOf

    def test_is_subset_of_1(self):
        self.assertEqual(Pretty(IsSubsetOf([4, 5, 6], [5, 6, 7])),
                         Pretty(Eternal(False)))

    def test_is_subset_of_2(self):
        self.assertEqual(Pretty(IsSubsetOf([4], [2, 6, 7])),
                         Pretty(Eternal(False)))

    def test_is_subset_of_3(self):
        self.assertEqual(Pretty(IsSubsetOf([4], [4, 6, 7])),
                         Pretty(Eternal(True)))

    def test_is_subset_of_4(self):
        self.assertEqual(Pretty(IsSubsetOf([4, 6, 7], [4])),
                         Pretty(Eternal(False)))

    # IsSubsetOf

    def test_is_in_1(self):
        self.assertEqual(Pretty(IsIn(5, [5, 6, 7])),
                         Pretty(Eternal(True)))

    def test_is_in_2(self):
        self.assertEqual(Pretty(IsIn(2, [5, 6, 7])),
                         Pretty(Eternal(False)))

    def test_is_in_3(self):
        self.assertEqual(Pretty(IsIn("Marcia", ["Sam", "Pat"])),
                         Pretty(Eternal(False)))

    def test_is_in_4(self):
        self.assertEqual(Pretty(IsIn("Marcia", ["Sam", "Marcia", "Pat"])),
                         Pretty(Eternal(True)))

    # Complement

    def test_complement_1(self):
        self.assertEqual(Pretty(Complement([5, 6], [5, 6, 7])),
                         Pretty(Eternal([])))

    def test_complement_2(self):
        self.assertEqual(Pretty(Complement([5, 6, 7], [5, 6])),
                         Pretty(Eternal([7])))

    # IntersectionQ

    def test_intersectionQ_1(self):
        self.assertEqual(Pretty(IntersectionQ([5, 6], [5, 6, 7])),
                         Pretty(Eternal(True)))

    def test_intersectionQ_2(self):
        self.assertEqual(Pretty(IntersectionQ([10, 11], [5, 6, 7])),
                         Pretty(Eternal(False)))


# Used to test time series logic
tsbool1 = TS({Dawn: False, '2020-01-01': True, '2021-01-01': Null})
tsbool2 = TS({Dawn: True, '2023-01-01': False, '2024-01-01': Stub})
tsnum1 = TS({Dawn: 4, '2020-01-01': 8, '2021-01-01': Null})
tsnum2 = TS({Dawn: 24, '2023-01-01': 3, '2024-01-01': Stub})


if __name__ == '__main__':
    unittest.main()
