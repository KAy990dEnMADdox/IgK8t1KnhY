# 代码生成时间: 2025-10-12 03:15:27
import pandas as pd

# 供应商管理系统
class SupplierManagement:
    def __init__(self):
        # 初始化供应商数据
        self.suppliers = pd.DataFrame(columns=['ID', 'Name', 'City', 'Country'])

    def add_supplier(self, supplier_id, name, city, country):
        """添加供应商"""
        if not all([supplier_id, name, city, country]):
            raise ValueError("所有字段都是必填的")
        
        # 检查供应商ID是否已存在
        if self.suppliers[(self.suppliers['ID'] == supplier_id)].empty == False:
            raise ValueError("供应商ID已存在")
        
        # 添加供应商到数据框架
        self.suppliers = self.suppliers.append({'ID': supplier_id, 'Name': name, 'City': city, 'Country': country}, ignore_index=True)
        print(f"供应商 {name} 已添加")

    def remove_supplier(self, supplier_id):
        """删除供应商"""
        # 检查供应商是否存在
        if self.suppliers[(self.suppliers['ID'] == supplier_id)].empty:
            raise ValueError("供应商ID不存在")
        
        # 删除供应商
        self.suppliers = self.suppliers.drop(self.suppliers[(self.suppliers['ID'] == supplier_id)].index)
        print(f"供应商ID {supplier_id} 已删除")

    def update_supplier(self, supplier_id, name=None, city=None, country=None):
        """更新供应商信息"""
        # 检查供应商是否存在
        if self.suppliers[(self.suppliers['ID'] == supplier_id)].empty:
            raise ValueError("供应商ID不存在")
        
        # 更新供应商信息
        self.suppliers.loc[self.suppliers['ID'] == supplier_id, ['Name', 'City', 'Country']] = \
            [name if name else self.suppliers.loc[self.suppliers['ID'] == supplier_id, 'Name'].values[0], \
             city if city else self.suppliers.loc[self.suppliers['ID'] == supplier_id, 'City'].values[0], \
             country if country else self.suppliers.loc[self.suppliers['ID'] == supplier_id, 'Country'].values[0]]
        print(f"供应商ID {supplier_id} 信息已更新")

    def list_suppliers(self):
        """列出所有供应商"""
        print("供应商列表：")
        print(self.suppliers)

    def find_supplier(self, supplier_id):
        """查找供应商"""
        # 检查供应商是否存在
        if self.suppliers[(self.suppliers['ID'] == supplier_id)].empty:
            raise ValueError("供应商ID不存在")
        
        # 打印供应商信息
        print(f"供应商ID {supplier_id} 信息：")
        print(self.suppliers[(self.suppliers['ID'] == supplier_id)])

# 示例用法
if __name__ == '__main__':
    sm = SupplierManagement()
    sm.add_supplier(1, '供应商A', '北京', '中国')
    sm.add_supplier(2, '供应商B', '上海', '中国')
    sm.list_suppliers()
    sm.update_supplier(1, name='供应商A1')
    sm.find_supplier(1)
    sm.remove_supplier(2)
    sm.list_suppliers()