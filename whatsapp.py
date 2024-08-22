from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path = "D:\chromedriver\chromedriver-win64\chromedriver.exe")
print(service)
driver = webdriver.Chrome(service=service)
print("halo")
print(driver)
driver.get('https://web.whatsapp.com/')
sleep(30)
name = "Chechy"
filepath= "D:\me\AMLS6918.JPG"

user = driver.find_element("xpath",'//span[@title = "{}"]'.format(name))
user.click()

attachment_box = driver.find_element("xpath",'//div[@title = "Attach"]')
attachment_box.click()

image_box= driver.find_element("xpath",'//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
image_box.send_keys(filepath)


sleep(5)

send_button = driver.find_element("xpath",'//span[@data-icon="send"]')
send_button.click()
sleep(10)
driver.quit()