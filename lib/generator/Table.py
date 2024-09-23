# !/user/bin/env python3
# -*- coding: utf-8 -*-
from lib.generator.Fields import BaseField


class SqlFmtForMysql:
    # 校验数据库表是否存在
    is_exist = "SELECT COUNT(*) FROM information_schema.tables WHERE table_name = '%s'"
    # 清空数据库表
    truncate = "TRUNCATE TABLE %s;"


class SqlGenerator:
    def __init__(self, name, engine="InnoDB", charset="utf8mb4", collate="utf8mb4_general_ci", comment=""):
        self.name = name
        self.engine = engine
        self.charset = charset
        self.collate = collate
        self.comment = comment
        self._fields = []
        self._pk_field = None
        self._space_char = " "

    def fields(self, *args):
        for field in args:
            try:
                self.append(field)
            except Exception as e:
                raise Exception("第%s个字段类型非法或不支持" % (args.index(field) + 1))
        return self

    def append(self, field: BaseField):
        if not isinstance(field, BaseField):
            raise Exception("字段类型非法或不支持")
        self._fields.append(field)

    def primary_key(self, pk_field):
        if not isinstance(pk_field, BaseField):
            raise Exception("主键字段非法或不支持")
        self._pk_field = pk_field
        return self

    def _create_sql(self):
        start_sql = f"CREATE TABLE `{self.name}`"
        end_sql = f"ENGINE={self.engine} DEFAULT CHARSET={self.charset} COLLATE={self.collate} COMMENT='{self.comment}';"
        fields_sql = ",".join([f() for f in self._fields])
        if self._pk_field is None:
            return f"{start_sql} ({fields_sql}) {end_sql}"
        else:
            return f"{start_sql} ({self._pk_field()}, {fields_sql}, PRIMARY KEY ('{self._pk_field.name}')) {end_sql}"

    def _insert_sql(self):
        _sql = f"INSERT INTO {self.name}"
        if self._pk_field is None:
            _fields = ','.join([f.name for f in self._fields])
            _fmt = ','.join(['%s' for f in self._fields])
            _field_str = f"({_fields}) VALUES({_fmt});"
            return _sql + self._space_char + _field_str
        else:
            _fields = self._pk_field.name + ',' + ','.join([f.name for f in self._fields])
            _fmt = ','.join(['%s' for f in range(len(self._fields) + 1)])
            _field_str = f"({_fields}) VALUES({_fmt});"
            return _sql + self._space_char + _field_str

    def _truncate_sql(self):
        return SqlFmtForMysql.truncate % self.name

    def _is_exist_sql(self):
        return SqlFmtForMysql.is_exist % self.name

    def _delete_sql(self):
        return

    @property
    def create(self):
        return self._create_sql()

    @property
    def insert(self):
        return self._insert_sql()

    @property
    def truncate(self):
        return self._truncate_sql()

    @property
    def is_exist(self):
        return self._is_exist_sql()

    @property
    def pk(self):
        return self._pk_field

    def __getitem__(self, item: int):
        return self._fields[item]

    def __call__(self):
        return self.create

    def __len__(self):
        if self._pk_field is not None:
            return len(self._fields) + 1
        return len(self._fields)


if __name__ == '__main__':
    from lib.generator.Fields import *
    t = SqlGenerator("example_table_test_data").fields(Varchar(name="f1"),
                                                       Varchar(name="f2"),
                                                       Double(name="f3"),
                                                       Double(name="f4"))
    print(t.insert)
    print(t.is_exist)
    print(t.create)
    print(t.truncate)
    print(len(t))