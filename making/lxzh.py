# !/user/bin/env python3
# -*- coding: utf-8 -*-


from lib.Connect import ConnExtendOld


class LXZHConfig(ConnExtendOld):
    # 类型转换
    table = "example_table_data5"
    create_table_sql = """
                CREATE TABLE example_table_data5 (
                id INT,
                name VARCHAR(255),
                age TINYINT,
                height FLOAT,
                weight DOUBLE,
                birthdate DATE,
                created_at TIMESTAMP,
                description TEXT,
                description1 TEXT,
                description2 TEXT,
                description3 TEXT,
                description4 VARCHAR(255)
            );"""
    create_data_sql = """INSERT INTO example_table_data5 (id, name, age, height, weight, birthdate, created_at, description, description1, description2, description3, description4)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

    def case1(self):
        data = [
            # 正常日期
            (1, '张三', 11, 223, 33.111,
             '2024-02-01', '2023-12-31 00:00:00',
             '123456789', '2023-12-31', '2023/12/31', '2023-12-31 00:00:00', 'X'),
            # 闰年
            (2, '李四', 127, 2234.1234567, 3.323456789012345,
             '2024-02-29', '2024-02-29 23:59:59',
             '123456789.123456789', '2024-02-29', '2024/02/29', '2024-02-29 23:59:59', 'Y,Z'),
            # 异常年份月日
            (3, '李四', -128, -2234.1234567, -3.323456789012345,
             '2023-02-28', '2023-02-28 12:00:00',
             '-123456789.123456789', '2023-02-28', '2023/02/28', '2023-02-28 12:00:00', 'Y,Z'),
            # 0 23年第一天 0
            (4, '王五', 0, 0, 0,
             '2023-01-01', '2023-01-01 13:45:23',
             '0', '2023-01-01', '2023/01/01', '2023-01-01 13:45:23', 'Y,Z'),
            # null 23年最后一天 null
            (5, '王五', None, None, None,
             None, None,
             None, None, None, None, None),
            (6, '王五', 33, 22.567, 323456789012345,
             '2023-01-01', '2023-01-01',
             '', '', '', '', '')]
        self.create_data(data)


if __name__ == '__main__':
    conn = LXZHConfig()
    conn.case1()