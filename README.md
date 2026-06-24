# AI App Compiler

## Overview

AI App Compiler converts natural language prompts into application blueprints. The system analyzes user requirements and automatically generates:

* UI Pages
* API Endpoints
* Database Tables
* Authentication Roles

## Supported Applications

* Hospital Management System
* CRM (Customer Relationship Management)
* Student Portal
* Inventory Management System
* Ecommerce Application
* Library Management System

## Features

* Intent Extraction
* Feature Detection
* Dynamic UI Generation
* API Generation
* Database Schema Generation
* Authentication Role Generation
* Schema Validation
* Auto Repair
* JSON Export

## Project Structure

* app.py
* intent.py
* design.py
* schema.py
* validator.py
* repair.py
* output.json
* test_prompts.txt

## Example Input

Build Hospital Management System with login dashboard reports notification search

## Example Output

```json
{
    "ui": {
        "pages": [
            "Login",
            "Dashboard",
            "Reports",
            "Notifications",
            "Search",
            "Book Appointment"
        ]
    }
}
```

## How to Run

### Run locally with Python
```bash
python app.py
```

### Run in Streamlit
```bash
streamlit run streamlit_app.py
```

## Streamlit Deployment
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```
3. Open `http://localhost:8501` in your browser.

## Future Enhancements

* SQL Code Generation
* Flask API Generation
* React UI Generation
* AI-Powered Requirement Analysis

## Author

Mourya Sai
