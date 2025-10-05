# 代码生成时间: 2025-10-05 19:57:37
import pandas as pd

"""
Firewall Rules Manager

A simple program to manage firewall rules using Python and Pandas.
"""

# Define a class to manage firewall rules
class FirewallRulesManager:
    def __init__(self):
        # Initialize with an empty DataFrame
        self.rules = pd.DataFrame(columns=['RuleID', 'Protocol', 'SourceIP', 'DestinationIP', 'Port', 'Action'])

    def add_rule(self, rule_id, protocol, source_ip, destination_ip, port, action):
        """Add a new firewall rule."""
        new_rule = pd.DataFrame([
            {'RuleID': rule_id, 'Protocol': protocol, 'SourceIP': source_ip,
             'DestinationIP': destination_ip, 'Port': port, 'Action': action}
        ])
        # Append the new rule to the existing rules
        self.rules = pd.concat([self.rules, new_rule], ignore_index=True)

    def remove_rule(self, rule_id):
        """Remove a firewall rule by its ID."""
        self.rules = self.rules[self.rules['RuleID'] != rule_id]

    def list_rules(self):
        """List all firewall rules."""
        return self.rules

    def find_rule(self, rule_id):
        """Find a firewall rule by its ID."""
        rule = self.rules[self.rules['RuleID'] == rule_id]
        if rule.empty:
            raise ValueError(f"Rule with ID {rule_id} not found.")
        return rule

    def save_rules_to_csv(self, file_path):
        """Save firewall rules to a CSV file."""
        try:
            self.rules.to_csv(file_path, index=False)
        except Exception as e:
            print(f"Error saving rules to CSV: {e}")

    def load_rules_from_csv(self, file_path):
        """Load firewall rules from a CSV file."""
        try:
            self.rules = pd.read_csv(file_path)
        except Exception as e:
            print(f"Error loading rules from CSV: {e}")

# Example usage of FirewallRulesManager
if __name__ == '__main__':
    manager = FirewallRulesManager()
    manager.add_rule('001', 'TCP', '192.168.1.1', '10.0.0.1', 80, 'ALLOW')
    manager.add_rule('002', 'UDP', '192.168.1.2', '10.0.0.2', 53, 'BLOCK')
    print(manager.list_rules())
    try:
        rule = manager.find_rule('001')
        print("Rule found:
", rule)
    except ValueError as e:
        print(e)
    manager.save_rules_to_csv('firewall_rules.csv')
    # Reload rules from CSV
    manager.load_rules_from_csv('firewall_rules.csv')
    print(manager.list_rules())
