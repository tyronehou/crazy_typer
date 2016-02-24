# Currently only works with 10fastfingers.com typing test

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
import time
import sys

# TODO: Add a random typer (exponential distributed interarrival times)

class DriverNotFoundException(Exception):
    pass

def interval(wpm):
    ''' determines the average time in seconds between words for
        a given rate in words per minute (wpm) '''
    return 60 / wpm

class typer:

    def __init__(self, browser, max_speed=True):
        # Create a new instance of the specified driver
        if browser == 'HTML':
            self.driver = webdriver.Remote(desired_capabilities=webdriver.
                                           DesiredCapabilities.HTMLUNIT.copy())
        elif browser == 'Firefox':
            self.driver = webdriver.Firefox()
        else:
            raise DriverNotFoundException

        self.max_speed = max_speed

    def run(self):
        self.driver.get("http://10fastfingers.com/typing-test/english")

        print(self.driver.title)
        
        try:
            wait = WebDriverWait(self.driver, 10)
            inputElement = wait.until(EC.presence_of_element_located((By.ID, "inputfield")))
            word_list = self.driver.execute_script("return document.getElementById('wordlist').innerHTML")

            # Format the outputted list
            words = word_list.replace('|', ' ') + ' '

            print(words)
            print('#:', len(words.split()))
            input('Press enter')
            
            if self.max_speed:
                inputElement.send_keys(words)
            else:
                words = words.split()
                for word in words:
                    inputElement.send_keys(word + " ")

            input('Press enter to quit')
        finally:
            self.driver.quit()


if __name__ == '__main__':
    max_speed = False
    typer('Firefox', max_speed).run()
