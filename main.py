from appium import webdriver
import time
import os
from appium.webdriver.common.touch_action import TouchAction

import utils


app = os.path.abspath('ru.letobank.Prometheus.apk')

utils.db_init()

desired_cap = {
    "platformName": "Android",
    "appPackage": "ru.letobank.Prometheus",
    "deviceName": "Android Emulator",
    "appWaitActivity": "ru.letobank.Prometheus.ui.activity.common.LeafHolderActivity",
    "app": app,
    "newCommandTimeout" : "600"
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
driver.implicitly_wait(30)

def swipe_up(count):
    for _ in range(count):
        driver.swipe(start_x=520, start_y=1260,
                     end_x=520, end_y=600,
                     duration=400)
        time.sleep(1)

def swipe_down(count):
    for _ in range(count):
        driver.swipe(start_x=520, start_y=600,
                     end_x=520, end_y=1260,
                     duration=400)
        time.sleep(2)

# 'Start to use' button
driver.find_element_by_id('ru.letobank.Prometheus:id/buttonStartUsing').click()


# Phone number
phone_number_message = driver.find_element_by_id('ru.letobank.Prometheus:id/messageInput')
phone_number = input('Phone number: ')
phone_number_message.send_keys(phone_number)
send_button = driver.find_element_by_id('ru.letobank.Prometheus:id/messageSendButton')
send_button.click()

# SMS code
sms_code_message = driver.find_element_by_id('ru.letobank.Prometheus:id/messageInput')
sms_code = input('SMS code: ')
sms_code_message.send_keys(sms_code)
send_button = driver.find_element_by_id('ru.letobank.Prometheus:id/messageSendButton')
send_button.click()

# Set PIN code '1234'
time.sleep(5)
touch = TouchAction(driver)
for _ in range(2):
    touch.tap(x=140, y=1210).perform() #1
    time.sleep(2)
    touch.tap(x=440, y=1210).perform() #2
    time.sleep(2)
    touch.tap(x=720, y=1210).perform() #3
    time.sleep(2)
    touch.tap(x=140, y=1360).perform() #4
    time.sleep(2)

# No fingerprint
no_fingerprint = driver.find_elements_by_id('ru.letobank.Prometheus:id/btn_item_action')[-1]
no_fingerprint.click()

# Enter account
driver.find_element_by_id('ru.letobank.Prometheus:id/buttonBottom').click()
time.sleep(5)

# Close pop-ups
driver.find_element_by_id('ru.letobank.Prometheus:id/okButton').click()
driver.find_element_by_id('ru.letobank.Prometheus:id/buttonClose').click()

# 'Open' button
open_button = driver.find_element_by_id('ru.letobank.Prometheus:id/viewAddNewProduct')
open_button.click()


# Online card
time.sleep(4)
swipe_up(count=2)
online_card = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.\
FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/\
android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/androidx.\
recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[1]')
online_card.click()


# Continue button
time.sleep(3)
continue_button = driver.find_element_by_id('ru.letobank.Prometheus:id/hidingMainActionButton')
continue_button.click()

# 'Order card online' button
time.sleep(15)
swipe_up(count=4)
open_online = driver.find_element_by_xpath('//android.view.View[@content-desc="Открыть онлайн"]')
open_online.click()
print('жмём ОТКРЫТЬ ОНЛАЙН')

# Card order form
time.sleep(15)
swipe_down(count=4)
full_name = driver.find_element_by_id('fullName')
name = utils.name_gen()
full_name.send_keys(name)

birthday = driver.find_element_by_id('birthDate')
birthday = utils.date_gen()
birthday.send_keys(birthday)
swipe_up(count=1)

passport_series = driver.find_element_by_id('passportSeries')
series = utils.passport_series()
passport_series.send_keys(series)

passport_number = driver.find_element_by_id('passportNumber')
number = utils.six_number_gen()
passport_number.send_keys(number)
swipe_up(count=1)

passport_code = driver.find_element_by_id('passportCodeDivision')
code = utils.six_number_gen()
passport_code.send_keys(code)

birth_place = driver.find_element_by_id('passportPlaceOfBirth')
place = utils.birth_place_gen()
birth_place.send_keys(place)
swipe_up(count=1)

issue_date = driver.find_element_by_id('passportDateOfIssue')
date = utils.date_gen()
issue_date.send_keys(date)

issuer = driver.find_element_by_id('passportIssuer')
issuer.send_keys(f'отделом УФМС гор. {place}')
swipe_up(count=1)

snils = driver.find_element_by_id('snils')
snils_num = utils.snils_gen()
snils.send_keys(snils_num)
swipe_up(count=1)

checkbox = driver.find_element_by_xpath('//android.webkit.WebView[@content-desc="Почта Банк Интернет-банк"]\
/android.view.View/android.view.View[3]/android.view.View[1]')
checkbox.click()

final_button = driver.find_element_by_xpath('//android.widget.Button[@content-desc="ОТПРАВИТЬ ДАННЫЕ"]')
final_button.click()