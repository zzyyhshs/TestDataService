# !/user/bin/env python3
# -*- coding: utf-8 -*-

from lib.Connect import ConnectExtend, MysqlConnect
from lib.Fields import *
from making.qomo.config import QomoConf, QomoSqlGenerator


class ZLRH2Config(ConnectExtend):
    """
    全量+增量
    """
    CONNECT = MysqlConnect(QomoConf)
    GENERATOR = QomoSqlGenerator("zlrh_all_0912", comment="增量入湖全量入湖测试表").fields(
                                                Varchar(name='field1', comment='年龄'),
                                                Varchar(name='field2', comment='姓名'),
                                                Varchar(name='field3', comment='性别'),
                                                Varchar(name='field4', comment='编号'),
                                                Varchar(name='field5', comment='身高'),
                                                Varchar(name='field6', comment='体重'),
                                                Datetime(name="create_time", comment='创建时间'),
                                                # Datetime(name="update_time", comment='更新时间')
                                                 )

    def case1(self):
        data = list()
        data.append(["1", "18", "张三", "男", "100001", "170", "70", '2022-01-01 00:00:00'])
        data.append(["2", "18", "李四", "男", "100002", "170", "70", '2022-01-01 00:00:00'])
        data.append(["3", "18", "王五", "男", "100003", "170", "70", '2022-01-01 00:00:00'])
        data.append(["4", "18", "赵六", "男", "100004", "170", "70", '2022-01-01 00:00:00'])
        data.append(["5", "18", "孙七", "男", "100005", "170", "70", '2022-01-01 00:00:00'])
        data.append(["6", "18", "刘八", "男", "100006", "170", "70", '2022-01-01 00:00:00'])
        data.append(["7", "18", "增量刘八", "男", "100007", "170", "70", '2024-09-09 00:00:00'])
        data.append(["8", "18", "增量刘八", "男", "100008", "170", "70", '2024-09-10 00:00:00'])
        data.append(["9", "18", "增量刘八", "男", "100009", "170", "70", '2024-09-10 00:00:00'])
        data.append(["10", "18", "增量刘八", "男", "100010", "170", "70", '2024-09-11 00:00:00'])
        data.append(["11", "18", "增量刘八", "男", "100011", "170", "70", '2024-09-11 00:00:00'])
        self.create_data(data)


class ZLRH3Config(ConnectExtend):
    """
    全量+增量
    """
    CONNECT = MysqlConnect(QomoConf)
    GENERATOR = QomoSqlGenerator("zlrh_all_0912_2", comment="增量入湖全量入湖测试表_2").fields(
                                                Varchar(name='field1', comment='年龄'),
                                                Varchar(name='field2', comment='姓名'),
                                                Varchar(name='field3', comment='性别'),
                                                Varchar(name='field4', comment='编号'),
                                                Varchar(name='field5', comment='身高'),
                                                Varchar(name='field6', comment='体重'),
                                                Datetime(name="create_time", comment='创建时间'),
                                                # Datetime(name="update_time", comment='更新时间')
                                                 )

    def case1(self):
        data = list()
        data.append(["1", "18", "张三", "男", "000001", "170", "70", '2022-01-01 00:00:00'])
        data.append(["2", "18", "李四", "男", "000002", "170", "70", '2022-01-01 00:00:00'])
        data.append(["3", "18", "王五", "男", "000003", "170", "70", '2022-01-01 00:00:00'])
        data.append(["4", "18", "赵六", "男", "000004", "170", "70", '2022-01-01 00:00:00'])
        data.append(["5", "18", "孙七", "男", "000005", "170", "70", '2022-01-01 00:00:00'])
        data.append(["6", "18", "刘八", "男", "000006", "170", "70", '2022-01-01 00:00:00'])
        data.append(["7", "18", "增量刘八", "男", "000007", "170", "70", '2024-09-09 00:00:00'])
        data.append(["8", "18", "增量刘八", "男", "000008", "170", "70", '2024-09-10 00:00:00'])
        data.append(["9", "18", "增量刘八", "男", "000009", "170", "70", '2024-09-10 00:00:00'])
        data.append(["10", "18", "增量刘八", "男", "000010", "170", "70", '2024-09-11 00:00:00'])
        data.append(["11", "18", "增量刘八", "男", "000011", "170", "70", '2024-09-11 00:00:00'])
        self.create_data(data)



if __name__ == '__main__':
    z2 = ZLRH3Config()
    z2.case1()
