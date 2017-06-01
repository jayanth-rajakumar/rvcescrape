#=================================================
#RVCE Results Scraper
#https://github.com/jayanth-rajakumar/rvcescrape
#=================================================

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

USN_start=100
USN_end=120
USN_yr_dept="15EC"

usn="1RV" + USN_yr_dept + "{0:03}"

driver = webdriver.Chrome('C:/python27/chromedriver.exe')

for i in range (USN_start,USN_end+1):
    try:
        driver.get("http://results.rvce.edu.in/")

        elem = driver.find_element_by_name("usn")
        elem.send_keys(usn.format(i))

        elem = driver.find_element_by_name("captcha")
        src= driver.page_source
        index=src.find("What is ")
        ans=  int(src[index+8])+int(src[index+12])
        elem.send_keys(str(ans))
        elem.send_keys(Keys.RETURN)

        res_src= driver.page_source
        res_index=res_src.find("\"SGPA\"><b>")
        sgpa= res_src[res_index+10:res_index+14]

        name=driver.find_element_by_css_selector('td[data-title=\"NAME\"]').text

        print usn.format(i),"\t",sgpa,"\t",name
        driver.back
    except:
        pass

driver.close()

