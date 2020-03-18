#from selenium import webdriver
#driver= webdriver.Chrome()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r'C:\Users\Prasad\AppData\Local\Programs\Python\Python38\chromedriver.exe')
#browser = webdriver.Firefox()
#browser.get('http://inventwithpython.com')
driver.get("http://localhost:5000/application.html")
name=driver.find_element_by_name("name")
email=driver.find_element_by_name("email")
age=driver.find_element_by_name("age")
gender=driver.find_element_by_name("gender")
married=driver.find_element_by_name("married")
dependents=driver.find_element_by_name("dependents")
education=driver.find_element_by_name("education")
appincome=driver.find_element_by_name("appincome")
coappincome=driver.find_element_by_name("coappincome")
loan_amount=driver.find_element_by_name("loan_amount")
loan_term=driver.find_element_by_name("loan_term")
credit_history=driver.find_element_by_name("credit_history")
area=driver.find_element_by_name("area")
employment=driver.find_element_by_name("employment")

name.send_keys('prasad')
email.send_keys('veginatiprasad@gmail.com')
age.send_keys('26')
gender.send_keys('1')
married.send_keys('1')
dependents.send_keys('0')
education.send_keys('1')
appincome.send_keys('0')
coappincome.send_keys('0')
loan_amount.get_attribute('value')
loan_term.send_keys('0')
credit_history.send_keys('0')
area.send_keys('2')
employment.send_keys('1')
#driver.find_element_by_name("submit").click()
form = driver.find_element_by_id('submit')
form.submit()

driver.close()
driver.quit()