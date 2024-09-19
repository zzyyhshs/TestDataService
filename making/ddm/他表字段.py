# !/user/bin/env python3
# -*- coding: utf-8 -*-
import random

from lib.Connect import ConnectExtend, MysqlConnect
from lib.Fields import *
from making.ddm.config import DDMConf, DDMSqlGenerator


class OtherTable(ConnectExtend):
    CONNECT = MysqlConnect(DDMConf)
    GENERATOR = DDMSqlGenerator("table0905", comment="测试表单0905").fields(
        Varchar(name='t_char1', comment='单数'),
        Varchar(name='t_char2', comment='双数'),
        Varchar(name='t_char3', comment='全部'),
        Double(name='t_int1', comment="数值1"),
        Double(name='t_int2', comment="数值2"),
        Double(name='t_int3', comment="数值3"),
        Double(name='t_int4', comment="数值4"),
        Double(name='t_int5', comment="数值5"),
        Double(name='t_int6', comment="数值6"),
    )


class OtherTable2(ConnectExtend):
    CONNECT = MysqlConnect(DDMConf)
    GENERATOR = DDMSqlGenerator("other_table0905", comment="他表表单0905").fields(
        Varchar(name='t_otherChar1', comment='他表单数'),
        Varchar(name='t_otherChar2', comment='他表双数'),
        Varchar(name='t_otherChar3', comment='他表全部'),
        Longtext(name='t_otherInt1', comment="他表数值1"),
        Longtext(name='t_otherInt2', comment="他表数值2"),
        Longtext(name='t_otherInt3', comment="他表数值3"),
        Longtext(name='t_otherInt4', comment="他表数值4"),
        Longtext(name='t_otherInt5', comment="他表数值5"),
        Longtext(name='t_otherInt6', comment="他表数值6"),
    )


if __name__ == '__main__':
    ot1 = OtherTable()
    ot2 = OtherTable2()
    # ot1.create_table()
    ot2.create_table()
