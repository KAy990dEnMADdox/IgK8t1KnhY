# 代码生成时间: 2025-10-03 18:51:49
import pandas as pd

"""
日志文件解析工具

该程序用于解析日志文件，并将其转换为Pandas DataFrame。
支持自定义行解析器和异常处理。
"""

class LogParser:
    """日志文件解析器"""

    def __init__(self, log_file_path, delimiter='
', parser=None):
        """
        :param log_file_path: 日志文件路径
        :param delimiter: 日志行分隔符，默认为换行符
        :param parser: 自定义行解析器函数，用于将每行日志转换为字典
        """
        self.log_file_path = log_file_path
        self.delimiter = delimiter
        self.parser = parser if parser else self.default_parser

    def default_parser(self, line):
        """默认行解析器
        将日志行转换为字典
        """
        # 示例：解析日志行
        # 假设日志格式为："2023-05-01 12:00:00 INFO [User] action='login'"
        # 可以根据实际日志格式自定义解析逻辑
        parts = line.split()
        date_time = parts[0] + ' ' + parts[1]
        log_level = parts[2]
        module = parts[3]
        action = parts[-1].split('=')[-1].strip("'")
        return {
            'date_time': date_time,
            'log_level': log_level,
            'module': module,
            'action': action
        }

    def parse_log_file(self):
        """解析日志文件并返回DataFrame"""
        try:
            with open(self.log_file_path, 'r') as f:
                lines = f.read().split(self.delimiter)
                data = [self.parser(line) for line in lines]
            df = pd.DataFrame(data)
            return df
        except FileNotFoundError:
            print(f"Error: 文件 {self.log_file_path} 不存在")
        except Exception as e:
            print(f"Error: 解析日志文件时发生异常 - {str(e)}")

# 示例用法
if __name__ == '__main__':
    log_file_path = 'path_to_log_file.log'
    parser = LogParser(log_file_path)
    df = parser.parse_log_file()
    print(df)