# Personal Finance Manager

class FinanceManager:
    def __init__(self):
        self.income = 0
        self.expenses = {}
        self.budget = 0

    def set_income(self, amount):
        self.income = amount

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount

    def set_budget(self, amount):
        self.budget = amount

    def display_summary(self):
        print("Income:", self.income)
        print("Expenses:")
        for category, amount in self.expenses.items():
            print(category, ":", amount)
        print("Budget:", self.budget)

    def check_budget(self):
        total_expenses = sum(self.expenses.values())
        if total_expenses > self.budget:
            print("Warning: Expenses exceed budget!")
        else:
            print("Expenses within budget.")

def main():
    finance_manager = FinanceManager()

    while True:
        print("\n1. Set income")
        print("2. Add expense")
        print("3. Set budget")
        print("4. Display summary")
        print("5. Check budget")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            income = float(input("Enter income: "))
            finance_manager.set_income(income)
        elif choice == "2":
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            finance_manager.add_expense(category, amount)
        elif choice == "3":
            budget = float(input("Enter budget: "))
            finance_manager.set_budget(budget)
        elif choice == "4":
            finance_manager.display_summary()
        elif choice == "5":
            finance_manager.check_budget()
        elif choice == "6":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()







