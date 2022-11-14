import bs4 as bs
import urllib.request
from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from send_email import sendEmail

while(True):
        try:
                driver = webdriver.Firefox()
                driver.get("https://evisaforms.state.gov/Instructions/ACSSchedulingSystem.asp")
                # await in end upload 
                # time.sleep(20)
                driver.implicitly_wait(25)
                # page 1 selected country and selected city and click submit 
                # select country
                country = driver.find_element(By.NAME , "CountryCodeShow")
                dropCountry = Select(country)
                dropCountry.select_by_index('49') # index Egypt = 49  # index Turkey 163
                # select city
                city = driver.find_element(By.NAME , "PostCodeShow")
                dropCity = Select(city)
                dropCity.select_by_index('1') # index Cairo = 1  # index Ankara 2
                # click button
                btn = driver.find_element(By.NAME , "Submit")
                btn.click()

                # page 2 click button
                btn2 = driver.find_element(By.XPATH , "//input[@value='Make Appointment!']")
                btn2.click()

                # page 3 click radio button and click checkbox and click button submit
                # click radio button
                radio = driver.find_element(By.XPATH , "//input[@value='AA']")
                radio.click()
                # click checkbox button
                checkbox = driver.find_element(By.NAME , "chkbox01")
                checkbox.click()
                # click button submit
                btn3 = driver.find_element(By.XPATH , "//input[@value='Submit']")
                btn3.click()

                url =  driver.page_source
                soup = bs.BeautifulSoup(url , 'html.parser')
                listTd = soup.find_all("td" , class_="formfield" , bgcolor="#ffffc0")
                countAvailable = 0

                for td in listTd:
                        countAvailable = countAvailable + 1

                if listTd:
                        print("The list is not empty")
                        sendEmail("قم بمراجعة مواعيد السفارة هناك مواعيد متاحة في "+str(countAvailable)+"أيام")
                        print(countAvailable)
                else:
                        print("the list empty")

                # await 5 second and exit the browser
                time.sleep(5)
                driver.quit()
        except Exception as e:
                print(e)
                driver.quit()
        print('أنتظر 30 دقيقة وسوف يعيد التنفيذ مرة أخري')
        time.sleep(1800)


