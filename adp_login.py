#!/usr/bin/python
import argparse
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

class ADPLogin():
  def execute_login(self, adp_user, adp_pass, headless):
    options = Options()
    options.headless = headless
    self.driver = webdriver.Firefox(options=options)
    self.driver.get("https://hcm.it.adp.com/login/?TARGET=-SM-https%3a%2f%2fhcm%2eit%2eadp%2ecom%2fportal--main%2fportal%2f")
    try:
      login = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, "login")))
    finally:
      self.driver.find_element(By.ID, "login").send_keys(adp_user)
      self.driver.find_element(By.ID, "login-pw").send_keys(adp_pass)
      self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
      try:
        logout = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".fa-chevron-down"))).click()
      finally:
        self.driver.find_element_by_xpath("//span[@id='revit_form_Button_0']").click()
    time.sleep(0.5)
    self.driver.close()
  
def main():
    parser = argparse.ArgumentParser(description='ADP Login')
    parser.add_argument('--username', dest='ADP_USERNAME', required=True, help='ADP login username')
    parser.add_argument('--password', dest='ADP_PASSWORD', required=True, help='ADP login password')
    parser.add_argument('--headless', dest='HEADLESS', default=False, type=bool, help='Boolean to run browser in headless mode')
    args = parser.parse_args()
    adp_login = ADPLogin()
    adp_login.execute_login(args.ADP_USERNAME, args.ADP_PASSWORD, args.HEADLESS)

if __name__== "__main__":
  main()

