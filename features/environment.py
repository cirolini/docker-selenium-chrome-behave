from selenium import webdriver
import os

def before_all(context):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        context.browser = webdriver.Chrome(chrome_options=chrome_options)

def after_all(context):
	context.browser.quit()
