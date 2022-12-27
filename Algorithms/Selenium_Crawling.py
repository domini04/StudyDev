from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import random

#https://www.opinet.co.kr/ (주유소 정보 사이트)를 기준으로 함
def launchBrowser(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://www.opinet.co.kr/user/main/mainView.do')
    driver.get(url)
    return driver
driver = launchBrowser('https://www.opinet.co.kr/searRgSelect.do')

time.sleep(3)
sido_path = '//*[@id="SIDO_NM0"]'
sido = driver.find_element(By.XPATH, sido_path)
# sido.click()#행정구역 - 시 click


#1. 랜덤한 city 클릭
#도시 리스트 뽑기
sido_list_names = sido.find_elements(By.TAG_NAME, 'option')
sido_list = [option.get_attribute('value') for option in sido_list_names]
# sido_list = sido_list[1:]
print(sido_list)

rand_city_num = random.choice(range(1,len(sido_list))) #첫 칸은 빈칸이기 떄문
rand_city = sido_list[rand_city_num]
print('랜덤한 도시번호는', rand_city_num)
print('랜덤한 도시는',rand_city)
rand_city_path = '//*[@id="SIDO_NM0"]/option[{}]'.format(rand_city_num+1) #두 칸씩 밀려있음! 도시는 2번부터 시작.
# print(rand_city_path)
driver.find_element(By.XPATH,rand_city_path).click() #랜덤한 시도 클릭

time.sleep(3)

#2. 해당 시의 랜덤한 구 선택
#서울 구 리스트 뽑기
gungu_path = '//*[@id="SIGUNGU_NM0"]'
gu = driver.find_element(By.XPATH, gungu_path)
gu_list_names = gu.find_elements(By.TAG_NAME, 'option')
gu_list = [option.get_attribute('value') for option in gu_list_names]
# gu_list = gu_list[1:]
print(gu_list)

# //*[@id="SIGUNGU_NM0"] 서울 -구
# //*[@id="SIGUNGU_NM0"] 부산 - 구 Xpath 똑같음!

rand_gu_num = random.choice(range(1,len(gu_list)))
rand_gu = gu_list[rand_gu_num]
print('랜덤한 구는', rand_gu)
rand_gu_path = '//*[@id="SIGUNGU_NM0"]/option[{}]'.format(rand_gu_num+1)
driver.find_element(By.XPATH, rand_gu_path).click() #랜덤한 구 클릭

#3. 해당 구의 랜덤한 읍/면/동 선택
dong_path = '//*[@id="DONG_NM"]'
dong = driver.find_element(By.XPATH, dong_path)
dong_list_names = dong.find_elements(By.TAG_NAME, 'option')
dong_list = [option.get_attribute('value') for option in dong_list_names]
# dong_list = dong[1:]
print(dong_list)

rand_dong_num = random.choice(range(1,len(dong_list)))
rand_dong = dong_list[rand_dong_num]
print('랜덤한 읍/면/동은', rand_dong)
rand_dong_path = '//*[@id="DONG_NM"]/option[{}]'.format(rand_dong_num+1)
driver.find_element(By.XPATH, rand_dong_path).click()

time.sleep(2)
#4. 조회 버튼 click
search_path = '//*[@id="searRgSelect"]/span'
driver.find_element(By.XPATH, search_path).click()

#5. 주유소 정보 엑셀로 다운로드
download_path = '//*[@id="glopopd_excel"]/span'
driver.find_element(By.XPATH, download_path).click()
