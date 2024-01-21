from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from infobip_channels.sms.channel import SMSChannel
import schedule
from twilio.rest import Client

def main():
    usernameStr = '******'
    passwordStr = '******'
    driver = webdriver.Chrome()
    driver.get(('http://radius.cloudsp.net.lb/login/?next=/userpage/'))
    username = driver.find_element(By.ID,'user-name')
    username.send_keys(usernameStr)
    password = driver.find_element(By.ID,'user-password')
    password.send_keys(passwordStr)
    signInButton = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/section/div/div/div/div[2]/div/form/button')
    signInButton.click()
    time.sleep(1)
    news_path = '/html/body/div[4]/div/div[5]/div[1]/div/div/div/div[1]/div[2]/div/div/div' 
    link = driver.find_element(By.XPATH,news_path)   
    print(link.text)
    x=str(link.text).replace("%","")
    time.sleep(1)   
    driver.close()
    account_sid = 'AC********************************'
    auth_token = '********************************'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_='whatsapp:+XXXXXXXXXXX',
    body="x",
    to='whatsapp:+XXXXXXXXXXX'
    )
    print(message.sid)

if __name__ == "__main__":
    main()
schedule.every(60).minutes.do(main)
while True:
    schedule.run_pending()
    time.sleep(1)
