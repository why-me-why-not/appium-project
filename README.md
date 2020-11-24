# Appium project
Automation of ordering 'Online card' in the ['Post Bank' Android app](https://play.google.com/store/apps/details?id=ru.letobank.Prometheus) using [Appium](https://pypi.org/project/Appium-Python-Client/).

### Overview ###
Appium automation script creates an account in the app (phone number and sms code input is required), goes to the card order section, fills in the order form with test data and sends it. Test data is generated using Python tools and by making queries to a simple SQLite database.

### Requirements ###
 * [Appium Python Client](https://pypi.org/project/Appium-Python-Client/)
 * Adb connected Android device or emulator
 * Installed Post Bank app `ru.letobank.Prometheus.apk`
