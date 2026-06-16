# ShopWise

A Python-powered CLI shopping assistant that helps users search products, compare alternatives, track prices, manage favorites, and make data-driven purchasing decisions using PostgreSQL-backed historical analysis.

---

## Overview

ShopWise was built to explore real-world software engineering concepts including:

* API Integration
* PostgreSQL Database Management
* Modular Software Architecture
* Data Analysis
* User Input Validation
* Environment-Based Configuration

The application fetches live product data, stores user activity, tracks price history, and provides analytical insights to support smarter buying decisions.

---

## Features

### Product Discovery

* Search products using the DummyJSON API
* View detailed product information
* Browse ratings, stock levels, pricing, and descriptions

### Product Evaluation

* ShopWise Scoring System
* Recommendation Verdict Engine
* Product Comparison Tool

### Data Persistence

* Save favorite products
* Store search history
* Track product prices over time

### Analytics

* Price History Viewer
* Price Trend Analysis
* Highest, Lowest, and Average Price Analysis
* Buy/Wait Recommendations

---

## Tech Stack

| Category        | Technology    |
| --------------- | ------------- |
| Language        | Python        |
| Database        | PostgreSQL    |
| API             | DummyJSON     |
| Database Driver | Psycopg       |
| HTTP Requests   | Requests      |
| Configuration   | Python Dotenv |
| Version Control | Git & GitHub  |

---

## Project Structure

```text
ShopWise/
│
├── services/
│   ├── analytics_service.py
│   ├── comparison_service.py
│   ├── export_service.py
│   ├── favorite_service.py
│   ├── history_service.py
│   └── trend_service.py
│
├── exports/
│
├── api_handler.py
├── database.py
├── main.py
├── utils.py
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd ShopWise
```

### Create and Activate a Virtual Environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
DB_HOST=localhost
DB_NAME=shopwise
DB_USER=postgres
DB_PASSWORD=your_password
```

### Run the Application

```bash
python main.py
```

---

## Skills Demonstrated

* Object-Oriented and Modular Python Development
* REST API Consumption
* PostgreSQL Integration
* SQL Query Design
* Environment Variable Management
* Data Processing and Analytics
* CLI Application Development
* Error Handling and Input Validation
* Version Control with Git

---

## Roadmap

### Completed

* Product Search
* Product Details Viewer
* Favorites Management
* Search History Management
* PostgreSQL Integration
* Price Tracking
* Price Analytics
* Trend Analysis
* Product Comparison Engine
* Recommendation System
* CSV Export Functionality

### Planned

* Advanced Recommendation Engine
* FastAPI Backend
* REST API
* Authentication System
* Web Dashboard

---

## Why This Project?

ShopWise was developed as a hands-on project to strengthen backend development skills by combining APIs, databases, analytics, and software architecture into a practical real-world application.
