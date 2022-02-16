from selenium import webdriver
from selenium.webdriver.common.by import By
import configparser


class Test:
    driver = webdriver.Chrome('C:/Users/SOHAN/PycharmProjects/pythonProject/data_files/chromedriver.exe')
    config = configparser.RawConfigParser()
    config.read("C:/Users/SOHAN/PycharmProjects/pythonProject/Configuration/config.txt")
    urls = config.get('HOSTNAME','url')
    uns = config.get('HOSTNAME', 'un')
    pwds = config.get('HOSTNAME', 'pwd')
    driver.get(urls)
    driver.find_element_by_name('user_name').send_keys(uns)
    driver.find_element_by_name('user_password').send_keys(pwds)