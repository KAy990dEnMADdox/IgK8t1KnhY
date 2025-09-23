# 代码生成时间: 2025-09-24 04:33:08
import pandas as pd
import json
"""
JSON数据格式转换器
本程序用于将JSON数据转换为Pandas DataFrame，并支持将DataFrame转换回JSON格式。
"""

def json_to_dataframe(json_data):
    """
    将JSON数据转换为Pandas DataFrame。

    参数:
    json_data (str): JSON格式的字符串数据。

    返回:
    pd.DataFrame: 包含JSON数据的DataFrame。

    异常:
    ValueError: 如果JSON数据格式不正确。
    """
    try:
        data = json.loads(json_data)
        return pd.DataFrame(data)
    except json.JSONDecodeError as e:
        raise ValueError("Invalid JSON data: {}".format(e))

def dataframe_to_json(df, orient='records'):
    """
    将Pandas DataFrame转换为JSON格式。

    参数:
    df (pd.DataFrame): 待转换的DataFrame。
    orient (str): JSON的输出格式，可选值包括：'records'、'index'、'columns'、'values'、'table'等，默认为'records'。

    返回:
    str: JSON格式的字符串。
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
    return df.to_json(orient=orient)
def main():
    # 示例JSON数据
    json_data = '"""
    {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    """'

    # 将JSON数据转换为DataFrame
    try:
        df = json_to_dataframe(json_data)
        print("DataFrame: ")
        print(df)
    except ValueError as e:
        print(e)

    # 将DataFrame转换回JSON格式
    try:
        json_output = dataframe_to_json(df)
        print("
JSON Output: ")
        print(json_output)
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    main()