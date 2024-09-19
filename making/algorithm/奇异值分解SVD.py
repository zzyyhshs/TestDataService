# !/user/bin/env python3
# -*- coding: utf-8 -*-
import random

from lib.Connect import ConnectExtend, MysqlConnect
from lib.Table import SqlGenerator
from lib.Fields import *
from making.algorithm.config import AlgorithmConf


class SVDConfig(ConnectExtend):
    CONNECT = MysqlConnect(AlgorithmConf)
    GENERATOR = SqlGenerator("qyzfj_svd").fields(Double(name='field1'),
                                                 Double(name='field2'),
                                                 Double(name='field3'),
                                                 Double(name='field4'),
                                                 Double(name='field5'),
                                                 Double(name='field6')
                                                 )

    def case1(self):
        data = [(1, 2, 3, 4, 5, 6),
                (-1, -2, -3, -4, -5, -6),
                (1.22, 2.99, 0.00, 4.55, 5.55, 6.66),
                (-1.22, -2.99, -0.00, -4.55, -1, -9),
                (0, 0, -0.00, -4.55, -1, -9),
                (-1.22, -2.99, -0.00, -4.55, -1, -9),
                ]
        self.create_data(data)


class SVDConfig100(ConnectExtend):
    CONNECT = MysqlConnect(AlgorithmConf)
    GENERATOR = SqlGenerator("qyzfj_svd100").fields(*[Double(name='field%s' % i) for i in range(100)])

    def case1(self):
        data = list()
        for i in range(100):
            son_data = list()
            for i in range(100):
                son_data.append(random.randint(-10000, 10000))
            data.append(son_data)
        self.create_data(data)


class SVDConfig50(ConnectExtend):
    CONNECT = MysqlConnect(AlgorithmConf)
    GENERATOR = SqlGenerator("qyzfj_svd50").fields(*[Double(name='field%s' % i) for i in range(50)])

    def case1(self):
        data = list()
        for i in range(50):
            son_data = list()
            for i in range(50):
                son_data.append(random.randint(-10000, 10000))
            data.append(son_data)
        self.create_data(data)


class SVDConfig75(ConnectExtend):
    CONNECT = MysqlConnect(AlgorithmConf)
    GENERATOR = SqlGenerator("qyzfj_svd75").fields(*[Double(name='field%s' % i) for i in range(75)])

    def case1(self):
        data = list()
        for i in range(75):
            son_data = list()
            for i in range(75):
                son_data.append(random.randint(-10000, 10000))
            data.append(son_data)
        self.create_data(data)



class SVDConfig60(ConnectExtend):
    CONNECT = MysqlConnect(AlgorithmConf)
    GENERATOR = SqlGenerator("qyzfj_svd60").fields(*[Double(name='field%s' % i) for i in range(60)])

    def case1(self):
        data = list()
        for i in range(60):
            son_data = list()
            for i in range(60):
                son_data.append(random.randint(-10000, 10000))
            data.append(son_data)
        self.create_data(data)



class SVDConfig70(ConnectExtend):
    CONNECT = MysqlConnect(AlgorithmConf)
    GENERATOR = SqlGenerator("qyzfj_svd70").fields(*[Double(name='field%s' % i) for i in range(70)])

    def case1(self):
        data = list()
        for i in range(70):
            son_data = list()
            for i in range(70):
                son_data.append(random.randint(-10000, 10000))
            data.append(son_data)
        self.create_data(data)


class SVDConfig65(ConnectExtend):
    CONNECT = MysqlConnect(AlgorithmConf)
    GENERATOR = SqlGenerator("qyzfj_svd65").fields(*[Double(name='field%s' % i) for i in range(65)])

    def case1(self):
        data = list()
        for i in range(65):
            son_data = list()
            for i in range(65):
                son_data.append(random.randint(-10000, 10000))
            data.append(son_data)
        self.create_data(data)



if __name__ == '__main__':
    c = SVDConfig65()
    c.case1()

