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

class Test_Odev:
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
    
    #   Test 1: Kullanıcı adı ve Şifre alanları boş geçildiğinde  "Epic sadface: Username is required" uyarısı veriyor mu?
    
    def test_empty_fields(self):
        self.waitForElementVisible((By.ID,"user-name"))
        userNameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        userNameInput.send_keys("")
        passwordInput.send_keys("")
        self.waitForElementVisible((By.ID,"login-button"))
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        self.waitForElementVisible((By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3"))
        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-empty-fields.png")
        assert errorMessage.text == "Epic sadface: Username is required"
    
    #   Test 2: Sadece şifre alanı boş bırakılırsa "Epic sadface: Password is required" mesajı verecek mi?
    
    def test_empty_password(self):
        self.waitForElementVisible((By.ID,"user-name"))
        userNameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        userNameInput.send_keys("standard_user")
        passwordInput.send_keys("")
        self.waitForElementVisible((By.ID,"login-button"))
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        self.waitForElementVisible((By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3"))
        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-empty-password.png")
        assert errorMessage.text == "Epic sadface: Password is required"   

    #   Test 3: Kullanıcı adı locked_out_user şifre de secret_sauce verilince,
    #   "Epic sadface: Sorry, this user has been locked out."  mesajı veriyor mu? 

    def test_locked_out(self):
        self.waitForElementVisible((By.ID,"user-name"))
        userNameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        userNameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        self.waitForElementVisible((By.ID,"login-button"))
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        self.waitForElementVisible((By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3"))
        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-locked-out-user.png")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
    
    #   Test 4: Kullanıcı adı ve şifre boş bırakılınca ilgili kutuların yanında X işareti oluşacak mı?
    #   eğer oluşursa uyarı mesajı kapatılınca bu işaretler kaybolacak mı? 

    def test_xSign(self):
        self.waitForElementVisible((By.ID,"login-button"))
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        self.waitForElementVisible((By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(1) > svg"))
        self.waitForElementVisible((By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(2) > svg"))
        firstSign = self.driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(1) > svg")
        secondSign = self.driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(2) > svg")
        

        if firstSign.is_displayed():
            if secondSign.is_displayed():
                assert True
        else: 
            False
        

        self.driver.save_screenshot(f"{self.folderPath}/error-x-signs.png")
        self.waitForElementVisible((By.CLASS_NAME,"error-button"))
        errorButton = self.driver.find_element(By.CLASS_NAME,"error-button")
        errorButton.click()

        xSignExist = len(self.driver.find_elements(By.CLASS_NAME,"error_icon")) > 0

        if xSignExist:
            assert False
        else: 
            assert True
        
        self.driver.save_screenshot(f"{self.folderPath}/x-signs-closed.png")

    # Test 5: standard_user username'i ve secret_sauce şifresi girilince "/inventory.html" sayfasına gidecek mi?
    
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_standard_login(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        userNameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        userNameInput.send_keys(username)
        passwordInput.send_keys(password)
        self.waitForElementVisible((By.ID,"login-button"))
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        currentUrl =self.driver.current_url
        self.driver.save_screenshot(f"{self.folderPath}/test-standard-login-inventory-page.png")
        if currentUrl == "https://www.saucedemo.com/inventory.html" : 
            assert True
        else:
            assert False
    
    # Test 6: Giriş yapılınca 6 adet ürün gösteriyor mu?
    def test_six_products(self):
        self.waitForElementVisible((By.ID,"user-name"))
        userNameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        userNameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        self.waitForElementVisible((By.ID,"login-button"))
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        self.waitForElementVisible((By.CLASS_NAME,"inventory_item_name"))
        listOfProducts = self.driver.find_elements(By.CLASS_NAME,"inventory_item_name")
        self.driver.save_screenshot(f"{self.folderPath}/list-of-products.png")
        assert len(listOfProducts) == 6

    


        

        






        



