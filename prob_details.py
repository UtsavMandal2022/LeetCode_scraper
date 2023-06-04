#Utsav Mandal
import os
from selenium import webdriver  
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

ser = Service('chromedriver.exe')  # Path to chromedriver executable
driver = webdriver.Chrome(service=ser)

heading=".mr-2.text-label-1"
body=".px-5.pt-4"

folder_path=os.path.join(os.getcwd(),"Qdata")
if not os.path.exists(folder_path):
    os.makedirs(folder_path)


def getfileContent(arr):
    with open('output_filtered.txt', 'r') as f:
        for line in f:
            arr.append(line)
    return arr

def save_body_q(text,ind):
    f_path=os.path.join(folder_path,"q"+str(ind))
    if not os.path.exists(f_path):
        os.makedirs(f_path)
    with open(f_path+"/"+str(ind)+".txt", 'w') as file:
        file.write(text)

arr=[]
getfileContent(arr)
print(len(arr))

hds=[]
qind=[]
for i in range(0,len(arr)):
    try:
        driver.get(arr[i])
        time.sleep(5)
        P_head=driver.find_elements(By.CSS_SELECTOR,heading)
        P_body=driver.find_elements(By.CSS_SELECTOR,body)
        save_body_q(P_body[0].get_attribute("textContent"),i+1)
        # print(P_head[0].get_attribute("textContent"))
        hds.append(P_head[0].get_attribute("textContent"))
        qind.append(arr[i])
    except:
        pass

print(len(hds))
print(len(qind))

with open(folder_path+'/output_headings.txt', 'w') as file:
    for item in hds:
        file.write(str(item) + '\n')


with open(folder_path+'/q_index.txt', 'w') as file:
    for item in qind:
        file.write(str(item))

driver.quit()