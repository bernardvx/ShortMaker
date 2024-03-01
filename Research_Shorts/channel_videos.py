"""
This script takes in a channel about page and
return info about that account like:
when joined, how many videos posted, total views

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  

chrome_options = Options()
chrome_options.add_argument("--headless") 

driver = webdriver.Chrome(options=chrome_options)

url = "https://www.youtube.com/channel/UCOnK8086_CzVXcTAPgcnejQ/about"
driver.get(url)

element_id = "right-column"
element = driver.find_element(By.ID, element_id)
texts = element.text.split("\n")
joined = texts[1].split("Joined ")[1]
views = texts[2].split(" ")[0]

element_id = "videos-count"
videos_count = driver.find_element(By.ID, element_id).text.split(" ")[0]

print("Joined:", joined)
print("Total Views:", views)
print("Videos Count:", videos_count)

driver.quit()
