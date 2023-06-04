from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#Utsav Mandal

# Set up the Chrome driver
ser = Service('chromedriver.exe')  # Path to chromedriver executable
driver = webdriver.Chrome(service=ser)

lc_page='https://leetcode.com/problemset/all/?page='

a_tags = driver.find_elements(By.TAG_NAME, 'a')

# Extract the href attribute from each <a> tag

def get_p_list(url):
    driver.get(url)
    time.sleep(5)
    P_link=driver.find_elements(By.TAG_NAME, 'a')
    links=[]
    for i in P_link:
        try:
            #try because of premium questions causes error
            if '/problem' in i.get_attribute("href"):
                links.append(i.get_attribute("href"))
        except:
            pass
    links=list(set(links))
    return links

lists=[]

for i in range(1,56):
    lists+=get_p_list(lc_page+str(i))

lists=list(set(lists))

#For testing purpose

# print(len(lists))
# for i in lists:
#     print(i,"\n")

# Open the file in write mode
with open('output_lc.txt', 'w') as file:
    for item in lists:
        # Write each element to a new line in the file
        file.write(str(item) + '\n')

# Clean up and close the browser
driver.quit()