# !/user/bin/env python3
# -*- coding: utf-8 -*-
from lib.Connect import ConnExtendOld


class QCConfig(ConnExtendOld):
    # 数据去重
    table = "example_table_data3"
    create_table_sql = """
                CREATE TABLE example_table_data3 (
                id INT,
                name VARCHAR(255),
                age TINYINT,
                height FLOAT,
                weight DOUBLE,
                birthdate DATE,
                created_at TIMESTAMP,
                is_active BOOLEAN,
                description TEXT,
                binary_data BINARY(10),
                enum_field ENUM('A', 'B', 'C'),
                set_field SET('X', 'Y', 'Z')
            );"""
    create_data_sql = """INSERT INTO example_table_data3 (id, name, age, height, weight, birthdate, created_at, is_active, description, binary_data, enum_field, set_field)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

    def case1(self):
        data = [
            (1, '张三', 11, 12.11, 13.111, '1991-02-02', '1991-02-02', False, 'zs', '0987654321', 'A', 'X'),
            (2, '李四', 11, 12.11, 13.111, '1991-03-02', '1991-02-02', False, 'ls', '0987654321', 'B', 'Y,Z'),
            (3, '李四', 21, 22.11, 23.111, '1991-03-02', '1991-02-02', False, 'LS', '0987654321', 'C', 'Y,Z'),
            (4, '王五', 11, 12.11, 13.111, '1991-04-02', '1991-02-02', False, 'ww', '0987654321', 'A', 'Y,Z'),
            (5, '王五', 21, 22.11, 23.111, '1991-04-02', '1991-02-02', False, 'wW', '0987654321', 'B', 'Y,Z'),
            (6, '王五', 31, 32.11, 33.111, '1993-04-02', '1991-02-02', True, 'Ww', '0987654321', 'C', 'Y,Z')]
        self.create_data(data)


if __name__ == '__main__':
    conn = QCConfig()
    conn.case1()


