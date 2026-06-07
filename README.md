# ShopWise

ShopWise is a Python-based shopping assistant that helps users search for products, view detailed product information, save favorite products, and maintain a history of previous searches.

The long-term goal is to evolve ShopWise from a CLI application into a full-stack web platform for product discovery, price comparison, review analysis, and smarter buying decisions.

## Features

* Search products using a product name
* Fetch product data from an external API
* View detailed product information
* Save favorite products using SQLite
* View saved favorite products
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
* SQLite Databases
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
├── database.py
├── utils.py
├── shopwise.db
├── README.md
└── .gitignore
```

## Roadmap

### Completed

* [x] Product Search
* [x] API Integration
* [x] Product Details View
* [x] Product Selection Menu
* [x] Search History Tracking
* [x] Search History Management
* [x] JSON Persistence
* [x] API Error Handling
* [x] Modular Project Structure
* [x] SQLite Integration
* [x] Favorites System
* [x] Favorites Persistence
* [x] Delete Favorite Product
* [x] Search History Migration to SQLite

### Next

* [ ] Product Rating Analysis
* [ ] Review-Based Recommendations

### Future Vision

* [ ] Price Comparison
* [ ] Price History Tracking
* [ ] Review Scraping & Analysis
* [ ] Buy/Wait Recommendations
* [ ] FastAPI Backend
* [ ] PostgreSQL Migration
* [ ] User Accounts
* [ ] Web Dashboard
* [ ] Full-Stack Web Application

## Current Version

**v0.2** — Product search application with API integration, SQLite-powered favorites system, search history management, and modular project architecture.
