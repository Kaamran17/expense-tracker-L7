class Expense:
    def __init__(self, name, amount, category, month, group=''):
        self.name = name
        self.amount = amount
        self.category = category
        self.month = month
        self.group = group
    def __repr__(self):
        return f"{self.name} - {self.amount} - {self.category} - {self.month} - {self.group}"
