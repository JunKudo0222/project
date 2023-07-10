#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time
import urllib

email = 'lebyoss@outlook.jp'    # メールアドレスを指定する
password = 'Iojk3231' # パスワードを平文で指定する
username = 'thii_kn' # ユーザ名を指定する
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15'

def main():
  # attempt login unless the profile directory is present
  isprofile = os.path.isdir(os.path.join(os.getcwd(), 'profile'))

  # instanciate
  bot = Tweetbot(email, password, username)

  if not isprofile:
    bot.login()

  # write access 1: text-only
  bot.update_status('これはテスト投稿ですうううeeeううううう。')

  # wait for space-karen
  time.sleep(10)

  # write access 2: text with media
  bot.update_status_with_media('これは画像付きテスト投稿ですうeeeううううううう。', ['image1.png', 'image2.png'])

class Tweetbot:
  def __init__(self, email, password, username):
    self.email = email
    self.password = password
    self.username = username
    self.user_agent = user_agent

    # set options for headless accessing
    chrome_options = webdriver.chrome.options.Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--user-agent=%s' % user_agent)
    chrome_options.add_argument('--user-data-dir=%s' % os.path.join(os.getcwd(), 'profile'))

    # instanciate
    self.driver = webdriver.Chrome(options = chrome_options)
    self.driver.set_window_size('1920', '1200')

    # wait for finding an element
    self.driver.implicitly_wait(10)

  
  def login(self):
    driver = self.driver

    # open login page
    driver.get('https://twitter.com/login')

    # login attempt using email
    try:
      elm = driver.find_element(By.XPATH, "//input[@name='text']")
      elm.send_keys(self.email)
      elm.send_keys(Keys.RETURN)
      time.sleep(5)
    except:
      driver.save_screenshot('debug-login.png')
      pass

    # sometimes twitter warns unusual access
    # in that case need to send the username
    try:
      elm = driver.find_element(By.XPATH, "//input[@name='text']")
      elm.send_keys(self.username)
      elm.send_keys(Keys.RETURN)
      time.sleep(5)
    except:
      driver.save_screenshot('debug-username.png')
      pass

    # send password
    try:
      elm = driver.find_element(By.XPATH, "//input[@name='password']")
      elm.send_keys(self.password)
      elm.send_keys(Keys.RETURN)
      time.sleep(5)
    except:
      driver.save_screenshot('debug-password.png')
      pass

  # post text-only
  def update_status(self, status):
    driver = self.driver

    # open post page
    text = urllib.parse.quote(status, safe='')
    url = "https://twitter.com/intent/tweet?text=%s" % text
    driver.get(url)
    time.sleep(5)

    # click the tweet button
    try:
      elm = driver.find_element(By.XPATH, "//div[@data-testid='tweetButton']")
      elm.click()
      time.sleep(5)
    except:
      driver.save_screenshot('debug-tweet.png')
      pass

  # post with media
  def update_status_with_media(self, status, media):
    driver = self.driver

    # open post page
    text = urllib.parse.quote(status, safe='')
    url = "https://twitter.com/intent/tweet?text=%s" % text
    driver.get(url)
    time.sleep(5)

    # prepare path for media files
    # all path must be full-path, and separated by LF
    media = [os.path.join(os.getcwd(), 'media', s) for s in media]
    media_files = "\n".join(media)

    # attach media files
    try:
      elm = driver.find_element(By.XPATH, "//input[@data-testid='fileInput']")
      elm.send_keys(media_files)
      time.sleep(5)
    except:
      driver.save_screenshot('debug-media-files.png')
      pass

    # click the tweet button
    try:
      elm = driver.find_element(By.XPATH, "//div[@data-testid='tweetButton']")
      elm.click()
      time.sleep(5)
    except:
      driver.save_screenshot('debug-tweet-media.png')
      pass

if __name__ == "__main__":
    main()

