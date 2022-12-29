#https://boxstat.co/popular-boxers를 기준으로 크롤링 진행

#I.env 설정
# 필요한 모듈을 임포트 합니다
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 키보드 입력을 위한 모듈
from selenium.webdriver.common.by import By # By 클래스를 임포트 합니다
import warnings # 경고 메시지를 무시하기 위한 모듈
import time # time 모듈을 임포트 합니다
from datetime import datetime 
import re   # 정규표현식을 위한 모듈
import json 
import os

warnings.filterwarnings('ignore')

#II. 크롤러
class Crawler:
  def setup(self, driver_path, wait_time=3,load_timeout=10): # 드라이버 경로, 대기시간, 로드 타임아웃을 인자로 받습니다
    options = webdriver.ChromeOptions() # 받은 인자를 사용해 크롬 옵션을 설정합니다
    options.add_experimental_option('excludeSwitches', ['enable-logging']) # 셀레니움 로그를 숨기는 옵션을 추가합니다

    self.driver_path = driver_path  # 드라이버 경로를 저장합니다
    self.driver = webdriver.Chrome(self.driver_path, options=options)   # 드라이버를 생성합니다(옵션 포함)
    self.driver.implicitly_wait(wait_time)  # 대기시간을 설정합니다
    self.driver.set_page_load_timeout(load_timeout) # 페이지 로드 시간 초과 설정
    self.start_time = time.time() #시작 시간 기록
    self.boxer_data = {}  # 복서 데이터를 저장할 딕셔너리를 생성합니다
    self.error_list = [] # 에러가 발생한 복서의 이름을 저장할 리스트를 생성합니다 get_boxer_info() 메서드에서 사용합니다
    
    print("------------------------------------------------ -_- ---------"*2)
    print("Crawler created at : ", datetime.now().strftime("%H:%M:%S"))
    
  def get_url(self, url, download_path ="C:\\Users\\Lenovo\\Downloads"):  # 페이지를 열어주는 메서드. url을 인자로 받습니다
    self.url = url
    self.driver.get(self.url)
    # self.driver.save_screenshot(download_path + '\\sc1.png')  # 스크린샷 저장
    self.driver.maximize_window() # 창을 최대화 합니다
    print("------------------------------------------------ -_- ---------"*2)
    print(f"Page {url} loaded at : ", datetime.now().strftime("%H:%M:%S"))

  def navigate_link(self, boxer_no):  # 복서의 링크를 클릭하는 메서드. 복서 번호를 인자로 받습니다. 번호는  boxerid가 아니라, html상의 순서입니다
    #boxer_no는 1부터 2760까지 알파벳 순입니다
    boxer_link = self.driver.find_element(By.XPATH, f'/html/body/div[4]/div/div/div/div[2]/article/div/div/div/a[{boxer_no}]')  # 복서의 링크를 찾습니다
    boxer_link.click()  # 링크를 클릭합니다
    print("------------------------------------------------ -_- ---------"*2)
    print("Boxer link clicked at : ", datetime.now().strftime("%H:%M:%S"))
  
  def get_boxer_info(self): # 복서 정보를 가져오는 메서드입니다  #이 부분은 코드가 난잡해서 나중에 정리하겠습니다. 리팩토링 필요할지도?
    boxer_stats = {}  # 복서 정보를 저장할 딕셔너리를 생성합니다

    # 복서 이름 및 전적을 가져옵니다
    boxer_name = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[5]/div[1]/div/div[2]/div/div[2]/h1').text  # 복서 이름을 가져옵니다
    boxer_stats['name'] = boxer_name  # 복서 이름을 딕셔너리에 저장합니다
    boxing_record_bulk = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[5]/div[1]/div/div[2]/div/div[3]')  # 복서 전적을 가져옵니다  
    boxing_record_bulk = boxing_record_bulk.text.split('\n')  # 복서 전적을 리스트로 저장합니다
    boxing_record_stat, boxing_record_name = boxing_record_bulk[::2], boxing_record_bulk[1::2]  # 복서 전적과, 승/패/무 가 뭉쳐져 있기에 이를 분리합니다.
    boxer_stats.update(dict(zip(boxing_record_name, boxing_record_stat)))  # boxing_record_name을 key로 boxing_record_stat을 value로 하는 딕셔너리를 boxer_stats에 추가합니다
    # print(boxing_record)
    #수정 point 1 : boxer_name이란 상위 문서를 webdriverElement클래스로 가져왔는데, 여기서 하위 문서에 해당하는 boxing_record_bulk를 추출 가능한지?
      # 만약 가능하다면 find_element를 두 번 사용 할 필요 없이 한 번만 사용해서 boxing_record_bulk를 가져올 수 있을 것 같습니다.
      # -> bs4 사용하면 가능할듯. 근데 귀찮음... 일단 보류
    
    #기본 스탯
    boxer_stats_bulk = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[5]/div[6]/div/div[2]').text  # 복서 기본 스탯을 가져옵니다. 이하 앞부분과 동일
    boxer_stats_bulk = boxer_stats_bulk.split('\n')
    boxer_stats_val, boxer_stats_name = boxer_stats_bulk[::2], boxer_stats_bulk[1::2]
    boxer_stats.update(dict(zip(boxer_stats_name, boxer_stats_val)))

    #Advanced Stats 
    advanced_stats = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[5]/div[5]/div/div[2]').text
    advanced_stats = advanced_stats.split('\n')
    # print('advanced_stats : ', advanced_stats) #디버깅용
    #해당 자료를 보면 advanced stats들과 선수의 승리 종류 (UD/Split/TKO)가 뭉쳐져 있습니다. 이를 분리합니다
    #그리고 '선수명 Results'라는 텍스트도 들어 있습니다. 이를 제거합니다
    regex = re.compile(r'.+RESULTS$') # '선수명 RESULTS'를 찾기 위한 정규표현식입니다
    idx = [i for i, x in enumerate(advanced_stats) if regex.match(x)] # '선수명 RESULTS'의 인덱스를 찾습니다 
    #수정 point.2 : 이 부분은 굳이 list로 할 필요 없이 바로 int로 받도록 수정 가능할지도?
    adv_stats, w_type = advanced_stats[:idx[0]], advanced_stats[idx[0]+1:]  # advanced_stats와 w_type을 분리합니다
    
    advanced_stats_val, advanced_stats_name = adv_stats[::2], adv_stats[1::2] 
    boxer_stats.update(dict(zip(advanced_stats_name, advanced_stats_val)))  # advanced_stats를 boxer_stats에 추가합니다
    # for string in w_type:
    #   re.sub(r'[()]', '', string)
    
    #문제. 아래의 w_type데이터가 잘못 들어가 있는 선수들이 있습니다. (웹사이트 관리 제대로좀...)
    # Ronald Maldini :PTS (30.8%) (7.7%) UD (7.7%)
    # Charles Martin : UD (9.7%) (3.2%) DQ (3.2%) 처럼 특정 데이터가 두 번 들어가 있는 경우가 있습니다.

    #디버깅
    #방법 1. advanced_stats를 받아올 때, 먼저 데이터가 중복되어 있는지 검사 -> 리소스를 많이 잡아먹을듯. 잘못된 데이터가 엄청 많진 않은데 굳이?
    #방법 2. try except를 사용해서 데이터가 중복되어 있는 경우, 두 번째 데이터를 제거 ->이게 나을듯?(모든 잘못된 데이터가 이런 식이라는 가정 하에)
    # print('w_type 1: ', w_type) #디버깅용
    for i,s in enumerate(w_type):  # w_type은 ['KO (45.2%)', 'TKO (25.8%)', 'RTD (9.7%)', 'UD (9.7%)', '(3.2%)', 'DQ (3.2%)', 'MD (3.2%)'] 같은 형태입니다
      w_type[i] = s.replace('(', '').replace(')', '') # w_type에서 괄호를 제거합니다
    # w_type = [re.sub(r'[()]', '', s).split(' ') for s in w_type]  #수정 전 코드
    try :   #이 부분은 try except를 사용해서 에러가 발생하면, 중복된 데이터를 제거하고 다시 시도하도록 수정했습니다
      w_type_split = [s.split(' ') for s in w_type] # w_type을 공백을 기준으로 분리합니다
      w_type_dict = {s[0]:s[1] for s in w_type_split} # <------ 이 부분에서 에러가 발생합니다(중복된 데이터가 있는 경우 : index out of range)
      boxer_stats['win_type'] = w_type_dict # win_type을 boxer_stats에 추가합니다. win_type을 종류별로 묶어서 딕셔너리로 만든 후 추가합니다
      #{win_type: {KO: 50%, UD: 20%, TKO: 3%, ...}} 같은 형태로 저장됩니다
    except IndexError as e: 
      try:  #데이터가 중복되어 있는 경우, 두 번째 데이터를 제거합니다
        print(e, ' : ', "중복된 데이터가 있습니다. 두 번째 데이터를 제거합니다")
        w_type = '`'.join(w_type) #중복을 제거하기 위해 데이터를 하나의 string으로 합칩니다(re.sub은 string만 받을 수 있음). `는 다시 split할때 구분자로 사용합니다
        # print('w_type 2: ',w_type) #디버깅용
        w_type = re.sub(r'[()]', '', w_type)  # w_type에서 괄호를 제거합니다. 중복 데이터도 제거해야하기에 split은 나중에 하겠습니다
        regex = re.compile(r'[0-9]+\.[0-9]%`[0-9]+\.[0-9]*%') # 중복된 데이터를 찾기 위한 정규표현식입니다. % % 형태인 경우 매칭됩니다 (ex. 30% 7%). (30% UD 6%는 매칭되지 않습니다)
        duplicate_values = re.search(regex, w_type).group() # w_type에서 해당 패턴과 일치하는 부분을 찾습니다. .group()을 사용해서 매칭된 부분만 가져옵니다
        print('duplicate_values : ', duplicate_values) #디버깅용
        w_type = w_type.replace(duplicate_values, duplicate_values.split('`')[0]) # 중복된 데이터를 제거합니다. 첫 번째 데이터는 옳은 수치이므로 제거하지 않습니다. 30% 7% -> 30%만 가져갑니다.
        # print('w_type 3: ',w_type) #디버깅용
        w_type = w_type.split('`')  # w_type에서 공백을 기준으로 분리합니다
        # print('w_type 4: ',w_type) #디버깅용
        w_type_split = [s.split(' ') for s in w_type] # w_type을 공백을 기준으로 분리합니다
        w_type_dict = {s[0]:s[1] for s in w_type_split}
        boxer_stats['win_type'] = w_type_dict
      except : #중복된 데이터가 아니라 다른 잘못된 데이터가 있는 경우
        print("중복데이터가 아닌 다른 에러가 발생했습니다")
        self.error_list.append(boxer_name)  # 에러가 발생한 선수를 error_list에 추가합니다
    except :  # 다른 에러가 발생한 경우
      pass

    # Opponent Stats : 상대방 스탯 평균
    boxer_stats_bulk = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[5]/div[6]/div/div[4]') # 상대방 평균 스탯을 가져옵니다. 이 수치가 높을수록 강한 상대와 맞붙었다고 볼 수 있을듯?
    boxer_stats_bulk = boxer_stats_bulk.text.split('\n')  
    boxer_stats_val, boxer_stats_name = boxer_stats_bulk[::2], boxer_stats_bulk[1::2]
    boxer_stats.update({'opponent' : dict(zip(boxer_stats_name, boxer_stats_val))})  # boxer_stats_name을 key로 boxer_stats_stat을 value로 하는 딕셔너리를 opponent라는 key로 boxer_stats에 추가합니다
    # opponent는 {opponent: {height: 5'10", reach: 72", ...}} 같은 형태로 저장됩니다

    # print(boxer_stats)
    self.boxer_data.update({boxer_name : boxer_stats})  # 마지막으로 복서의 데이터를 이름으로 묶은 딕셔너리를 만들어, 최종 데이터에 추가합니다
    # print(self.boxer_data) #테스트용
    print("------------------------------------------------ -_- ---------"*2)
    print(f"Boxer {boxer_name} data scraped at : ", datetime.now().strftime("%H:%M:%S"))\
  
  def export_data(self, path, filename): #데이터를 json 파일로 저장합니다
    if os.path.exists(f'{path}/{filename}.json'): #파일이 이미 존재하는 경우
      with open(f'{path}/{filename}.json', 'a') as f: #기존 파일에 추가합니다
        json.dump(self.boxer_data, f, indent=4)
    else :  #파일이 존재하지 않는 경우
      with open(f'{path}/{filename}.json', 'w') as f: #새로 파일을 만들어 저장합니다
        json.dump(self.boxer_data, f, indent=4) #자료를 json형태로 변환하여 지정한 경로에 저장합니다
      print(f"Boxer data exported at : {path}/{filename}.json")

  def export_error(self,path, filename):    #에러가 발생한 선수들의 이름을 txt 파일로 저장합니다
    if os.path.exists(f'{path}/{filename}.txt'): #파일이 이미 존재하는 경우
      with open(f'{path}/{filename}.txt', 'a') as f:
        f.write('\n'.join(self.error_list))
    else:
      with open(f'{path}/{filename}.txt', 'w') as f:
        f.write('\n'.join(self.error_list))

#III. 실행
if __name__ == '__main__' : #파이썬 파일을 직접 실행할 때만 실행되는 코드입니다. 이 코드를 실행하면, boxer_data에 복서들의 데이터가 저장됩니다
  test = Crawler()
  # chromedriver_path = input("크롬드라이버 경로를 지정해주세요. ex) 'C:\\Users\\Lenovo\\Downloads\\chromedriver.exe'")
  chromedriver_path = 'C:\\Users\\Lenovo\\Downloads\\chromedriver.exe' 
  # data_download_path = input("선수 데이터를 다운받을 경로를 지정해주세요. ex) 'C:\\Users\\Lenovo\\Downloads\\data'")
  # error_download_path = input("에러 리스트를 다운받을 경로를 지정해주세요. ex) 'C:\\Users\\Lenovo\\Downloads\\data'")
  test.setup(chromedriver_path)
  for i in range(2700,2761):  #1500번부터 1510번까지의 복서 데이터를 긁어옵니다 복서 번호는 1 ~ 2760까지 존재합니다
    test.get_url('https://boxstat.co/popular-boxers')
    test.navigate_link(i) 
    test.get_boxer_info()
    # print(test.boxer_data)  #테스트용
    # print(i)  #테스트용
  
  data_download_path = 'C:\\Users\\Lenovo\\Downloads\\data'
  error_download_path = 'C:\\Users\\Lenovo\\Downloads\\data'
  test.export_data(data_download_path, 'boxer_data')  #데이터 export는 한 번만 해주면 되기에 반복문 밖에 위치시킵니다
  test.export_error(error_download_path, 'error_list')
  # print(test.boxer_data) #테스트용
  print("--- Scraping done. %s seconds total ---" % (time.time() - test.start_time)) #크롤링에 걸린 시간을 출력합니다
  print(f"--- {len(test.error_list)} errors occured ---") #에러가 발생한 횟수를 출력합니다
  test.driver.quit()  #복서 정보를 긁어오고 나면, driver를 종료합니다

  #특이사항 & 목표
#1. 복서의 데이터가 없는 경우에도 긁어와지는지 테스팅 안해봄............ -> 됨!
#2. 복서의 전적도 긁어오기(필요한 경우 추가)
#3. multiprocessing을 사용한 병렬처리 구현해보기
#4. boxrec의 데이터와 합칠 수 있도록 데이터 구조 및 전처리 진행하기
#5. 선수 데이터를 긁어올 때마다 저장하도록 수정하기(중요)
  # -> 지금은 선수 데이터를 모두 긁고 나서 저장하는데, 이렇게 하면 중간에 에러가 나면 데이터가 날아감

#실행방법
#1. 크롬드라이버 다운로드 및 경로 지정해주세요(크롬드라이버는 크롬 브라우저의 버전과 일치해야 합니다) -> III.실행 문단의 chromedriver_path
#2. 데이터를 저장할 경로를 지정해주세요 data_download_path, error_download_path
#3. 복서 데이터를 긁어오고 싶은 복서의 번호를 지정해주세요: 159번 줄의 range 수정
#4. 코드 실행
