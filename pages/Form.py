import pytest
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from pages.PageBase import PageBase
from constants.globalconstants import *
from Tests.constest import*

#kategori_ve_alt_kategori_seçimi
@pytest.mark.usefixtures("setup")
class Kisisel_bilgileri_doldur(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    

    def ad_soyadini_yaz (self):
       self.wait_element_visibility(ADSOYAD).click()
       self.wait_element_visibility(ADSOYAD).send_keys(ADSOYADTEXT)


    def Dogum_tarihini_yaz(self):
        self.wait_element_visibility(DOGUMTARIHI).click()
        self.wait_element_visibility(DOGUMTARIHI).send_keys(DOGUMTARIHITEXT)

    def Tc_kimlik_no_yaz(self):
        self.wait_element_visibility(TCKIMLIK).click()
        self.wait_element_visibility(TCKIMLIK).send_keys(TCKIMLIKTEXT)
    
    def Telefon_no_yaz(self):
        self.wait_element_visibility(TELEFON).click()
        self.wait_element_visibility(TELEFON).send_keys(TELEFONTEXT)

    def Email_yaz(self):
        self.wait_element_visibility(MAIL).click()
        self.wait_element_visibility(MAIL).send_keys(MAILTEXT)

    def cv_yukle(self):
        self.wait_element_visibility(CVYUKLEME).click()

    def egitim_bilgi_tikla(self):
        self.wait_element_visibility(EGITIMBILGISI).click()
    
    def ileri_tusuna_bas(self):
        self.wait_element_visibility(ILERITUS).click()
    
    sleep(5)
    

    def Test_mühendisi_alanina_tikla(self):
        self.wait_element_visibility(TEST).click()

    def gonder_butonuna_tikla(self):
        self.wait_element_visibility(GONDERBUTONU).click()
