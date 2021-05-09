import time                            # スリープを使うために必要
from selenium import webdriver         # Webブラウザを自動操作する（python -m pip install selenium)
import chromedriver_binary             # パスを通すためのコード

# heroku用にchromedriverのPATHを指定
driver = webdriver.Chrome()            # Chromeを準備
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--remote-debugging-port=9222')
driver.get('https://www.google.com/')  # Googleを開く
driver.set_window_size(950, 800)
time.sleep(5)                          # 5秒間待機
driver.quit()                          # ブラウザを閉じる
