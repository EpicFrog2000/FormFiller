from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
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
        btns = pytanie.find_elements(By.CSS_SELECTOR, '[role="radio"][aria-label]')
        if 0 <= nr_opcji < len(btns):
            btns[nr_opcji].click()

    def WybierzOpcjeCheckButton(self, pytanie, nr_opcji):
        btns = pytanie.find_elements(By.CSS_SELECTOR, '[role="checkbox"][aria-label]')
        if 0 <= nr_opcji < len(btns):
            btns[nr_opcji].click()

    def WybierzOpcjeSkali(self, pytanie, nr_opcji):
        btns = WebDriverWait(pytanie, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".Od2TWd.hYsg7c"))
        )
        # Find all elements matching the selector
        buttons = pytanie.find_elements(By.CSS_SELECTOR, ".Od2TWd.hYsg7c")
        
        # Ensure the option index is valid
        if nr_opcji < len(buttons):
            buttons[nr_opcji].click()
        
    def Prześlij(self):
        submit_button = self.driver.find_element(By.XPATH, "//div[@role='button']//span[text()='Prześlij']")
        submit_button.click()

if __name__ == "__main__":
    bot = Bot()
    while(True):
        bot.OpenForm("https://docs.google.com/forms/d/e/1FAIpQLSdQI-VK9i91942aHII7O_nZ6QxDx14ekVBnz6V5FfWjYFsGbQ/viewform")
        pytania = bot.GetPytania()
        if pytania: 
            bot.WybierzOpcjeRadioButton(pytania[0], random.choices([0, 1, 2, 3, 4], [2, 2, 2, 2, 1])[0]) # Jak często podróżujesz pociągiem?
            bot.WybierzOpcjeRadioButton(pytania[1], random.choices([0,1,2,3,4,5], [4, 4, 4, 4, 4, 4])[0]) # Ile masz lat?
            bot.WybierzOpcjeRadioButton(pytania[2], random.choices([0,1,2,3,4], [0, 1, 0, 1, 0])[0]) # W jakim celu najczęściej podróżujesz?
            bot.WybierzOpcjeCheckButton(pytania[3], random.choices([0,1,2,3,4], [0, 3, 0, 3, 0])[0]) # Z którym z wymienionych problemów spotkałeś się podczas podróży pociągiem?
            bot.WybierzOpcjeRadioButton(pytania[4], random.choices([0,1,2,3], [3, 3, 0, 3])[0]) # Który problem jest według ciebie najpoważniejszy?
            bot.WybierzOpcjeSkali(pytania[5], (random.randint(0, 9))) # W skali od 1 do 10, jak bardzo wcześniej zaznaczone problemy wpływają na twoją podróż? (1- nie wpływa, 10 - uniemożliwia podróż)
            bot.WybierzOpcjeSkali(pytania[6], (random.randint(0, 9))) # Jak oceniasz ogólny poziom bezpieczeństwa podczas podróży pociągiem?  (1 - bardzo niebezpiecznie, 10 - bardzo bezpiecznie)
            bot.WybierzOpcjeCheckButton(pytania[7], random.choices([0,1], [1, 1])[0]) # Czy byłbyś zainteresowany którymś z tych rozwiązań?
            bot.Prześlij()