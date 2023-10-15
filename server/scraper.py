from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.common.exceptions import NoSuchElementException
def extract_text(element, by, selector):
    try:
        return element.find_element(by, selector).text
    except:
        return ""
def scrape_url(url):
    # Extract category from the URL
    category = url.split("/")[-1]

    # Set up Selenium options
    options = Options()
    # options.add_argument("--headless")  # Run in headless mode (without a visible browser window)

    # Create a WebDriver
    driver = webdriver.Chrome(options=options)

    # Navigate to the URL
    driver.get(url)
    time.sleep(2)  # Allow time for the page to load (adjust as needed)

    # Attempt to click "Load More" button twice
    for _ in range(2):
        try:
            load_more_button = driver.find_element(By.CLASS_NAME, 'QMXJlc3R5MMJjDGSV4Jd')
            load_more_button.click()
            time.sleep(2)  # Wait for the page to load (adjust as needed)
        except NoSuchElementException:
            # Handle the case when the button is not found
            break

    # Find elements using Selenium
    divtags = driver.find_elements(By.CLASS_NAME, 'TfxplVx3RtbilOD2tqd6')
    scraped_data = []
    for divtag in divtags:
        try:
            headline = extract_text(divtag, By.CLASS_NAME, 'S2DdZEgzkqC9bYeTJUGw')
            author = extract_text(divtag, By.XPATH, './/span[@itemprop="author"]')
            date = extract_text(divtag, By.XPATH, './/span[@itemprop="datePublished"]')
            description = extract_text(divtag, By.XPATH, './/span[@itemprop="description"]')
            image_meta = divtag.find_element(By.CSS_SELECTOR, 'span[itemprop="image"] meta')
            image_url = image_meta.get_attribute('content')
            article_body = extract_text(divtag, By.XPATH, './/div[@itemprop="articleBody"]')
            article_link = extract_text(divtag, By.XPATH, './/span[@itemprop="mainEntityOfPage"]')
            if(article_link != ""):
                article_link = article_link.get_attribute('itemID')

                scraped_data.append({
                    "Category": category,
                    "Headline": headline,
                    "Author": author,
                    "Date": date,
                    "Description": description,
                    "Image URL": image_url,
                    "Article Body": article_body
                })
        except NoSuchElementException:
            pass

    # Close the WebDriver
    driver.quit()

    return scraped_data
