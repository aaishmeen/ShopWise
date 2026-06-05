# ShopWise

ShopWise is a Python-based shopping assistant that helps users search for products, view product information, and maintain a history of previous searches.

The long-term goal is to evolve ShopWise from a CLI application into a full-stack web platform for product discovery, price comparison, review analysis, and smarter buying decisions.

## Features

* Search products using a product name
* Fetch product data from an external API
* Display product name, category, and price
* Save search history automatically
* View search history
* Delete individual search records
* Clear all search history
* Handle API request failures using exception handling

## Concepts Used

* Python Functions
* Lists & Dictionaries
* File Handling
* JSON Storage
* API Integration
* HTTP Requests (`requests`)
* Exception Handling
* Date & Time Handling
* CLI Development
* Git & GitHub

## Project Structure

```text
ShopWise/
│
├── main.py
├── api_handler.py
├── storage.py
├── utils.py
├── search_history.json
└── README.md
```

## Roadmap

### Completed

* [x] Product Search
* [x] API Integration
* [x] Search History Tracking
* [x] Search History Management
* [x] JSON Persistence
* [x] API Error Handling
* [x] Modular Project Structure

### Next

* [ ] Product Details View
* [ ] Product Selection Menu
* [ ] Save Favorite Products
* [ ] SQLite Integration

### Future Vision

* [ ] Price Comparison
* [ ] Price History Tracking
* [ ] Review Analysis
* [ ] Buy/Wait Recommendations
* [ ] FastAPI Backend
* [ ] Web Dashboard
* [ ] User Accounts
* [ ] Full-Stack Web Application

## Current Version

**v0.1** — Product search application with API integration, search history management, JSON persistence, and modular project architecture.
