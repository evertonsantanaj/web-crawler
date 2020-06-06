#imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driverPATH = ' ' #replace here with the path for the driver, e.g.: 'C:/PATH/chromedriver'
website = '' #replace here with the website you want to access, e.g.: 'https://www.exemple.com'
username_login = '' #replace here with login username
password_login = '' #replace here with login password 

username_field = '' #paste here the Xpath of username field "/html/body/div/cux-card/div/div[2]/div[2]/cux-card-content/form[1]/cux-input[1]/div/div/div/input"
password_field = '' #paste here the Xpath of password field
login_button = '' #paste here the Xpath of login button


driver = webdriver.Chrome(driverPATH) 

sleep(2)

driver.get('website')

sleep(10)

#user
driver.find_element_by_xpath(username_field).send_keys(username_login)

#password
driver.find_element_by_xpath(password_field).send_keys(password_login)

#entrar
driver.find_element_by_xpath(login_button).click()

###continue here with the specific actions for the website
