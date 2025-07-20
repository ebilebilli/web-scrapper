from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
options = Options()
options.binary_location = brave_path
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

start_url = "https://www.superprof.ma/cours/anglais/maroc/"
driver.get(start_url)
time.sleep(4)

# Profil linklərini toplayırıq (5 ədəd)
profile_links = []
links_elements = driver.find_elements(By.CSS_SELECTOR, "a[href$='.html']")

for link_elem in links_elements:
    href = link_elem.get_attribute("href")
    if href and href.startswith("https://www.superprof.ma") and href not in profile_links:
        if '.html' in href and '/cours/' not in href:
            profile_links.append(href)
    if len(profile_links) >= 5:
        break

def get_text(selector, index=0):
    try:
        elements = driver.find_elements(By.CSS_SELECTOR, selector)
        if elements and len(elements) > index:
            return elements[index].text.strip()
        else:
            return "Not Found"
    except:
        return "Non Found"

print("\nProfile informations:\n")

for idx, profile_url in enumerate(profile_links, 1):
    driver.get(profile_url)
    time.sleep(4)

    name = get_text("div.name > p")
    response = get_text("span.value", 1)
    price = get_text("span.value", 0)
    students = get_text("span.value.tip-trigger")
    rating = get_text("span.emphasis-size")

    try:
        availability_elem = driver.find_element(By.CSS_SELECTOR, "span.badge-picto.ttip-hv")
        availability = "Available" if availability_elem.is_displayed() else "Not Available"
    except:
        availability = "Not Found"

    lesson_place = get_text("li.webcam a")
    about_me = get_text("h1")

    print(f"Profil {idx}:")
    print(f"Name: {name}")
    print(f"Response Time: {response}")
    print(f"Price: {price}")
    print(f"Students: {students}")
    print(f"Rating: {rating}")
    print(f"Availability: {availability}")
    print(f"Lesson style: {lesson_place}")
    print(f"About Me: {about_me}")
    print("-" * 50)

driver.quit()
