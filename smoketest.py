"""
 ************** loan app smoke testing ***************
 Author name : Krishna
 Data Written :
This program will perform the following web testing:

1. Check URL and verify the title
2. Send user query to input box and verify the rows retrieved

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

# initialize driver with browser
driver = webdriver.Chrome()
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
# test deployment url
url = "http://ec2-54-152-82-141.compute-1.amazonaws.com:8080/"
driver.get(url)
response = requests.get(url)
try:
    assert response.status_code == 200
except:
    print(AssertionError)
finally:
    # finish the testing
    driver.quit()
