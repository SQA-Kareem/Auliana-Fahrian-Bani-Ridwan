import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SystemTest(unittest.TestCase):
    def setUp(self):
        # Inisialisasi WebDriver
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Tambahkan penundaan waktu sebelum menutup WebDriver
        time.sleep(5)

        # Menutup WebDriver
        self.driver.quit()

    def login(self, email, password):

        time.sleep(2)

        # Mencari elemen input email dan password menggunakan ID
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "hs-toggle-password")

        # Memasukkan nama pengguna dan kata sandi
        email_input.send_keys(email)
        password_input.send_keys(password)

        time.sleep(2)

        # Klik tombol Login
        button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        button.click()

        time.sleep(5)

        # Cari dan klik tombol OK pada popup
        swal = self.driver.find_element(By.CLASS_NAME, "swal2-confirm")
        swal.click()

        time.sleep(2)

    def detail_magang(self):
        
        time.sleep(2)

        # Mencari elemen input email dan password menggunakan ID
        button = self.driver.find_element(By.XPATH, "//a[@href='cariInternship.html']")
        button.click()

        time.sleep(2)

        button = self.driver.find_element(By.XPATH, "//a[@href='detailMagang?magangId=65ab797ca8b25e04a4b4b518']")
        button.click()

        time.sleep(2)
        
        
    def apply_magang(self):
        
        #cari dan klik tombol daftar
        button = self.driver.find_element(By.XPATH, "//button[@class='inline-flex justify-center items-center gap-x-3 text-center bg-gradient-to-tl from-blue-600 to-violet-600 shadow-md shadow-transparent hover:shadow-blue-700/50 border border-transparent text-white text-sm font-medium rounded-lg focus:outline-none focus:ring-1 focus:ring-blue-600 focus:ring-offset-1 focus:ring-offset-white py-2 px-5']")
        button.click()
        
        time.sleep(2)
        
        #cari dan klik confirm pada popup
        swal = self.driver.find_element(By.CLASS_NAME, "swal2-confirm")
        swal.click()
        
        time.sleep(2)
                

    def test_detail_magang(self):
        # Membuka halaman web
        self.driver.get("https://intermoni.my.id/")

        time.sleep(2)

        button = self.driver.find_element(By.XPATH, "//a[@href='pages/signIn.html']")
        button.click()

        time.sleep(2)

        self.login("dimasmhs@gmail.com", "fghjkliow")

        time.sleep(2)

        self.detail_magang()
        
        self.apply_magang()


if __name__ == "__main__":
    unittest.main()