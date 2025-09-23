# 代码生成时间: 2025-09-23 12:40:10
import pandas as pd
import sqlalchemy as sa
from sqlalchemy.exc import SQLAlchemyError
import logging

# 数据库迁移工具
class DatabaseMigrationTool:
    """用于从源数据库迁移数据到目标数据库的工具类。"""
    def __init__(self, source_db_url, target_db_url):
        """初始化数据库迁移工具。"""
        self.source_db_url = source_db_url
        self.target_db_url = target_db_url
        self.source_engine = sa.create_engine(self.source_db_url)
        self.target_engine = sa.create_engine(self.target_db_url)
        self.source_conn = None
        self.target_conn = None

    def connect(self):
        """建立与源数据库和目标数据库的连接。"""
        try:
            self.source_conn = self.source_engine.connect()
            self.target_conn = self.target_engine.connect()
        except SQLAlchemyError as e:
            logging.error(f"数据库连接失败：{e}")

    def disconnect(self):
        """断开与源数据库和目标数据库的连接。"""
        try:
            if self.source_conn:
                self.source_conn.close()
            if self.target_conn:
                self.target_conn.close()
        except SQLAlchemyError as e:
            logging.error(f"数据库断开连接失败：{e}")

    def migrate_table(self, table_name, source_table=None, target_table=None):
        """从源数据库迁移指定表的数据到目标数据库。"""
        if not self.source_conn or not self.target_conn:
            logging.error("数据库连接未建立，请先调用connect方法。")
            return

        source_table_name = source_table or table_name
        target_table_name = target_table or table_name

        try:
            # 从源数据库读取数据
            df = pd.read_sql_table(source_table_name, self.source_conn)
            # 将数据写入目标数据库
            df.to_sql(target_table_name, self.target_conn, if_exists='replace', index=False)
            logging.info(f"表 {table_name} 迁移成功。")
        except SQLAlchemyError as e:
            logging.error(f"表 {table_name} 迁移失败：{e}")
        except pd.errors.EmptyDataError:
            logging.warning(f"表 {table_name} 为空，跳过迁移。")

    def migrate_all_tables(self):
        """迁移源数据库的所有表到目标数据库。"""
        if not self.source_conn or not self.target_conn:
            logging.error("数据库连接未建立，请先调用connect方法。")
            return

        try:
            # 获取源数据库的所有表名
            tables = self.source_engine.table_names()
            for table_name in tables:
                self.migrate_table(table_name)
        except SQLAlchemyError as e:
            logging.error(f"获取源数据库表名失败：{e}")

# 配置数据库连接参数
source_db_url = "mysql+pymysql://user:password@host:port/source_db"
target_db_url = "mysql+pymysql://user:password@host:port/target_db"

# 创建数据库迁移工具实例
migration_tool = DatabaseMigrationTool(source_db_url, target_db_url)

# 建立数据库连接
migration_tool.connect()

# 迁移指定表
migration_tool.migrate_table("employees")

# 迁移所有表
migration_tool.migrate_all_tables()

# 断开数据库连接
migration_tool.disconnect()