# 代码生成时间: 2025-10-09 16:29:56
import pandas as pd

"""
Inventory Management System using Python and Pandas.

This program is designed to manage inventory with features like adding,
editing, deleting, and listing inventory items. It ensures that
the code is clear, easy to understand, and follows best practices.
"""

class InventoryManager:
    def __init__(self):
        # Initialize a DataFrame to store inventory data
        self.inventory = pd.DataFrame(columns=['Item ID', 'Item Name', 'Quantity', 'Price'])

    def add_item(self, item_id, item_name, quantity, price):
        """
        Add a new item to the inventory.

        Args:
            item_id (str): Unique identifier for the item.
            item_name (str): Name of the item.
            quantity (int): Quantity of the item.
            price (float): Price of the item.

        Returns:
            bool: True if the item is added successfully, False otherwise.
        """
        # Check if the item already exists in the inventory
        if self.inventory.loc[self.inventory['Item ID'] == item_id].empty:
            self.inventory = self.inventory.append({'Item ID': item_id, 'Item Name': item_name, 'Quantity': quantity, 'Price': price}, ignore_index=True)
            return True
        else:
            print(f"Item with ID {item_id} already exists in the inventory.")
            return False

    def edit_item(self, item_id, new_item_name=None, new_quantity=None, new_price=None):
        """
        Edit an existing item in the inventory.

        Args:
            item_id (str): Unique identifier for the item.
            new_item_name (str, optional): New name for the item. Defaults to None.
            new_quantity (int, optional): New quantity for the item. Defaults to None.
            new_price (float, optional): New price for the item. Defaults to None.

        Returns:
            bool: True if the item is edited successfully, False otherwise.
        """
        # Check if the item exists in the inventory
        if not self.inventory.loc[self.inventory['Item ID'] == item_id].empty:
            # Update the item's details
            if new_item_name:
                self.inventory.loc[self.inventory['Item ID'] == item_id, 'Item Name'] = new_item_name
            if new_quantity:
                self.inventory.loc[self.inventory['Item ID'] == item_id, 'Quantity'] = new_quantity
            if new_price:
                self.inventory.loc[self.inventory['Item ID'] == item_id, 'Price'] = new_price
            return True
        else:
            print(f"Item with ID {item_id} not found in the inventory.")
            return False

    def delete_item(self, item_id):
        """
        Delete an item from the inventory.

        Args:
            item_id (str): Unique identifier for the item.

        Returns:
            bool: True if the item is deleted successfully, False otherwise.
        """
        # Check if the item exists in the inventory
        if not self.inventory.loc[self.inventory['Item ID'] == item_id].empty:
            self.inventory = self.inventory.loc[self.inventory['Item ID'] != item_id]
            return True
        else:
            print(f"Item with ID {item_id} not found in the inventory.")
            return False

    def list_items(self):
        """
        List all items in the inventory.

        Returns:
            None
        """
        print(self.inventory)

# Example usage
if __name__ == '__main__':
    manager = InventoryManager()

    # Add items
    manager.add_item('001', 'Apple', 50, 1.99)
    manager.add_item('002', 'Banana', 30, 0.99)

    # Edit an item
    manager.edit_item('001', new_quantity=60)

    # Delete an item
    manager.delete_item('002')

    # List all items
    manager.list_items()