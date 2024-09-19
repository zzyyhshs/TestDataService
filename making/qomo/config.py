# !/user/bin/env python3
# -*- coding: utf-8 -*-
from lib import *


class QomoConf:
    host = "192.168.50.9"
    port = 2212
    user = "zzzz"
    password = "knphm2021"
    database = "demo"
    charset = 'utf8'


class QomoSqlGenerator(SqlGenerator):
    def __init__(self, name, *args, **kwargs):
        name = "test_qomo_%s" % name
        super(QomoSqlGenerator, self).__init__(name, *args, **kwargs)
        self.primary_key(PrimaryKey(name="id", comment="主键"))
        # self.fields(
        #     Varchar(name="create_by", length=50, comment="创建人"),
        #     Datetime(name="create_time", comment="创建日期"),
        #     Varchar(name="update_by", length=50, comment="更新人"),
        #     Datetime(name="update_time", comment="更新日期"),
        #     Varchar(name="sys_org_code", length=64, comment="所属部门")
        # )
