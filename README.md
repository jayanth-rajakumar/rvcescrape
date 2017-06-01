# rvcescrape
Python tool to scrape exam results of RV College of Engineering

This uses the Selenium WebDriver to enter the USN, solve the (rather poorly implemented) captcha and get the name & SGPA of the candidates within the selected USN range. Tested on Python 2.7.13 only.

Setup:
1. Install selenium using 'pip install selenium' (Windows might have to do 'cd C:/Python27/Scripts' first)
2. Download chromedriver.exe from https://sites.google.com/a/chromium.org/chromedriver/ and place it in C:/Python27

Usage:
1. Open rvcescrape.py in Python editor.
1. Replace USN_start, USN_end, and USN_yr_dept as required
2. Run the program.
