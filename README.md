# Restaurant Menu Scraper

## Introduction

Restaurant Menu Scraper is a web application that allows users to scrape menu images from restaurant websites, extract item names and prices using Optical Character Recognition (OCR), and store the data in a database.

## Assumptions

### Web Scraping Assumptions:

- Use of Selenium with Geckodriver: Selenium is suitable for complex scraping tasks and sites requiring JavaScript rendering.
- Target Website: We assume the target restaurant websites are accessible and do not have anti-scraping measures.

### Backend Framework Assumptions:

- Django: Chosen for its robustness and ease of integrating with various databases and third-party services.

### Database Assumptions:

- The application uses Django's default SQLite database to store restaurant and menu item data. You can access the database using Django's admin interface or by running Django management commands.


### OCR Assumptions:

- Tesseract: An open-source OCR engine that is reliable and easy to integrate with Python.

## Features

- Scrapes menu images from restaurant websites using selenium and geckodriver.
- Uses OCR to extract item names and prices from menu images.
- Stores extracted data in a database.
- Provides a user-friendly interface for viewing restaurant menus and their prices.

## Prerequisites

Before running the application, ensure you have the following prerequisites installed:

- Python 3.x
- Django
- Tesseract OCR

## Setup

Follow these steps to set up the application locally:

1. Clone the repository:

   ```bash
   git clone https://github.com/DhirajsGithub/MenuCard-scrapper.git
   ```

2. Navigate to the project directory:

   ```bash
   cd MenuCard-scrapper
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Install Tesseract OCR:

   - On Ubuntu:

     ```bash
     sudo apt-get install tesseract-ocr
     ```

   - On macOS:

     ```bash
     brew install tesseract
     ```

5. Run database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser.

## Usage

1. Navigate to the home page to view a list of restaurants.
2. Click on a restaurant to view its menu and prices.
3. To add a new restaurant, fill out the form on the home page with the restaurant name, location, and image URL, and click "Scrape This Restaurant".
