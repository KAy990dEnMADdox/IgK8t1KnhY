# 代码生成时间: 2025-09-18 17:16:38
import pandas as pd

"""
Excel表格自动生成器

这个程序使用Pandas库来创建和保存Excel文件。
它允许用户输入数据和文件名，然后生成一个Excel文件。
"""

def create_excel(data, file_name):
    """
    创建一个Excel文件并保存数据。

    参数:
    data (dict): 包含列名和数据的字典。
    file_name (str): 要保存的Excel文件的名称。

    返回:
    None
    """
    try:
        # 将数据转换为Pandas DataFrame
        df = pd.DataFrame(data)
        # 保存DataFrame到Excel文件
        df.to_excel(file_name, index=False)
        print(f"Excel文件 '{file_name}' 已成功创建。")
    except Exception as e:
        # 错误处理
        print(f"创建Excel文件时发生错误：{e}")

def main():
    """
    主函数，用于测试Excel生成器。
    """
    # 示例数据
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "City": ["New York", "Los Angeles", "Chicago"]
    }
    # 文件名
    file_name = "example.xlsx"
    # 创建Excel文件
    create_excel(data, file_name)

if __name__ == "__main__":
    main()