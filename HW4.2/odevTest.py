from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Testler:
    #   Test 1: Kullanıcı adı ve Şifre alanları boş geçildiğinde  "Epic sadface: Username is required" uyarısı veriyor mu?

    def test1(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        userNameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(5)
        userNameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(3)
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(10)
        errorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        test1Result = errorMessage.text == "Epic sadface: Username is required"
        print(f" 'Epic sadface: Username is required' mesajını verdi mi: {test1Result} ")
        sleep(10)
    
    
    #   Test 2: Sadece şifre alanı boş bırakılırsa "Epic sadface: Password is required" mesajı verecek mi?
    def test2(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        userNameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(5)
        userNameInput.send_keys("standard_user")
        passwordInput.send_keys("")
        sleep(3)
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(10)
        errorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        test2Result = errorMessage.text == "Epic sadface: Password is required"
        print(f" 'Epic sadface: Password is required' mesajını verdi mi: {test2Result} ")
    
    #   Test 3: Kullanıcı adı locked_out_user şifre de secret_sauce verilince "Epic sadface: Sorry, this user has been locked out." 
    #   mesajı veriyor mu?
    def test3(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        userNameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(5)
        userNameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        sleep(3)
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(10)
        errorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        test3Result = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f" 'Epic sadface: Sorry, this user has been locked out.' mesajı veriyor mu: {test3Result}")
    
    #   Test 4: Kullanıcı adı ve şifre boş bırakılınca ilgili kutuların yanında X işareti oluşacak mı?
    #   eğer oluşursa uyarı mesajı kapatılınca bu işaretler kaybolacak mı? 
    def test4(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(10)
        usernameWarningSign = driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(1) > svg")
        passwordWarningSign = driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(2) > svg")
        print(f"Username girilmeyince 'x' işareti çıkıyor mu: {usernameWarningSign.is_displayed()}")
        print(f"Password girilmeyince 'x' işareti çıkıyor mu: {passwordWarningSign.is_displayed()}")
        sleep(10)
        errorButton = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        errorButton.click()
        sleep(10)
        try:
            print(f"Test Başarısız.Uyarı mesajı kapatılmasına rağmen 'x' işaretleri hala görünüyor mu: {usernameWarningSign.is_displayed()} ")
        except:
            print(f"Test başarılı, uyarı mesajı kapatıldı 'x' işaretleri kayboldu.") 
    
    # Test 5: standard_user username'i ve secret_sauce şifresi girilince "/inventory.html" sayfasına gidecek mi?
    def test5(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        userNameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(5)
        userNameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(3)
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(10)
        
        currentUrl = driver.current_url
        
        print(f"Giriş yapılınca /inventory.html sayfasına gidiyor mu: {currentUrl.endswith('/inventory.html')}")
    
    # Test 6: Giriş yapılınca 6 adet ürün gösteriyor mu?
    def test6(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        userNameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(5)
        userNameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(3)
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(10)
        listOfProducts = driver.find_elements(By.CLASS_NAME,"inventory_item_name")
        if (len(listOfProducts) == 6):
            testResult = True
            print(f"Giriş yapılınca sergilenen ürün sayısı 6 mı: {testResult}")


    
        

        


        


testClass = Testler()
print("Test 1 deneniyor.")
testClass.test1()
print("*******************")
print("Test 2 deneniyor.")
testClass.test2()
print("*******************")
print("Test 3 deneniyor.")
testClass.test3()
print("*******************")
print("Test 4 deneniyor.")
testClass.test4()
print("*******************")
print("Test 5 deneniyor.")
testClass.test5()
print("*******************")
print("Test 6 deneniyor.")
testClass.test6()


