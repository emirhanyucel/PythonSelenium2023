from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path 
from datetime import date

class Test_3testsMore:
    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
    
    # her testten önce çağırılır
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
        # günün tarihini al bu tarih ile bir klasör var mı kontrol et yoksa oluştur
    # her testten sonra çağırılır    
    def teardown_method(self):
        self.driver.quit()
    # Test 1 ürünlerin fiyatını düşükten yükseğe sıralıyor mu?
    def test_low_to_high(self):
        self.waitForElementVisible((By.ID,"user-name"))
        userNameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        userNameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        self.waitForElementVisible((By.ID,"login-button"))
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        self.waitForElementVisible((By.CLASS_NAME,"product_sort_container"))
        itemSortContainer = self.driver.find_element(By.CLASS_NAME,"product_sort_container")
        itemSortContainer.click()
        self.waitForElementVisible((By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/span/select/option[3]"))
        lowToHighOption = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/span/select/option[3]")
        lowToHighOption.click()
        self.waitForElementVisible((By.CLASS_NAME,"inventory_item_price"))
        items = self.driver.find_elements(By.CLASS_NAME,"inventory_item_price")
        self.driver.save_screenshot(f"{self.folderPath}/sort-items-low-to-high.png")
        assert items[0].text < items[1].text
    # Test 2: Bir ürün satın alınınca satın alım başarılı oldu diye mesaj veriyor mu?
    def test_succesful_purchase(self):
        self.waitForElementVisible((By.ID,"user-name"))
        userNameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        userNameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        self.waitForElementVisible((By.ID,"login-button"))
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        self.waitForElementVisible((By.CLASS_NAME,"btn_inventory"))
        buyItemButton = self.driver.find_element(By.CLASS_NAME,"btn_inventory")
        buyItemButton.click()
        self.waitForElementVisible((By.CLASS_NAME,"shopping_cart_link"))
        goToCart = self.driver.find_element(By.CLASS_NAME,"shopping_cart_link")
        goToCart.click()
        self.waitForElementVisible((By.CLASS_NAME,"checkout_button"))
        checkOutBtn = self.driver.find_element(By.CLASS_NAME,"checkout_button")
        checkOutBtn.click()
        self.waitForElementVisible((By.ID,"first-name"))
        self.waitForElementVisible((By.ID,"last-name"))
        self.waitForElementVisible((By.ID,"postal-code"))
        
        firstName = self.driver.find_element(By.ID,"first-name")
        lastName = self.driver.find_element(By.ID,"last-name")
        postalCode = self.driver.find_element(By.ID,"postal-code")

        firstName.send_keys("MyName")
        lastName.send_keys("MyLastName")
        postalCode.send_keys("99999")

        self.waitForElementVisible((By.CLASS_NAME,"submit-button"))
        submitButton = self.driver.find_element(By.CLASS_NAME,"submit-button")
        submitButton.click()

        self.waitForElementVisible((By.ID,"finish"))
        finishButton = self.driver.find_element(By.ID,"finish")
        finishButton.click()
        self.waitForElementVisible((By.XPATH,"/html/body/div/div/div/div[2]/img"))
        self.driver.save_screenshot(f"{self.folderPath}/succesful-purchase-logo.png")
        succesfulSign = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/img")
        assert succesfulSign.is_displayed()
    # Test 3 : Sayfanın en altındaki twitter butonuna tıklayınca sitenin twitter sayfasına yönlendiriyor mu?
    def test_twitter_button(self):
        self.waitForElementVisible((By.ID,"user-name"))
        userNameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        userNameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        self.waitForElementVisible((By.ID,"login-button"))
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        self.waitForElementVisible((By.CLASS_NAME,"social_twitter"))
        twitterBtn = self.driver.find_element(By.CLASS_NAME,"social_twitter")
        twitterBtn.click()

        self.driver.switch_to.window(self.driver.window_handles[1])
        currentUrl = self.driver.current_url

        self.driver.save_screenshot(f"{self.folderPath}/twitter-page.png")
        assert currentUrl == "https://twitter.com/saucelabs"
        

    

      

        





   
      
