from selenium import webdriver
from selenium.webdriver.common.by  import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time
import datetime
import pyperclip

hora_actual = datetime.datetime.now().strftime('%H:%M')
usuario = 'John Doe'
contrasena = 'ThisIsNotAPassword'
fecha = '10/10/2023'
comentario = 'This is a reserve for health care services.'


class Formulario(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def test_login(self):
        self.driver.get('https://katalon-demo-cura.herokuapp.com/')
        self.wait.until(EC.presence_of_element_located((By.ID, 'btn-make-appointment')))
        login = self.driver.find_element(By.ID, 'btn-make-appointment')
        login.click()

        self.wait.until(EC.presence_of_element_located((By.ID, 'txt-username')))
        username = self.driver.find_element(By.ID, 'txt-username')
        username.send_keys(usuario)

        self.wait.until(EC.presence_of_element_located((By.ID, 'txt-password')))
        password = self.driver.find_element(By.ID, 'txt-password')
        password.send_keys(contrasena)

        password.send_keys(Keys.ENTER)
        time.sleep(3)
        self.wait.until(EC.presence_of_element_located((By.ID, 'radio_program_medicare')))

    def test_formulario(self):
        program = self.driver.find_element((By.ID, 'radio_program_medicare'))
        program.click()
        print("encontro el programa")
        
        date = self.driver.find_element(By.NAME, 'visit_date')
        date.send_keys(fecha)

        comment = self.driver.find_element((By.NAME, 'comment'))
        comment.send_keys(comentario)

        booking = self.driver.find_element(By.ID, 'btn-book-appointment')
        booking.click()

        self.wait.until(EC.presence_of_element_located((By.ID, 'facility')))
        facility = self.driver.find_element(By. ID, 'facility').text
        pyperclip.copy(facility)
        print('\nFacility: ', facility)

        self.wait.until(EC.presence_of_element_located((By.ID, 'hospital_readmission')))
        readmission = self.driver.find_element(By.ID, 'hospital_readmission').text
        pyperclip.copy(readmission)
        print('Apply for hospital readmission: ', readmission)

        self.wait.until(EC.presence_of_element_located((By.ID, 'program')))
        healtcare_program = self.driver.find_element(By.ID, 'program').text
        pyperclip.copy(healtcare_program)
        print('Healtcare Program: ', healtcare_program)

        self.wait.until(EC.presence_of_element_located((By.ID, 'visit_date')))
        visit = self.driver.find_element(By.ID, 'visit_date').text
        pyperclip.copy(visit)
        print('Visit Date: ', visit)
        time.sleep(2)

        print("Hora de la prueba:", hora_actual)
        input("Press Enter to continue...")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()