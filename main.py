from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class Bot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def OpenForm(self, form_url):
        self.driver.get(form_url)
        time.sleep(1)

    def GetPytania(self):
        div_z_pytaniami = self.driver.find_element(By.CLASS_NAME, "o3Dpx")
        return div_z_pytaniami.find_elements(By.CLASS_NAME, "Qr7Oae")

    def WybierzOpcjeRadioButton(self, pytanie, nr_opcji):
        btns = pytanie.find_elements(By.CSS_SELECTOR, ".d7L4fc.bJNwt.FXLARc.aomaEc.ECvBRb")
        btns[nr_opcji].click()

    def WybierzOpcjeCheckButton(self, pytanie, nr_opcji):
        btns = pytanie.find_elements(By.CSS_SELECTOR, ".uVccjd.aiSeRd.FXLARc.wGQFbe.BJHAP.oLlshd")
        btns[nr_opcji].click()

    def Prześlij(self):
        submit_button = self.driver.find_element(By.XPATH, "//div[@role='button']//span[text()='Prześlij']")
        submit_button.click()

    def DoTheThing(self):
        self.driver.get("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        time.sleep(10)

if __name__ == "__main__":
    bot = Bot()
    DoTheThing()
    bot.OpenForm("https://docs.google.com/forms/d/e/1FAIpQLSctNmsjLW082da48bVWE2Euy7l5C1zfRi4-oTh59e3a22uDFA/viewform")
    pytania = bot.GetPytania()

    if pytania:
        bot.WybierzOpcjeRadioButton(pytania[0], 0)
        bot.WybierzOpcjeCheckButton(pytania[1], 3)
        # itd...
    
    input("test")
    bot.Prześlij()  