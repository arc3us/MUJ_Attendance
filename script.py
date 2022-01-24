from time import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pytesseract
import os



chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--output=/dev/null")


driver = webdriver.Chrome(options=chrome_options) #Chrome webdriver

id = "registration_number" #replace it with your registration number
pwd = "password" #replace it with your password

id_field = '//*[@id="txtUserid"]'
pwd_field = '//*[@id="txtpassword"]'
captcha_field = '//*[@id="txtCaptcha"]'
captcha_img = '//*[@id="imgCaptcha"]'
logn_btn = '//*[@id="hprlnkStduent"]'
acad_rec = '//*[@id="reptrMainManu1_lnkbtn_3"]'

driver.get("https://dms.jaipur.manipal.edu/loginForm.aspx")

driver.find_element_by_xpath(id_field).send_keys(id)
driver.find_element_by_xpath(pwd_field).send_keys(pwd)
captcha_link = driver.find_element_by_xpath(captcha_img).get_attribute("src")

with open('captcha.jpg', 'wb') as file:
    file.write(driver.find_element_by_xpath(captcha_img).screenshot_as_png)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract' #path to Tesseract

captcha_code = pytesseract.image_to_string(r'captcha.jpg')

driver.find_element_by_xpath(captcha_field).send_keys(captcha_code.strip())

driver.find_element_by_xpath(logn_btn).click()

time.sleep(2)

driver.find_element_by_xpath(acad_rec).click()

print("Attendances are as follows: ")

for i in range(0, 10):
    j= i+2
    name = '//*[@id="ContentPlaceHolder1_grdAttendanceDetails_grdlbSubName_%d"]' %i
    att = ' //*[@id="ContentPlaceHolder1_grdAttendanceDetails"]/tbody/tr[%d]/td[10]' %j


    print(driver.find_element_by_xpath(name).get_attribute("innerHTML"), end=" ")
    print(driver.find_element_by_xpath(att).get_attribute("innerHTML"))

driver.close()
driver.quit()
os.remove("captcha.jpg")

