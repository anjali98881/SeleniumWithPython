from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# setUp
driver = webdriver.Chrome()
base_url = "https://creds.appwrk.com/sign-in"

driver.get(base_url)

# test data
firstName = "Rajesh"
lastName = "Panwar"
emailId = "rajeshpanwar1717@gmail.com"
password = "password"

# Step 1: SignUp
signUp = driver.find_element_by_link_text("Sign up")
signUp.click()

firstNameInput = driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div[2]/form/div[1]/div/input")
firstNameInput.send_keys(firstName)

lastNameInput = driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div[2]/form/div[2]/div/input")
lastNameInput.send_keys(lastName)

emailIdInput = driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div[2]/form/div[3]/div/input")
emailIdInput.send_keys(emailId)

passwordInput = driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div[2]/form/div[4]/div/input")
passwordInput.send_keys(password)

termsCheckbox = driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div[2]/form/div[5]/span/span[1]/input")
termsCheckbox.click()

signUpNowButton = driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div[2]/form/button")
"""
if signUpNowButton.is_enabled():
    signUpNowButton.click()
else:
    pass
"""
signUpNowButton.click()
time.sleep(3)

# Step 2: Signin

signIn = driver.find_element_by_link_text("Sign in")
signIn.click()

emailIdSignIn = driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div[2]/form/div[2]/div/input")
emailIdSignIn.send_keys(emailId)

passwordSignIn = driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div[2]/form/div[3]/div/input")
passwordSignIn.send_keys(password)

signInNowButton = driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div[2]/form/button")
signInNowButton.click()
"""
if signUpNowButton.is_enabled():
    signUpNowButton.click()
else:
    pass
"""

# Step 3: Dashboard
timeout = 3

time.sleep(timeout)

hamburgerButton = driver.find_element_by_xpath("//*[@id='root']/div/header/div/button")
if hamburgerButton.is_displayed():
    hamburgerButton.click()

userLink = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/ul/li[1]")
userLink.click()

time.sleep(timeout)

projectsLink = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/ul/li[2]/div/a")
projectsLink.click()

time.sleep(timeout)

credentialsLink = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/ul/li[3]/div/a")
credentialsLink.click()

time.sleep(timeout)

groupsLink = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/ul/li[4]/div/a")
groupsLink.click()

# TearDown
time.sleep(5)
driver.close()