import requests
import random
import os
from lxml import etree
from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

move_link='E:\python\move_link.txt'
title_path="E:/python/title.txt"

def read_name_into_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines


def write_file(file_path, content):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(content + '\n')  # Append a new line after each response

def read_file_into_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines







# for link,name in zip(links,names):
#     print(link)
#     print(name)
#     print('\n')
url_list=read_file_into_list(move_link)
names=read_name_into_list(title_path)

# def get_html_content( url_list,names):
#     # 创建一个新的Chrome浏览器实例
#     driver = webdriver.Chrome()
#     for url,name in zip(url_list,names):
#         print(url)
#         print(name)
#         try:
#             file_path='E:/python/detail/'+name+'.html'
#             # 访问网页
#             driver.get(url)
#             # 获取所有的cookie
#             # cookies = driver.get_cookies()
#             time.sleep(60)
#             # 打印所有的cookie
#             # for cookie in cookies:
#             #     print(cookie)
#             # cookies_dict = {c['name']: c['value'] for c in cookies}
#             # 获取包含内容的元素
#             element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'wr')))
#             # 获取元素的HTML内容
#             content = element.get_attribute('innerHTML')
#             print(content)
#             write_file(file_path, content)
    
#         except requests.exceptions.RequestException as e:
#             print(f"An error occurred while making the request: {e}")

driver = webdriver.Chrome()
driver.get('https://sex-positions.online/zh-cn/position/po-sobachi/')
time.sleep(80)
element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'position_listing')))
content = element.get_attribute('innerHTML')
print(content)
# get_html_content(url_list,names)