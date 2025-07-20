# 🕷 Superprof Profile Scraper
![Selenium Logo](https://raw.githubusercontent.com/SeleniumHQ/selenium/main/common/src/web/images/selenium_logo_square_green.png)

This Python script scrapes teacher profiles with selenium from [superprof.ma](https://www.superprof.ma) based on a subject you choose.

---

## ✅ Features

- Collects profile details: name, price, rating, availability, etc.
- Saves data to `profiles.json`
- Supports **Chrome** and **Brave** browsers (headless)

---

## ⚙ Requirements

- Python 3.x  
- Chrome or Brave browser installed  
- `pipenv` (for virtual environment)

---

## 🔧 Setup

1. **Install pipenv dependencies:**

   ```bash
   pipenv install selenium
   ```

2. **Enter the virtual environment:**

   ```bash
   pipenv shell
   ```

3. **Make sure Chrome or Brave is installed.**

   If using Brave, update this path in the code if needed:

   ```python
   brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
   ```

   To use Chrome instead, just comment out the `binary_location` line:

   ```python
   # options.binary_location = brave_path
   ```

---

## 🚀 Run the Script

```bash
python scrape_profiles.py
```

You’ll be asked:

- How many profiles to scrape
- Which subject to search (choose from the list)

Example:
```
How many profiles do you want to scrape? 5  
Please choose one of the subjects from the list:  
Your choice: anglais
```

---

## 💾 Output

The script creates/updates a file called `profiles.json` with the scraped data.

Example entry:
```json
{
  "Profile Number": 1,
  "Name": "Sarah",
  "Price": "150 DH",
  "Rating": "5.0",
  "Availability": "Available",
  ...
}
```

---

## ❗ Notes

- Runs in **headless mode** (no visible browser window)
- Add delays (`time.sleep()`) if scraping many profiles to avoid getting blocked
- If CAPTCHA or verification appears, the scraper may stop or get blocked

---

## 🔚 Exit Virtual Environment

```bash
exit
```
