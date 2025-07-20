import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def scrape_profiles(count:int = 1):
    brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    options = Options()
    options.binary_location = brave_path
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)

    start_url = "https://www.superprof.ma/cours/anglais/maroc/"
    driver.get(start_url)
    time.sleep(3)

    profile_links = []
    links_elements = driver.find_elements(By.CSS_SELECTOR, "a[href$='.html']")
    for elem in links_elements:
        href = elem.get_attribute("href")
        if href and href.startswith("https://www.superprof.ma") and href not in profile_links:
            if '.html' in href and '/cours/' not in href:
                profile_links.append(href)
        if len(profile_links) >= count:
            break

    def get_text(selector, index=0):
        try:
            elements = driver.find_elements(By.CSS_SELECTOR, selector)
            if elements and len(elements) > index:
                return elements[index].text.strip()
            return "Not found"
        except:
            return "Not found"

    results = []

    for idx, url in enumerate(profile_links, 1):
        driver.get(url)
        time.sleep(3)

        profile = {
            "Profile Number": idx,
            "Name": get_text("div.name > p"),
            "Response Time": get_text("span.value", 1),
            "Price": get_text("span.value", 0),
            "Students": get_text("span.value.tip-trigger"),
            "Rating": get_text("span.emphasis-size"),
            "Availability": "Available" if driver.find_elements(By.CSS_SELECTOR, "span.badge-picto.ttip-hv") else "Not available",
            "Lesson Place": get_text("li.webcam a"),
            "About Me": get_text("h1"),
        }

        results.append(profile)
        print(profile)
        print("-" * 40)

    with open("profiles.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    driver.quit()

if __name__ == "__main__":
    count = int(input("How many profiles do you want to scrape? "))
    scrape_profiles(count)