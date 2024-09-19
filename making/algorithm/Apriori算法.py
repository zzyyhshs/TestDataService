# !/user/bin/env python3
# -*- coding: utf-8 -*-
import random

from lib import *
from making.algorithm.config import AlgorithmConf


class Apriori(ConnectExtend):
    CONNECT = MysqlConnect(AlgorithmConf)
    GENERATOR = SqlGenerator("Apriori0906").fields(
        Varchar(name="field1", length=255),
        Varchar(name="field2", length=255),
        Varchar(name="field3", length=255),
        Varchar(name="field4", length=255),
        Varchar(name="field5", length=255),
    )

    def case1(self):
        row_data = list()
        int_data = [i for i in range(len(self.GENERATOR))]
        str_data = ['field%s' % i for i in range(len(self.GENERATOR))]
        none_data = [None for i in range(len(self.GENERATOR))]
        bool_data = [True if i % 2 == 1 else False for i in range(len(self.GENERATOR))]
        sum_data = [1, 1.11, "asdsd", None, True]

        row_data.append([str(int_data), str(str_data), str(none_data), str(bool_data), str(sum_data)])
        row_data.append([str(int_data), str(str_data), str(none_data), str(bool_data), str(sum_data)])
        row_data.append([str(int_data), str(str_data), str(none_data), str(bool_data), str(sum_data)])
        row_data.append([str(int_data), str(str_data), str(none_data), str(bool_data), str(sum_data)])
        self.create_data(row_data)


if __name__ == '__main__':
    t = Apriori()
    t.case1()
