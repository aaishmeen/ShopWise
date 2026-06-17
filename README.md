# ShopWise

A Python-based product tracking and analysis application that integrates with the DummyJSON API and PostgreSQL to help users search products, track prices, manage favorites, analyze trends, and generate reports.

---

## Features

* Search products using the DummyJSON API
* View detailed product information
* Save products to favorites
* View and manage favorites
* Track search history with date and time
* Track product price history
* Compare products using a custom ShopWise Score
* Analyze product pricing and buying recommendations
* Analyze price trends over time
* Export favorites, search history, and price history to CSV
* Generate timestamped PDF reports
* PostgreSQL database integration
* Environment variable configuration using `.env`

---

## Technologies Used

* Python
* PostgreSQL
* Requests
* Psycopg
* Python-dotenv
* ReportLab
* Git & GitHub

---

## Project Structure

```text
ShopWise/
│
├── data/
│
├── exports/      # Generated CSV exports
├── reports/      # Generated PDF reports
│
├── services/
│   ├── analytics_service.py
│   ├── comparison_service.py
│   ├── export_service.py
│   ├── favorite_service.py
│   ├── history_service.py
│   ├── report_service.py
│   └── trend_service.py
│
├── .env
├── .env.example
├── .gitignore
├── api_handler.py
├── database.py
├── main.py
├── README.md
├── requirements.txt
└── utils.py
```

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd ShopWise
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### macOS/Linux

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
DB_HOST=localhost
DB_NAME=shopwise
DB_USER=postgres
DB_PASSWORD=your_password
```

---

## CSV Export Functionality

ShopWise can export:

* Favorites
* Search History
* Price History

Generated CSV files are stored in the:

```text
exports/
```

directory.

---

## PDF Report Generation

ShopWise can generate timestamped PDF reports containing:

* Total Favorites
* Total Searches
* Total Price Records
* Highest Recorded Price
* Lowest Recorded Price
* Average Recorded Price
* Report Generation Timestamp

Generated reports are stored in the:

```text
reports/
```

directory.

---

## Sample Report Contents

```text
SHOPWISE REPORT

Generated On: 18-Jun-2026 12:30:00

SUMMARY

Total Favorites: 10
Total Searches: 25
Total Price Records: 15

ANALYTICS SUMMARY

Highest Recorded Price: $1099.99
Lowest Recorded Price: $199.99
Average Recorded Price: $799.99
```

---

## Dependencies

```text
requests
psycopg
python-dotenv
reportlab
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## Future Improvements

* FastAPI integration
* Interactive web dashboard
* Data visualization charts
* Unit testing
* User authentication
* Email report delivery
* Scheduled report generation

---

## Author

Developed as a Python portfolio project demonstrating:

* API Integration
* PostgreSQL Database Management
* Data Analysis
* File Exporting
* PDF Report Generation
* Environment Variable Management
* Modular Software Design
* Error Handling and Validation
