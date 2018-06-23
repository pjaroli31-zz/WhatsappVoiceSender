from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
def sender(mess):
	browser = webdriver.Firefox(executable_path='./geckodriver');
	browser.get("https://web.whatsapp.com/")
	print("Sending...............")
	wait = WebDriverWait(browser,600)
	#list of contacts u need to send put them all right here ...PUT IN ALL YOUR CONTACTS HERE
	#Python is case sensitive please type names correctly between " "
	contacts = ["Name1","Name2"]
	for contact in contacts:
		x_path = '//span[contains(@title,"'+contact+'")]'
		group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_path)))
		group_title.click()

		inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@dir="ltr"][@data-tab="1"]'
		input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
		input_box.send_keys(mess + Keys.ENTER)
		print("sent message to : " + contact) 

