# autotraderca_webscrapping
An automated web scraper for AutoTrader.ca built with Python and Selenium, featuring antibot evasion, headless execution, and dynamic data validation.

# AutoTrader.ca Automated Web Scraper

A robust and production-ready web scraping solution designed to extract vehicle data from AutoTrader.ca using Python and Selenium. This project focuses on overcoming modern web automation defenses, ensuring reliable data collection through human-like interaction patterns and dynamic page synchronization.

## 🚀 Key Features

* **Advanced Antibot Evasion:** Integrated with `undetected-chromedriver` to bypass strict perimeter security and data poisoning (preventing the site from serving false or generic results).
* **Smart Synchronization:** Implements explicit waiting conditions (`WebDriverWait`) to handle asynchronous API calls, ensuring the script waits until location data is fully validated before proceeding.
* **Headless Architecture:** Configured to run efficiently in the background (`--headless=new`) with optimal virtual viewport rendering to minimize CPU and RAM usage.
* **Human Emulation:** Mimics real user behavior through hardware-level actions (`ActionChains`), simulated keystroke delays, and session-clearing protocols.
* **Data Sanitization:** Automatically cleans and formats raw string data (e.g., converting text prices like `$ 35,488` into clean numerical integers).

## 🛠️ Tech Stack

* **Language:** Python 3.13+
* **Automation:** Selenium WebDriver & ActionChains
* **Stealth Engine:** Undetected-Chromedriver
