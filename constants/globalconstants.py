import random
from selenium.webdriver.common.by import By


#ANASAYFA

BASE_URL = "https://www.2ntech.com.tr/hr/"
ADSOYAD=(By.XPATH,"//input[@id='name']")
ADSOYADTEXT="asaf"
DOGUMTARIHI=(By.XPATH,"//input[@id='birth']")
DOGUMTARIHITEXT="24011992"
TCKIMLIK=(By.XPATH,"//input[@id='tcKimlik']")
TCKIMLIKTEXT="12345678901"
TELEFONTEXT="05111111111"
TELEFON=(By.XPATH,"//input[@id='phone']")
MAIL=(By.XPATH,"//input[@id='email']")
MAILTEXT="a@mail.com"
CVYUKLEME=(By.XPATH,"//label[@for='cv_field']")
EGITIMBILGISI=(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[2]/form/div[5]/div/button[2]")
ILERITUS=(By.XPATH,"//button[@type='submit']")
TEST=(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/div[1]/span")
GONDERBUTONU=(By.XPATH,"//div[@class='text-white flex justify-center items-center text-[14px] py-2 px-4 rounded-full bg-[#DF1F29] cursor-pointer']")


