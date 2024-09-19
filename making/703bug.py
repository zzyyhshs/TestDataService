# !/user/bin/env python3
# -*- coding: utf-8 -*-


from lib.Connect import ConnExtend
from lib.Fields import *
from lib.Table import SqlGenerator


class LXZHConfig(ConnExtend):
    table = "example_table_test_data"
    # 类型转换
    create_table_sql = SqlGenerator("example_table_test_data").fields(Varchar(name="f1"),
                                                                        Varchar(name="f2"),
                                                                        Double(name="f3"),
                                                                        Double(name="f4"))()

# .primary_key("f1")



if __name__ == '__main__':
    conn = LXZHConfig()
    conn.create_table()