import json
import datetime
import csv

FILE = "data.json"


# =========================
# DATA HANDLING
# =========================

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


# =========================
# TRANSACTIONS
# =========================

def add_transaction(data):
    t_type = input("Type (income/expense): ").lower()
    amount = float(input("Amount: "))
    category = input("Category: ")

    transaction = {
        "type": t_type,
        "amount": amount,
        "category": category,
        "date": str(datetime.date.today())
    }

    data.append(transaction)
    save_data(data)
    print("Transaction added!")


# =========================
# SUMMARY
# =========================

def show_summary(data):
    income = sum(t["amount"] for t in data if t["type"] == "income")
    expense = sum(t["amount"] for t in data if t["type"] == "expense")

    print("\n📊 SUMMARY")
    print(f"Total Income: {income}")
    print(f"Total Expenses: {expense}")
    print(f"Balance: {income - expense}")


# =========================
# CSV EXPORT
# =========================

def export_csv(data):
    with open("report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Type", "Amount", "Category", "Date"])

        for t in data:
            writer.writerow([t["type"], t["amount"], t["category"], t["date"]])

    print("CSV exported as report.csv")


# =========================
# RESET DATA
# =========================

def reset_data():
    confirm = input("Are you sure you want to delete all data? (yes/no): ").lower()

    if confirm == "yes":
        with open(FILE, "w") as f:
            f.write("[]")
        print("All data has been reset.")
    else:
        print("Reset cancelled.")


# =========================
# MENU
# =========================

def menu():
    data = load_data()

    while True:
        print("\n=== EXPENSE TRACKER ===")
        print("1. Add transaction")
        print("2. Show summary")
        print("3. Export CSV")
        print("4. Reset All Data")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_transaction(data)

        elif choice == "2":
            show_summary(data)

        elif choice == "3":
            export_csv(data)

        elif choice == "4":
            reset_data()
            data = load_data()

        elif choice == "5":
             break

        else:
            print("Invalid option")


# =========================
# RUN PROGRAM
# =========================

if __name__ == "__main__":
    menu()