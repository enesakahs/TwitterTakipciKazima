from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
#selenıum uzerıden erıstıgımız sıtelerde klavye ıle ıslem yapmak ıstedıgımızde ımport etmemız gereken yapı. Örn: klavyeden enter a bas
from selenium.webdriver.common.by import By
from TwitterGirisBilgi import kullanıcıadı,sifre
import time

driver=webdriver.Chrome("C:/Users/enes_/OneDrive/Masaüstü/Python Egitimleri/ChromeDriver/chromedriver.exe")

url="https://www.twitter.com/login"
driver.get(url)
time.sleep(3)
driver.maximize_window()
time.sleep(3)

ka=driver.find_element(By.XPATH,"//input[@autocomplete='username']")
ka.send_keys(kullanıcıadı)
time.sleep(3)
ka.send_keys(Keys.ENTER)
time.sleep(3)

ksifre=driver.find_element(By.XPATH,"//input[@autocomplete='current-password']")
ksifre.send_keys(sifre)
time.sleep(3)
ksifre.send_keys(Keys.ENTER)
time.sleep(3)


#istenilen kisinin twitter sayfasına gidebilmek icin
url="https://www.twitter.com/ThePSF"
driver.get(url)
time.sleep(5)

takipci=driver.find_element(By.CSS_SELECTOR,"#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div:nth-child(3) > div > div > div > div > div.css-1dbjc4n.r-13awgt0.r-18u37iz.r-1w6e6rj > div:nth-child(2) > a")
takipci.click()
time.sleep(10)

takipciliste=driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/section/div").find_elements(By.CSS_SELECTOR,".css-901oao.css-1hf3ou5.r-1bwzh9t.r-18u37iz.r-37j5jr.r-1wvb978.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-qvutc0")
#takipci kısmına gelip incele dedik. Tüm takipcileri icinde barındıran genel divden xpathi aldık. Daha sonra en özele inip kullanıcı adının oldugu span etıketının hemen bir üstündeki yani spanı ıcınde bulunduran divin class=" " ını selector olarak aldık.
#Gelen yapıda önemli olan kısım yapının arasındaki boslukları silip . ile birlestirdik ve yapının en basına da . ekledik
sayac=1
for i in takipciliste:
    print(f"{sayac}-{i.text}")
    sayac+=1
    sayac=sayac
