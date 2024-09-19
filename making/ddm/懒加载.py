# !/user/bin/env python3
# -*- coding: utf-8 -*-



import random

from lib.Connect import ConnectExtend, MysqlConnect
from lib.FakeData import *
from lib.Fields import *
from making.ddm.config import DDMConf, DDMSqlGenerator


class LJZTable(ConnectExtend):
    CONNECT = MysqlConnect(DDMConf)
    GENERATOR = DDMSqlGenerator("ljz_table0918", comment="懒加载表单0918").fields(
        Varchar(name='t_char1', comment='类型1'),
        Varchar(name='t_char2', comment='类型2'),
        Varchar(name='t_char3', comment='类型3'),
        Double(name='t_int1', comment="数值1"),
        Double(name='t_int2', comment="数值2"),
        Double(name='t_int3', comment="数值3"),
        Double(name='t_int4', comment="数值4"),
        Double(name='t_int5', comment="数值5"),
        Double(name='t_int6', comment="数值6"),
    )

    def case1(self):
        data = list()
        data_count = 500
        for i in range(data_count):
            son_data = list()
            if self.GENERATOR.pk is not None:
                son_data.append(i)
            for j in range(len(self.GENERATOR) - 1):
                if isinstance(self.GENERATOR[j], Datetime):
                    son_data.append(fake_date())
                elif isinstance(self.GENERATOR[j], Varchar):
                    son_data.append("%s_%s_%s" % (self.GENERATOR[j].comment, i, j))
                elif isinstance(self.GENERATOR[j], Double):
                    son_data.append(fake_float(0, 1000))
            data.append(son_data)
        self.create_data(data)


if __name__ == '__main__':
    t = LJZTable()
    t.case1()






