# ShopWise

ShopWise is a Python CLI shopping assistant that helps users search products, manage favorites, track search history, monitor product prices, and analyze buying decisions using historical data.

## Features

- Search products using the DummyJSON API
- View detailed product information
- Save and manage favorite products
- Track search history
- Track product prices automatically
- View price history
- Analyze historical pricing data
- Generate ShopWise product scores
- Receive product recommendations
- Get Buy / Wait suggestions based on price trends

---

## Tech Stack

- Python
- SQLite
- Requests
- DummyJSON API
- Git & GitHub

---

## Project Structure

```text
ShopWise/
│
├── data/
│   └── shopwise.db
├── services/
│   └── analytics_service.py
├── main.py
├── database.py
├── api_handler.py
├── utils.py
├── README.md
└── .gitignore
```

---

## Current Features

### Product Search
Search products and view:

- Title
- Category
- Price
- Rating
- Stock
- Description

### Favorites
- Save products
- View favorites
- Remove favorites

### Search History
- Save searches
- View history
- Delete records
- Clear all history

### Price Tracking
- Automatically store viewed product prices
- Maintain historical price records

### Price Analytics
- Highest recorded price
- Lowest recorded price
- Average recorded price

### Product Insights
- ShopWise Score
- Recommendation Verdict
- Buy / Wait Recommendation

---

## Current Version

**v0.5**

---

## Roadmap

### Completed ✅

* [x] Product Search
* [x] Favorites System
* [x] Search History System
* [x] SQLite Integration
* [x] Product Scoring System
* [x] Recommendation Verdicts
* [x] Price Tracking
* [x] Price History Viewer
* [x] Price Analytics
* [x] Buy / Wait Recommendations
* [x] Analytics Service Refactor

### Next 🚧

* [ ] Favorite Service Refactor
* [ ] History Service Refactor
* [ ] Product Comparison System
* [ ] Price Trend Analysis

### Future 🚀

* [ ] PostgreSQL Migration
* [ ] FastAPI Backend
* [ ] Authentication System
* [ ] REST API
* [ ] Web Dashboard
* [ ] Full-Stack Application
