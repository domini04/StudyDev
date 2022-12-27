# dict를 csv로 만들어보기

z = [{'이름':'짱구','수학':90,'영어':100}, {'이름':'짱아','수학':95,'영어':97}]
import csv
with open('practice.csv', 'w') as csv_file:
  fields = ['이름', '수학','영어']
  writer = csv.DictWriter(csv_file, fieldnames=fields)

  writer.writeheader()
    #writer.writerow({'이름':'짱구','수학':90,'영어':100})  이렇게도 가능
  for item in z:
    writer.writerow(item)
