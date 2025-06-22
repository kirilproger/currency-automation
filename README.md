# 💱 Currency Automation Tool (Python)

A Python CLI tool that fetches currency exchange rates via public API, logs results, and optionally saves them to an Excel file.

---

## 🚀 Features

- ✅ Fetches exchange rates using open.er-api.com (no API key required)
- ✅ Command-line interface (CLI)
- ✅ Saves results to Excel
- ✅ Logs requests to `log.json`
- ✅ Ready for CI/CD

---

## 🧱 Project Structure

```
currency-automation/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── rates.xlsx
│
├── logs/
│   └── log.json
│
└── .github/
    └── workflows/
        └── python-ci.yml
```

---

## ⚙️ Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/kirilproger/currency-automation.git
cd currency-automation
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🧪 Usage

### Fetch rate and save to Excel
```bash
python main.py --currency USD --target EUR --save
```

### Fetch rate without saving
```bash
python main.py --currency BTC --target USD
```

### Show log
```bash
python main.py --log
```

---

## ✅ Example log entry
```json
{
  "timestamp": "2025-06-20 10:00:00",
  "base_currency": "USD",
  "target_currency": "EUR",
  "rate": 0.914
}
```

---

## 📦 Requirements

- Python 3.10+
- requests
- pandas
- openpyxl

---

## 🧠 License

MIT — free to use, modify, and share. ⭐
