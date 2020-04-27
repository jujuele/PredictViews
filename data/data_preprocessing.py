import glob
import numpy as np
import pandas as pd

files = glob.glob("today*.csv") #today로 시작하는 모든 파일을 묶어줄 함수
df_list = []
for filename in files:
  data = pd.read_csv(filename)
  df_list.append(data)
df = pd.concat(df_list)

df.head() # 처음 5행, 윗부분을 보여줌
df.info() # 표의 속성을 요약해줌
df.describe() #기 술 통계를 요약해줌
df.columns # 열 이름을 보여줌



df = df.drop_duplicates(subset=['Title']) #Title이 중복되는 행 삭제
df = df.dropna() # 결측값이 있는 모든 행 삭제

df.head() # 처음 5행, 윗부분을 보여줌
df.info() # 표의 속성을 요약해줌
df.describe() # 기술 통계를 요약해줌
df.columns # 열 이름을 보여줌


# 데이터 값들을 정수로 변환해줌
df.View = pd.to_numeric(df.View)
df.Coment = pd.to_numeric(df.Coment)
df.Like = pd.to_numeric(df.Like)
df.Subscriber = pd.to_numeric(df.Subscriber)

df.head() # 처음 5행, 윗부분을 보여줌
df.info() # 표의 속성을 요약해줌
df.describe() # 기술 통계를 요약해줌
df.columns # 열 이름을 보여줌

del df["Unnamed: 0"] # 난잡한 인덱스 정리
df.to_csv('today_youtube_crawling_data_deduplication.csv', mode='w',encoding='utf-8-sig')
