from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import unittest
import time





class usando_unitest(unittest.TestCase):
	driver = webdriver.Chrome(executable_path=r"C:\cchromedriver.exe")
driver.get("http://localhost:3000/login")


usuario = driver.find_element("name","User_Name")
usuario.send_keys("Jimmy Admin")
password = driver.find_element("name","Password")
password.send_keys("Unlock123")
usuario.send_keys(Keys.ENTER)
	
	
		bodega=driver.find_element_by_xpath("/html/body/form/div/div/div/div[2]/button[1]")
		bodega.test_usando_click
		time.sleep(15)

if __name__ == '__main__':
	unittest.main()