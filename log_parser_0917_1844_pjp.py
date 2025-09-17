# 代码生成时间: 2025-09-17 18:44:13
import pandas as pd
import re
from datetime import datetime
import sys

"""
日志文件解析工具

该工具用于解析日志文件，并提取有用信息。
支持自定义正则表达式以匹配日志中的特定模式。
"""

class LogParser:
    def __init__(self, log_file_path, pattern):
        """
        初始化LogParser类。
        
        参数:
        log_file_path (str): 日志文件路径。
        pattern (str): 用于匹配日志模式的正则表达式。
        """
        self.log_file_path = log_file_path
        self.pattern = pattern

    def parse_log(self):
        """
        解析日志文件，并返回包含提取信息的Pandas DataFrame。
        
        返回:
        pd.DataFrame: 包含提取信息的DataFrame。
        """
        try:
            # 读取日志文件内容
            with open(self.log_file_path, 'r') as file:
                logs = file.readlines()

            # 使用正则表达式匹配日志模式
            matched_logs = [re.search(self.pattern, log) for log in logs]

            # 提取匹配结果到DataFrame
            df = pd.DataFrame([match.groupdict() for match in matched_logs if match],
                            columns=['timestamp', 'level', 'message'])

            return df
        except FileNotFoundError:
            print(f"错误：文件'{self.log_file_path}'不存在。")
            sys.exit(1)
        except Exception as e:
            print(f"错误：解析日志时出现异常。{e}")
            sys.exit(1)

    def display_parsed_logs(self, df):
        """
        显示解析后的日志信息。
        
        参数:
        df (pd.DataFrame): 包含提取信息的DataFrame。
        """
        print("解析后的日志信息：")
        print(df)

# 示例用法
if __name__ == '__main__':
    # 日志文件路径
    log_file_path = 'example.log'
    
    # 自定义正则表达式（以时间戳、日志级别和消息为例）
    pattern = r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s(?P<level>\w+)\s(?P<message>.*)"
    
    # 创建LogParser实例
    log_parser = LogParser(log_file_path, pattern)
    
    # 解析日志文件
    df = log_parser.parse_log()
    
    # 显示解析后的日志信息
    log_parser.display_parsed_logs(df)