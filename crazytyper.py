from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
import time

# TODO: Add a random typer (poisson distributed?!) Hell yes

def interval(wpm):
    ''' determines the average time in seconds between words for
        a given rate in words per minute (wpm) '''
    return 60 / wpm

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# go to the google home page
driver.get("http://10fastfingers.com/typing-test/english")

# the page is ajaxy so the title is originally this:
print(driver.title)

try:
    wait = WebDriverWait(driver, 10)
    inputElement = wait.until(EC.presence_of_element_located((By.ID, "inputfield")))
    word_list = driver.execute_script("return document.getElementById('wordlist').innerHTML")

    # maximum speed (all input at once)
    # words = word_list.replace('|', ' ') + ' '
    # inputElement.send_keys(words)

    # input word by word
    # words = word_list.split('|')
    # for word in words:
    #     inputElement.send_keys(word + " ")

    words = word_list.replace('|', ' ') + ' '

    print(words)
    print('#:', len(words.split()))

    start_typing = time.time()
    input('Press enter')
    inputElement.send_keys(words)
    stop_typing = time.time()
    
    seconds_taken = (stop_typing - start_typing) / 1000
    wpm = len(words) / seconds_taken
finally:
    print('time:', seconds_taken)
    print('actual wpm:', wpm)
    #driver.quit()
