# 💰 Personal Expense Tracker

A Python command-line application designed to help users track income and expenses, manage financial records, and generate reports for analysis.

---

## 🚀 Features

* Add income and expense transactions
* Categorize financial records
* Automatically save data using JSON
* View a financial summary
* Export transaction history to CSV
* Reset all stored data with confirmation
* Simple and user-friendly command-line interface

---

## 📊 Financial Summary

The application calculates:

* Total Income
* Total Expenses
* Current Balance

This allows users to quickly understand their financial situation.

---

## 📁 Data Storage

All transactions are stored locally in a JSON file.

Example transaction:

```json
{
    "type": "expense",
    "amount": 25.50,
    "category": "food",
    "date": "2026-06-13"
}
```

---

## 📄 CSV Export

The application can generate a CSV report containing:

| Type    | Amount | Category | Date       |
| ------- | ------ | -------- | ---------- |
| income  | 1000   | salary   | 2026-06-13 |
| expense | 150    | food     | 2026-06-13 |

This report can be opened in Microsoft Excel, Google Sheets, or other spreadsheet applications.

---

## 🛠 Technologies Used

* Python 3
* JSON
* CSV
* Datetime

---

## ▶️ How to Run

Navigate to the project folder and run:

```bash
python Tracker.py
```

---

## 📂 Project Structure

```text
expense-tracker/
│
├── Tracker.py
├── data.json
├── report.csv
└── README.md
```

---

## 🎯 Learning Objectives

This project demonstrates:

* File handling
* Data persistence
* CRUD-style operations
* Financial data management
* Python programming fundamentals
* Command-line application development

---

## 👨‍💻 Author

**Moisés Alcázares**

* Systems Engineer
* Bilingual (Spanish / English)
* Python Developer
* Building a professional software development portfolio
