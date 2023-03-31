**Pytest Decoratos**

## 1) @pytest.fixture

```
import pytest

class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


@pytest.fixture
def my_fruit():
    return Fruit("apple")


@pytest.fixture
def fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]


def test_my_fruit_in_basket(my_fruit, fruit_basket):
    assert my_fruit in fruit_basket

```

### Yukarıdaki kod içerisinde testimiz my_fruit olarak tanımlı meyvenin ("apple") fruit_basket olarak tanımlı meyve sepetinde olup olmadığını test ediyor.  eğer @pytest.fixture decoratorleri olmazsa, bu iki fonksiyon sabitlenmeyecek ve testim başarılı geçmeyecektir. Fixture fonksiyonların sabitlenmesine yarar.

## 2) @pytest.mark.parametrize

### Bu decorator ile testimize birden fazla parametreyi tupple olarak verip testin her verilen parametre için tekrar çalışmasını sağlarız.

```
@pytest.mark.parametrize("username,password",[("1","1"),("kullaniciadim","sifrem")])
    def test_invalid_login(self,username,password):
        #en fazla 5 saniye olacak şekilde user-name id'li elementin görünmesini bekle
        self.waitForElementVisible((By.ID,"user-name"))
        userNameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"),10)
        passwordInput = self.driver.find_element(By.ID,"password")
        userNameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{password}.png")        
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
```

### Burada testimiz username ve password alanlarında hem "1""1" ikilisini hem de "kullaniciadim" "sifrem" ikilisini ayrı ayrı test edecektir.

## 3) @pytest.mark.skip

### Bir test fonksiyonunu atlamak istediğimizde kullanırız, isteğe bağlı olarak yanına bir gerekçe de sunulabilir.

```
@pytest.mark.skip(reason="no way of currently testing this") #reason -> sunulan gerekçe, isteğe bağlı
def test_the_unknown():
...

```

## 4) @pytest.mark.xfail

### Bu decorator ile zaten başarısız olacağını bildiğimiz bir testi işaretleriz böylece testing ekranında sorun çıkarmaz "expected to fail" diye çıkar. 

```
@pytest.mark.xfail
def test_function():
    ...

```

## 5) @pytest.mark.timeout

### Bu decorator ile bir test fonksiyonuna süre sınırı koyabiliriz. Eğer tüm test kodu için bir global timeout süresi belirlendiyse, istediğimiz fonksiyonu bu decorator ile işaretleyip ona özel timeout süresi verebiliriz.

