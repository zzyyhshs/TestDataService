# !/user/bin/env python3
# -*- coding: utf-8 -*-


from lib.Connect import ConnExtend
from lib.Table import TableGenerator
from lib.Fields import *


class ZDQXConfig(ConnExtend):
    # 类型转换
    GENERATOR = TableGenerator("example_table_data6").fields(Varchar(name="description1", length=255),
                                                             Varchar(name="description2", length=255),
                                                             Varchar(name="description3", length=255),
                                                             Varchar(name="description4", length=255),
                                                             Varchar(name="description5", length=255))
    create_data_sql = """INSERT INTO example_table_data6 (description1, description2, description3, description4, description5)
    VALUES (%s, %s, %s, %s, %s);"""

    def case1(self):
        data = [
            ("helloword", " 这是一条数据", "啊啊啊!@#$%^&*()_+{}[]|\:;\"\'<,>.?/~`【】{}：；“‘《，》。？/~·啊啊啊", "场景一：  系统时间为4月18， 报表时间为3月31日（只能选3,6,9,12月份）， 表示补充预测上个季度的数据， 此时 显示月末实际账期表 ，根据报表日期计算账龄得到 客户+实际 账期表，汇总金额", None),
            ("HelloWord", "  这是一条数据", "啊啊啊!@#$%^&*()_+{}[]|\:;\"\'<,>.?/~`【】{}：；“‘《，》。？/~·啊啊啊", "场景二： 系统时间为4月29日， 报表时间为3月31日（只能选3,6,9,12月份），表示补充预测上个季度的数据， 与场景一一样", None),
            ("HELLOWORD", " 这 是 一 条 数 据 ", "这是一条数据", "场景三： 系统时间为4月18日 ，报表时间为6月30日， 将 SAP3月底的SAP账龄表 作为月初账期， 新增应收为累计4月、5月、6月计划金额，计划回款为累计4月、5月、6月计划回款金额。", None),
            ("helloWord", "  这  是  一  条  数  据  ", "这是一条数据", "场景四： 系统时间为4月29日 ，报表时间为6月30日，将SAP3月底的账龄表作为月初账期，新增应收为 4月SAP实际开票金额+累计5月、6月计划金额（因为29号SAP已经开票完毕以实际开票为准），计划回款为累计4月，5月，6月计划回款金额", None),
            ("helloword!!!", "这是一条数据 ", "这是一条数据", "场景五： 系统时间为5月18日 ，报表时间为6月30日，将SAP4月底的账龄表作为月初账期，新增应收为累计5月、6月计划金额（因为29号SAP已经开票完毕以实际开票为准），计划回款为累计5月，6月计划回款金额", None),
            ("Hello你好Word", "这是一条数据  ", "这是一条数据", "场景六： 系统时间为5月29日 ，报表时间为6月30日，将SAP4月底的账龄表作为月初账期，新增应收为 5月SAP实际开票金额+6月计划金额（因为29号SAP已经开票完毕以实际开票为准），计划回款为累计 5月，6月计划回款金额", None),
            ("HelloWord你好", "      ", "这是一条数据", "场景七： 系统时间为6月18日 ，报表时间为6月30日，将SAP5月底的账龄表作为月初账期，新增应收6月计划金额 ，6月计划回款金额", None),
            ("", "", "这是一条数据   !!!", "场景八： 系统时间为6月29日 ，报表时间为6月30日，将SAP5月底的账龄表作为月初账期，新增应收6月SAP实际金额 ，6月计划回款金额", None),
            ("", "", "", "", ""),
            (None, None, None, None, None)
        ]
        self.create_data(data)


if __name__ == '__main__':
    conn = ZDQXConfig()
    conn.case1()