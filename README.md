# ShopWise

ShopWise is a Python CLI shopping assistant that helps users search products, manage favorites, track search history, monitor price changes, analyze pricing trends, compare products, and make smarter buying decisions using historical data.

---

## Current Version

### v0.7

---

## Features

### Product Search

* Search products using the DummyJSON API
* View detailed product information
* Display:

  * Title
  * Category
  * Price
  * Rating
  * Stock
  * Description

### Product Insights

* ShopWise Product Score
* Recommendation Verdict System
* Buy / Wait Recommendations

### Favorites Management

* Save products to favorites
* View favorite products
* Remove favorites

### Search History

* Automatically save searches
* View search history
* Delete search records
* Clear all search history

### Price Tracking

* Automatically store viewed product prices
* Save historical pricing data

### Price History Viewer

* View all tracked product prices
* Display date and time of each record

### Price Analytics

Analyze historical pricing data:

* Highest Price
* Lowest Price
* Average Price

### Price Trend Analysis

Analyze price movement over time:

* Increasing Trend 📈
* Decreasing Trend 📉
* Stable Trend ➖

Provides recommendations based on observed trends.

### Product Comparison

Compare two products side-by-side using:

* Price
* Rating
* Stock
* ShopWise Score

Automatically determines the winning product.

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
│   ├── history_service.py
│   └── trend_service.py
│
├── api_handler.py
├── database.py
├── main.py
├── utils.py
├── README.md
└── .gitignore
```

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
* [x] Price Trend Analysis
* [x] Analytics Service Refactor
* [x] Favorites Service Refactor
* [x] History Service Refactor

### Next 🚧

* [ ] Export Reports
* [ ] Advanced Recommendation Engine
* [ ] Improved Product Comparison

### Future 🚀

* [ ] PostgreSQL Migration
* [ ] FastAPI Backend
* [ ] Authentication System
* [ ] REST API
* [ ] Web Dashboard
* [ ] Full-Stack Web Application

---