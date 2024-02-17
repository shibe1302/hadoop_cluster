#Selenium helps you use this executable to automate Chrome
from multiprocessing.sharedctypes import Value
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium
import requests
import io
from datetime import datetime as dt
from PIL import Image
import time
import os
import urllib.request
import csv
file_path="download/"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
wd=webdriver.Chrome(options=options)
url1="https://www.pexels.com/vi-vn/tim-kiem/shiba/"
des="shiba inu shibe dog cho"

max_img=10

wd.get(url1)

images = wd.find_elements(By.TAG_NAME, "img")



def scroll_down(wd):
    wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
for i in range (0,3):
    scroll_down(wd)
image_urls = set()



for img in images:
    if(len(image_urls)>=max_img):
        break
    try:
        image_urls.add(img.get_attribute('src'))
    except:
        continue
wd.close()   
def xu_li_link(link_str,des):
    try:
        string1=link_str
        nameOfImg=string1.split("/")
        name_last=nameOfImg[-1].split("?")
        
        link_hd=string1.split("?")
        
        return [name_last[0],link_str,link_hd[0],des]
    except:
        print("failed process") 
def download_img(url,des):
    data=requests.get(url).content
    dataimg=xu_li_link(url,des)
    f = open("cao_anh/img_folder/"+dataimg[0],'wb') 
    f.write(data) 
    f.close()

# opening the csv file in 'a+' mode
file = open('link.csv', 'w', newline ='')
list_url=list(image_urls)
listoflist=[]
for img in list_url:
     listoflist.append(xu_li_link(img,des))
# writing the data into the file
with file: 
	write = csv.writer(file)
	write.writerows(listoflist)      
for cou,dl in enumerate(listoflist):
    try:
        download_img(dl[2],des)
        print(cou,"--tai thanh cong !")
    except:
        print("that bai")
import push_file_to_hdfs
push_file_to_hdfs.push_Toan_bo_file()
ip=push_file_to_hdfs.importdata()
ip.import_csv_to_sql()
push_file_to_hdfs.xoa_sau_khi_push()
#push_file_to_hdfs.xoa_toan_bo_file_HDFS()