from time import sleep
from ddt import ddt, data, unpack
from selenium import webdriver
from pages.Form import *
from pages.PageBase import *
from constants.globalconstants import*
import allure
import softest
import unittest
import pytest
from Tests.constest import*


@pytest.mark.usefixtures("setup")
@ddt
class TestKisiselBilgiler(softest.TestCase, unittest.TestCase):
    


    def test_kisisel_bilgileri_doldur(self):
        form = Kisisel_bilgileri_doldur(self.driver)
        
        form.ad_soyadini_yaz()
        form.Dogum_tarihini_yaz()
        form.Tc_kimlik_no_yaz()
        form.Telefon_no_yaz()
        form.Email_yaz()
        form.cv_yukle()
        form.egitim_bilgi_tikla()
        form.ileri_tusuna_bas()
        sleep(2)
        form.Test_mühendisi_alanina_tikla()
        form.gonder_butonuna_tikla()