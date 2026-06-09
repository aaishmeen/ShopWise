# ShopWise

A Python CLI shopping assistant that helps users search products, manage favorites, track price history, analyze pricing trends, and receive product recommendations.

Built as a learning project to master:

- Python
- APIs & HTTP Requests
- SQLite
- Database Design
- Software Architecture
- Recommendation Systems
- Backend Development

---

# Features

## Product Search
- Search products by name
- Fetch real-time product data from DummyJSON API
- View detailed product information

## Product Insights
- ShopWise Score (/10)
- Product Recommendation Verdict
- Rating & Stock Analysis

## Favorites Management
- Save favorite products
- View saved favorites
- Delete favorite products

## Search History
- Automatically save searches
- View search history
- Delete individual search records
- Clear all search history

## Price Tracking
- Automatically record product prices
- Store historical price data
- View complete price history

## Price Analytics
- Highest recorded price
- Lowest recorded price
- Average recorded price

## Reliability
- API error handling
- Input validation
- SQLite data persistence

---

# Technologies Used

- Python 3
- SQLite3
- Requests Library
- DummyJSON API
- Git & GitHub

---

# Project Structure

```text
ShopWise/
│
├── main.py
├── database.py
├── api_handler.py
├── utils.py
├── shopwise.db
├── README.md
├── .gitignore
│
└── .venv/
```

---

# Database Design

## favorites

Stores user favorite products.

| Column | Type |
|----------|----------|
| id | INTEGER |
| title | TEXT |
| category | TEXT |
| price | REAL |

---

## search_history

Stores search activity.

| Column | Type |
|----------|----------|
| id | INTEGER |
| product_name | TEXT |
| date | TEXT |
| time | TEXT |

---

## price_history

Stores product price records.

| Column | Type |
|----------|----------|
| id | INTEGER |
| product_name | TEXT |
| price | REAL |
| date | TEXT |
| time | TEXT |

---


# ShopWise Score System

Products are evaluated using:

- Rating
- Stock Availability

### Verdict Rules

| Score | Verdict |
|---------|---------|
| 8+ | Excellent Choice |
| 6+ | Recommended |
| 4+ | Average |
| Below 4 | Not Recommended |

---

# Roadmap

## Completed ✅

- [x] Product Search
- [x] Product Details View
- [x] API Integration
- [x] Favorites System
- [x] Favorites Persistence (SQLite)
- [x] Delete Favorite Product
- [x] Search History Tracking
- [x] Search History Persistence (SQLite)
- [x] Delete Search History
- [x] Clear Search History
- [x] ShopWise Product Score
- [x] Recommendation Verdict System
- [x] Price Tracking
- [x] Price History Viewer
- [x] Price Analytics
- [x] API Error Handling
- [x] Modular Architecture

## In Progress 🚧

- [ ] Buy / Wait Recommendation System

## Planned 📌

- [ ] Product Comparison System
- [ ] Review-Based Recommendations
- [ ] Price Trend Analysis
- [ ] Export Reports

## Future Vision 🚀

- [ ] FastAPI Backend
- [ ] PostgreSQL Migration
- [ ] Authentication System
- [ ] User Accounts
- [ ] Web Dashboard
- [ ] Full-Stack Web Application

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd ShopWise
```

## Create Virtual Environment

```bash
python -m venv .venv
```

# Current Version

## v0.4

Features Included:

- Product Search
- Favorites Management
- Search History Management
- Product Scoring
- Recommendation Verdicts
- Price Tracking
- Price History Viewer
- Price Analytics

---

# Learning Journey

ShopWise is being built incrementally to practice real-world software development.

Progression:

Python Fundamentals
→ APIs & HTTP
→ SQLite
→ Analytics
→ Recommendation Systems
→ FastAPI
→ PostgreSQL
→ Full-Stack Development