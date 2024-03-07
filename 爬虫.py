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

base_url = "https://sex-positions.online/zh-cn/page/{}/"
url_list = [base_url.format(i) for i in range(1, 12)]  # 生成1到100的URL列表

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",  # Chrome
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",  # Firefox
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582",  # Edge
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",  # IE
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1"  # Mobile Safari
]
# random_user_agent = random.choice(user_agents)
# headers = {'User-Agent': random_user_agent}

file_path = 'E:/python/sex-positions.html'

def get_html_content(file_path, url_list):
    # 创建一个新的Chrome浏览器实例
    driver = webdriver.Chrome()
    for url in url_list:
        print(url)
        try:
            # 访问网页
            driver.get(url)
            # 获取所有的cookie
            cookies = driver.get_cookies()
            time.sleep(60)
            # 打印所有的cookie
            # for cookie in cookies:
            #     print(cookie)
            cookies_dict = {c['name']: c['value'] for c in cookies}
            # 获取包含内容的元素
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'page-template-default')))
            # 获取元素的HTML内容
            content = element.get_attribute('innerHTML')
            print(content)
            write_file(file_path, content)
    
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while making the request: {e}")


def write_file(file_path, content):
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(content + '\n')  # Append a new line after each response


def read_sex_positions(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        if not os.path.exists(file_path):
            open(file_path, 'w').close()
        html_content = file.read()
    # Parse the HTML content
    html_tree = etree.HTML(html_content)
    # Extract all div elements with class="position_listing"
    title=html_tree.xpath('//h2[@class="title_2"]/a/text()')
    detail_link=html_tree.xpath('//a[@class="btn btn_empty btn_lg"]/@href')
    move_link = html_tree.xpath('//a[@class="btn btn_empty btn_lg"]/@href')
    div_elements = html_tree.xpath('//div[@class="position_listing"]')
    i=0
    # for element in div_elements:
    #     i=i+1
    #     element_str = etree.tostring(element, encoding='utf-8').decode('utf-8')
    #     write_file('E:/python/aticel.txt', element_str)
    #     print(i)

    # for element in title:
    #     i=i+1
    #     element_str = str(element)
    #     write_file('E:/python/title.txt', element_str)
    #     print(i)
    for element in detail_link:
        i=i+1
        element_str = str(element)
        write_file('E:/python/detail_link.txt', element_str)
        print(i)
    # for element in move_link:
    #     i=i+1
    #     element_str = str(element)
    #     write_file('E:/python/move_link.txt', element_str)
    #     print(i)


    




    # Get the content of each div element
    # div_content = [etree.tostring(div_element, encoding='unicode') for div_element in div_elements]

    # Print the content of each div element
    # for content in div_content:
    #     print(content)

# get_html_content(file_path, url_list,driver)

read_sex_positions(file_path)