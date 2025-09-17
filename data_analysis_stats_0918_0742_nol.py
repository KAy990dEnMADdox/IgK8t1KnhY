# 代码生成时间: 2025-09-18 07:42:10
import pandas as pd

"""
数据统计分析器

该程序使用PANDAS框架，用于加载数据集，并对数据进行统计分析。
"""


def load_data(filepath):
    """加载数据集
    
    参数:
    filepath (str): 数据文件路径
    
    返回:
    DataFrame: 包含数据的Pandas DataFrame对象
    """
    try:
        # 尝试读取CSV文件
        data = pd.read_csv(filepath)
        return data
    except Exception as e:
        # 如果读取文件时出现错误，打印错误信息
        print(f"Error loading data: {e}")
        return None


def calculate_statistics(data):
    """计算统计数据
    
    参数:
    data (DataFrame): 包含数据的Pandas DataFrame对象
    
    返回:
    dict: 包含统计数据的字典
    """
    if data is None:
        return None
    try:
        # 计算描述性统计数据
        stats = {
            "mean": data.mean(),
            "median": data.median(),
            "max": data.max(),
            "min": data.min(),
            "std": data.std(),
            "var": data.var()
        }
        return stats
    except Exception as e:
        print(f"Error calculating statistics: {e}")
        return None


def display_statistics(stats):
    "