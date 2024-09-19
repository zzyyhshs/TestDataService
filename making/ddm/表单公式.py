# !/user/bin/env python3
# -*- coding: utf-8 -*-
import random

from lib.Connect import ConnectExtend, MysqlConnect
from lib.Fields import *
from making.ddm.config import DDMConf, DDMSqlGenerator


class OtherTable(ConnectExtend):
    CONNECT = MysqlConnect(DDMConf)
    GENERATOR = DDMSqlGenerator("table0910_1", comment="表单公式0910_1").fields(
        Varchar(name='t_char3', comment='名称'),
        Double(name='t_int0', comment="数值0"),
        Double(name='t_int1', comment="数值1"),
        Double(name='t_int2', comment="数值2"),
        Double(name='t_int3', comment="数值3"),
        Double(name='t_int4', comment="数值4"),
        Double(name='t_int5', comment="加"),
        Double(name='t_int6', comment="减"),
        Double(name='t_int7', comment="乘"),
        Double(name='t_int8', comment="除"),
        Double(name='t_int9', comment="取余数"),
        Double(name='t_int10', comment="联合计算"),
    )



if __name__ == '__main__':
    ot1 = OtherTable()
    ot1.create_table()
