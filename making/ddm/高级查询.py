# !/user/bin/env python3
# -*- coding: utf-8 -*-
from lib.Connect import ConnectExtend, MysqlConnect
from lib.Fields import *
from making.ddm.config import DDMConf, DDMSqlGenerator


class OtherTable(ConnectExtend):
    CONNECT = MysqlConnect(DDMConf)
    GENERATOR = DDMSqlGenerator("bug_table", comment="低代码8月BUG统计-高级查询测试").fields(
        Varchar(name='t_field1', length=255,comment='Bug编号'),
        Varchar(name='t_field2', length=255, comment='所属产品'),
        Varchar(name='t_field3', length=255, comment='分支/平台'),
        Varchar(name='t_field4', length=255, comment='所属模块'),
        Varchar(name='t_field5', length=255, comment='所属项目'),
        Varchar(name='t_field6', length=255, comment='所属执行'),
        Varchar(name='t_field7', length=255, comment='相关需求'),
        Varchar(name='t_field8', length=255, comment='相关任务'),
        Varchar(name='t_field9', length=255, comment='Bug标题'),
        Varchar(name='t_field10', length=255, comment='关键词'),
        Varchar(name='t_field11', length=255, comment='严重程度'),
        Varchar(name='t_field12', length=255, comment='优先级'),
        Varchar(name='t_field13', length=255, comment='Bug类型'),
        Varchar(name='t_field14', length=255, comment='操作系统'),
        Varchar(name='t_field15', length=255, comment='浏览器'),
        Longtext(name='t_field16', comment='重现步骤'),
        Varchar(name='t_field17', length=255, comment='Bug状态'),
        Datetime(name='t_field18', comment='截止日期'),
        Varchar(name='t_field19', length=255, comment='激活次数'),
        Varchar(name='t_field20', comment='是否确认'),
        Varchar(name='t_field21', length=255, comment='抄送给'),
        Varchar(name='t_field22', length=255, comment='由谁创建'),
        Datetime(name='t_field23', comment='创建日期'),
        Varchar(name='t_field24', length=255, comment='影响版本'),
        Varchar(name='t_field25', length=255, comment='指派给'),
        Datetime(name='t_field26', comment='指派日期'),
        Varchar(name='t_field27', length=255, comment='解决者'),
        Varchar(name='t_field28', length=255, comment='解决方案'),
        Varchar(name='t_field29', length=255, comment='解决版本'),
        Datetime(name='t_field30', comment='解决日期'),
        Varchar(name='t_field31', length=255, comment='由谁关闭'),
        Datetime(name='t_field32', comment='关闭日期'),
        Varchar(name='t_field33', length=255, comment='重复Bug'),
        Varchar(name='t_field34', length=255, comment='相关Bug'),
        Varchar(name='t_field35', length=255, comment='相关用例'),
        Varchar(name='t_field36', length=255, comment='最后修改者'),
        Datetime(name='t_field37', comment='修改日期'),
    )



if __name__ == '__main__':
    ot1 = OtherTable()
    ot1.create_table()
