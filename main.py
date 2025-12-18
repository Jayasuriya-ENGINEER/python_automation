from selenium import webdriver                          
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

#importing the webdriver manager to automatically manage driver binaries
#importing the servce to magnage what to do
#importing the common by to locate elements, that is the components of the webpage


#due the loading reasons, we need to use webdriverwait, and EC

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sercice = Service(path='chromedriver.exe')  #this is what i installed and paste in windows folder of my system
driver = webdriver.Chrome(service=sercice)  #initializing the driver with the service

driver.get('https://www.amazon.in/')  #navigating to the url
input_box = driver.find_element(By.ID, 'twotabsearchtextbox')  #locating the search box using ID
input_box.send_keys('headphones'+ Keys.ENTER)

wait=WebDriverWait(driver,40)

wait.until(EC.presence_of_element_located((By.ID,'twotabsearchtextbox')))



driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)

#for first product order use XPATH 
# Click first product
first_product = wait.until(
    EC.presence_of_element_located((
        By.XPATH,
        "//a[contains(@href,'/dp/') and contains(@class,'a-link-normal')]"
    ))
)
driver.execute_script("arguments[0].click();", first_product)

# Switch tab ONLY if needed
if len(driver.window_handles) > 1:
    driver.switch_to.window(driver.window_handles[1])


#after that, the windows moves to next page, and there we find the add to cart button using ID

driver.switch_to.window(driver.window_handles[1])  #switching to the new tab

#adding the procdut to the cart

add_cart=wait.until(EC.element_to_be_clickable((By.ID,'add-to-cart-button')))
add_cart.click()

proced_to_buy=wait.until(EC.element_to_be_clickable((By.ID,'sc-buy-box-ptc-button')))
proced_to_buy.click()

#login page
example_gmail= wait.until(EC.presence_of_element_located((By.ID,'ap_email_login')))
example_gmail.send_keys("jayasuriyas900@gmail.com"+ Keys.ENTER)

time.sleep(2)
example_password= wait.until(EC.presence_of_element_located((By.ID,'ap_password')))
example_password.send_keys("$uriya@21"+ Keys.ENTER)


print("Enter OTP manually in browser...")
input("After entering OTP, press ENTER here to continue...")



#time.sleep(20)

