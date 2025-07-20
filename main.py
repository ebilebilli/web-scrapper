import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from subjects import subjects

def scrape_profiles(count: int = 1, subject: str = 'anglais'):
    """
    Scrapes tutor profiles from superprof.ma for a given subject.

    Args:
        count (int): Number of profiles to scrape. Defaults to 1.
        subject (str): The subject to filter tutors by. Defaults to 'anglais'.

    Saves:
        A JSON file ('profiles.json') with the collected tutor information.
    """
    brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    options = Options()
    options.binary_location = brave_path
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)

    start_url = f"https://www.superprof.ma/cours/{subject}/maroc/"
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
        """
        Helper function to extract text from an element using a CSS selector.

        Args:
            selector (str): The CSS selector to locate elements.
            index (int): The index of the element in the list (default is 0).

        Returns:
            str: The extracted text or 'Not found' if not present.
        """
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

    with open("profiles.json", "a") as file:
        json.dump(results, file, indent=4)

    driver.quit()

if __name__ == "__main__":
    """
    Entry point for running the script interactively.
    Prompts the user for the number of profiles and subject, then runs scraping.
    """
    count = int(input("How many profiles do you want to scrape? "))
    subject = input(f"Please choose one of the subjects from the list:\n{chr(10).join(subjects)}\nYour choice: ")

    scrape_profiles(count)
