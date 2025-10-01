# 代码生成时间: 2025-10-02 02:20:30
import pandas as pd
from datetime import datetime

"""
内容管理系统
"""

class ContentManagementSystem:
    """
    内容管理系统类
    """
    def __init__(self, filename):
        """
        初始化内容管理系统
        :param filename: 存储内容的文件名
        """
        self.filename = filename
        self.data = pd.DataFrame(columns=['id', 'title', 'content', 'author', 'created_at', 'updated_at'])

    def add_content(self, content_id, title, content, author):
        """
        添加内容
        :param content_id: 内容ID
        :param title: 内容标题
        :param content: 内容
        :param author: 作者
        :return: None
        """
        try:
            new_content = {
                'id': content_id,
                'title': title,
                'content': content,
                'author': author,
                'created_at': datetime.now(),
                'updated_at': datetime.now()
            }
            self.data = pd.concat([self.data, pd.DataFrame([new_content])])
            self.save_data()
        except Exception as e:
            print(f"添加内容失败：{e}")

    def update_content(self, content_id, title, content, author):
        """
        更新内容
        :param content_id: 内容ID
        :param title: 内容标题
        :param content: 内容
        :param author: 作者
        :return: None
        """
        try:
            self.data.loc[self.data['id'] == content_id, 'title'] = title
            self.data.loc[self.data['id'] == content_id, 'content'] = content
            self.data.loc[self.data['id'] == content_id, 'author'] = author
            self.data.loc[self.data['id'] == content_id, 'updated_at'] = datetime.now()
            self.save_data()
        except Exception as e:
            print(f"更新内容失败：{e}")

    def delete_content(self, content_id):
        """
        删除内容
        :param content_id: 内容ID
        :return: None
        """
        try:
            self.data = self.data[self.data['id'] != content_id]
            self.save_data()
        except Exception as e:
            print(f"删除内容失败：{e}")

    def get_content(self, content_id):
        """
        获取内容
        :param content_id: 内容ID
        :return: 内容
        """
        try:
            content = self.data[self.data['id'] == content_id]
            return content
        except Exception as e:
            print(f"获取内容失败：{e}")
            return None

    def save_data(self):
        """
        保存内容到文件
        :return: None
        """
        try:
            self.data.to_csv(self.filename, index=False)
        except Exception as e:
            print(f"保存内容失败：{e}")

    def load_data(self):
        """
        从文件加载内容
        :return: None
        """
        try:
            self.data = pd.read_csv(self.filename)
        except Exception as e:
            print(f"加载内容失败：{e}")

if __name__ == '__main__':
    # 创建内容管理系统实例
    cms = ContentManagementSystem('content.csv')
    cms.load_data()

    # 添加内容
    cms.add_content('1', '标题1', '内容1', '作者1')
    cms.add_content('2', '标题2', '内容2', '作者2')

    # 更新内容
    cms.update_content('1', '新标题1', '新内容1', '新作者1')

    # 删除内容
    cms.delete_content('2')

    # 获取内容
    content = cms.get_content('1')
    print(content)