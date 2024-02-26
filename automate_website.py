import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumwire import webdriver as wiredriver  # Import seleniumwire's webdriver

def extract_text_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def automate_website(file_path, website_url):
    # Use selenium-wire's webdriver instead of regular webdriver
    options = wiredriver.ChromeOptions()
    options.add_argument('--incognito')
    driver = wiredriver.Chrome(options=options)

    try:
        # Navigate to the website
        driver.get(website_url)

        # Find the text area and clear any existing text
        text_area = driver.find_element(By.CLASS_NAME, 'el-textarea__inner')  # Replace with the actual class name
        text_area.clear()

        # Extract text from the file
        file_text = extract_text_from_file(file_path)

        # Enter the extracted text into the text area
        text_area.send_keys(file_text)

        # Find and click the Submit button
        submit_button = driver.find_element(By.CLASS_NAME, 'el-button--primary')  # Replace with the actual class name
        submit_button.click()

        # Wait until the table is visible
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, 'el-table--scrollable-y')))

        # Find and click the Export button
        export_button = driver.find_element(By.CLASS_NAME, 'el-button--success')  # Replace with the actual class name
        export_button.click()

        # Wait for the download to complete using selenium-wire
        time.sleep(5)  # Add a small sleep to ensure the download has started
        request = driver.wait_for_request('C:\\AIML')  # Replace with the actual download endpoint

        # Save the downloaded file
        downloaded_file_path = 'C:\\AIML\\result.tsv'  # Replace with the actual path
        with open(downloaded_file_path, 'wb') as file:
            file.write(request.response.body)

        # Read the downloaded file and save the data to a DataFrame
        df = pd.read_csv(downloaded_file_path)

        # Perform further actions on the DataFrame if needed

    finally:
        # Close the browser
        driver.quit()

# Specify the path to your file and the website URL
file_path = input('Enter file path')  # Replace with the actual path
website_url = 'http://bioinfo.life.hust.edu.cn/AnimalTFDB4/#/TFBS_Predict'  # Replace with the actual URL

# Run the automation script
automate_website(file_path, website_url)
