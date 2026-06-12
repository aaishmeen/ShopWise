# ShopWise

ShopWise is a Python CLI shopping assistant that helps users search products, manage favorites, track search history, monitor product prices, analyze pricing trends, and compare products to make smarter buying decisions.

---

## Features

### Product Search

* Search products using the DummyJSON API
* View detailed product information
* Display product rating, stock, category, price, and description

### Product Insights

* ShopWise Product Score
* Product Recommendation Verdicts
* Buy / Wait Recommendations

### Favorites Management

* Save products to favorites
* View saved favorites
* Remove favorite products

### Search History

* Automatically save searches
* View search history
* Delete individual search records
* Clear all search history

### Price Tracking

* Automatically track viewed product prices
* Store historical price data in SQLite

### Price Analytics

* Highest recorded price
* Lowest recorded price
* Average recorded price
* Buy / Wait recommendation based on historical pricing

### Product Comparison

Compare two products side-by-side using:

* Price
* Rating
* Stock
* ShopWise Score

The system automatically selects a winner based on the calculated score.

---

## Tech Stack

* Python
* SQLite
* Requests
* DummyJSON API
* Git
* GitHub

---

## Project Structure

```text
ShopWise/
│
├── data/
│   └── shopwise.db
│
├── services/
│   ├── analytics_service.py
│   ├── comparison_service.py
│   ├── favorite_service.py
│   └── history_service.py
│
├── api_handler.py
├── database.py
├── main.py
├── utils.py
├── README.md
└── .gitignore
```

---

## Current Version

### v0.6

---

## Roadmap

### Completed ✅

* [x] Product Search
* [x] Product Details View
* [x] Favorites System
* [x] Search History System
* [x] SQLite Integration
* [x] Product Scoring System
* [x] Recommendation Verdict System
* [x] Price Tracking
* [x] Price History Viewer
* [x] Price Analytics
* [x] Buy / Wait Recommendations
* [x] Product Comparison System
* [x] Analytics Service Refactor
* [x] Favorites Service Refactor
* [x] History Service Refactor

### Next 🚧

* [ ] Price Trend Analysis
* [ ] Export Reports
* [ ] Advanced Recommendation Engine

### Future 🚀

* [ ] PostgreSQL Migration
* [ ] FastAPI Backend
* [ ] Authentication System
* [ ] REST API
* [ ] Web Dashboard
* [ ] Full-Stack Application

---
