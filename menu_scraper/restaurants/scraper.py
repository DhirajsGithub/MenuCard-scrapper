from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import requests
from PIL import Image, UnidentifiedImageError
from io import BytesIO
import pytesseract
import re

def scrape_menu_images(restaurant_url):
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get(restaurant_url)
    
    # Find all images on the page
    menu_images = driver.find_elements(By.TAG_NAME, 'img')
    image_urls = [img.get_attribute('src') for img in menu_images if img.get_attribute('src')]
    
    # Print the URLs to ensure they are being collected correctly
    print("Image URLs:", image_urls)
    
    driver.quit()
    return image_urls

def ocr_image(image_url):
    try:
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        
        # Perform OCR
        text = pytesseract.image_to_string(img)
        
        # Print the OCR result for debugging
        print("OCR Result:", text)
    except UnidentifiedImageError:
        print(f"Error: Cannot identify image from URL {image_url}")
        return ""
    
    return text

def parse_menu_text(ocr_text):
    menu_items = []
    lines = ocr_text.split('\n')
    
    # Define combined regex pattern
    combined_pattern = r'(.+?)\s+((?:\d{1,3},)?\d{1,3}(?:\.\d{1,2})?)$'
    
    # Print each line to see the format
    print("OCR Text Lines:", lines)
    
    for line in lines:
        # Adjust regex pattern as needed
        match = re.search(combined_pattern, line)
        if match:
            item_name, price = match.groups()
            # Remove commas from price and convert to float
            price = float(price.replace(',', ''))
            menu_items.append((item_name.strip(), price))
    
    # Print parsed menu items for debugging
    print("Parsed Menu Items:", menu_items)
    
    return menu_items

