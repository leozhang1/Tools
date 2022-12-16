# code inspired by https://www.youtube.com/watch?v=GpDQpiCiNZ8&ab_channel=TopNotchProgrammer

# Prerequistes mentioned in the video:
# In settings:
#   - make sure videos are never made for kids
import os
import pwd

import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


os.chdir(os.path.dirname(__file__))

chrome_options = Options()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument("--log-level=3")
chrome_options.set_capability("detach", True)
# which chrome profile to use
chrome_options.add_argument('--profile-directory=Default')
# directory containing all the profiles
chrome_options.add_argument(f"--user-data-dir=/home/{pwd.getpwuid(os.getuid()).pw_name}/.config/google-chrome/")
chrome_options.binary_location = "/opt/google/chrome/google-chrome"
print("\033[1;31;40m IMPORTANT: Put one or more videos in the *videos* folder in the bot directory. Please make sure to name the video files like this --> Ex: vid1.mp4 vid2.mp4 vid3.mp4 etc..")
# sleep(6)

print("\033[1;31;40m IMPORTANT: Please make sure the name of the videos are like this: vid1.mp4, vid2.mp4, vid3.mp4 ...  etc")

dir_path = f'{os.getcwd()}/videos'
count = 0

for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1
print("   ", count, " Videos found in the videos folder, ready to upload...")
sleep(6)

for i in range(2,6):
    bot = uc.Chrome(options=chrome_options)
    bot.get("https://studio.youtube.com")
    sleep(3)
    upload_button = bot.find_element(By.XPATH, '//*[@id="upload-icon"]')
    upload_button.click()
    sleep(1)

    file_input = bot.find_element(By.XPATH, '//*[@id="content"]/input')
    simp_path = f'videos/vid{i}.mkv'
    abs_path = os.path.abspath(simp_path)

    file_input.send_keys(abs_path)

    sleep(7)

    inputs = bot.find_elements(By.XPATH, '//*[@id="textbox"]')

    title, desc = inputs

    # TODO: grab from config file
    title.clear()
    title.send_keys('title')
    desc.clear()
    desc.send_keys('desc')

    next_button = bot.find_element(By.XPATH, '//*[@id="next-button"]')
    for i in range(3):
        next_button.click()
        sleep(1)

    done_button = bot.find_element(By.XPATH, '//*[@id="done-button"]')
    done_button.click()
    sleep(5)
    bot.quit()

    print('finished with this video')
    sleep(5000)





