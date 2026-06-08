# ShopWise

ShopWise is a Python-based shopping assistant that helps users search for products, view detailed product information, save favorite products, track price history, and maintain a searchable record of previous searches.

The long-term goal is to evolve ShopWise from a CLI application into a full-stack web platform for product discovery, price tracking, review analysis, and smarter buying decisions.

---

## Features

* Search products using a product name
* Fetch product data from an external API
* View detailed product information
* Generate a ShopWise product score
* Get recommendation verdicts based on product score
* Save favorite products using SQLite
* View saved favorite products
* Delete favorite products
* Save search history automatically
* View search history
* Delete individual search records
* Clear all search history
* Track product prices automatically
* View product price history
* Handle API request failures using exception handling

---

## Concepts Used

* Python Functions
* Lists & Dictionaries
* SQLite Databases
* SQL CRUD Operations
* Database Design
* API Integration
* HTTP Requests (`requests`)
* Exception Handling
* Date & Time Handling
* Business Logic
* Recommendation Systems
* Scoring Algorithms
* CLI Development
* Modular Programming
* Git & GitHub

---

## Project Structure

```text
ShopWise/
│
├── main.py
├── api_handler.py
├── database.py
├── utils.py
├── shopwise.db
├── README.md
└── .gitignore
```

---

## Database Tables

### favorites

Stores user favorite products.

| Column   | Type    |
| -------- | ------- |
| id       | INTEGER |
| title    | TEXT    |
| category | TEXT    |
| price    | REAL    |

### search_history

Stores product searches.

| Column       | Type    |
| ------------ | ------- |
| id           | INTEGER |
| product_name | TEXT    |
| date         | TEXT    |
| time         | TEXT    |

### price_history

Stores product price records over time.

| Column       | Type    |
| ------------ | ------- |
| id           | INTEGER |
| product_name | TEXT    |
| price        | REAL    |
| date         | TEXT    |
| time         | TEXT    |

---

## Roadmap

### Completed

* [x] Product Search
* [x] API Integration
* [x] Product Details View
* [x] Product Selection Menu
* [x] Favorites System
* [x] Favorites Persistence (SQLite)
* [x] Delete Favorite Product
* [x] Search History Tracking
* [x] Search History Management
* [x] Search History Migration to SQLite
* [x] Product Scoring System
* [x] Product Recommendation Verdicts
* [x] Price History Tracking
* [x] Price History Viewer
* [x] API Error Handling
* [x] Modular Project Structure

### Next

* [ ] Price Analytics (Highest / Lowest / Average Price)
* [ ] Buy / Wait Recommendation System
* [ ] Review-Based Recommendations
* [ ] Product Comparison System

### Future Vision

* [ ] Price Comparison Engine
* [ ] Review Scraping & Analysis
* [ ] FastAPI Backend
* [ ] PostgreSQL Migration
* [ ] User Accounts
* [ ] Authentication System
* [ ] Web Dashboard
* [ ] Full-Stack Web Application

---

## Current Version

**v0.3** — SQLite-powered shopping assistant featuring product search, favorites management, search history tracking, product scoring, recommendation verdicts, and price history tracking.

---

## How to Run

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

Windows:

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install requests
```

### 5. Run the Application

```bash
python main.py
```

---

## Learning Journey

This project is being developed incrementally to learn:

* Python Fundamentals
* APIs and HTTP Requests
* SQLite and SQL
* Database Design
* Software Architecture
* Recommendation Systems
* Backend Development with FastAPI
* PostgreSQL
* Full-Stack Development
