from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import time

stock = input("Stock Name:")

driver = webdriver.Chrome(
    "C:\\Users\\Ian Manalo\\Desktop\\Python\\Python Course\\chromedriver\\chromedriver.exe")
driver.get("https://www.colfinancial.com/")

time.sleep(10)
username_textbox = driver.find_element_by_name("txtUser1")
username_textbox.send_keys('2017')

username1_textbox = driver.find_element_by_name("txtUser2")
username1_textbox.send_keys('4556')

password_textbox = driver.find_element_by_name("txtPassword")
password_textbox.send_keys('Soulgun21')
password_textbox.send_keys(Keys.RETURN)

time.sleep(10)

search = driver.find_element_by_xpath(
    "//body/div[2]/table/tbody/tr/td/table[2]/tbody/tr[1]/td[1]/table//tr/td[2]/font/input[@name='txtStkSymbol']")
search.send_keys('stock')
search.send_keys(Keys.RETURN)
