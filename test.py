
#import plotly.graph_objects as go
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np
import matplotlib.dates as mdates
import numpy as np
import time

# st.code("""
# [theme]
# primaryColor="#F39C12"
# backgroundColor="#81F7D8"
# # secondaryBackgroundColor="#AED6F1"
# # textColor="#FFFFFF"
# # font="monospace"
# """)


# if user_name != '':
#   st.write(f'👋 안녕하세요 {user_name}님!')
# else:
#   st.write('👈  **이름**을 입력해 주세요!')

# my_bar = st.progress(0)
# for percent_complete in range(100):
#      time.sleep(0.05)
#      my_bar.progress(percent_complete + 1)

# st.balloons()

# st.title('this is title')
# st.header('this is header')
# st.subheader('this is subheader'


# 현재 날짜 가져오기
today = datetime.today()

# 날짜를 문자열로 변환하여 포매팅
formatted_date = today.strftime("%Y-%m-%d")

# Streamlit Markdown에 날짜 추가
st.title("코인예측 시뮬레이션 데시보드")
st.markdown(f'### 1. 코인 추천랭킹, 예측날짜: {formatted_date} 9시 기준')
# 사이드바에 select box를 활용하여 종을 선택한 다음 그에 해당하는 행만 추출하여 데이터프레임을 만들고자합니다.
st.sidebar.title("Coin Chart")
st.sidebar.markdown('비트/알트코인 Link : [All Coin Symbols](https://upbit.com/exchange?code=CRIX.UPBIT.KRW-BTC)')
st.sidebar.markdown('코스피200 Link : [All Kospi200 Symbols](https://finance.naver.com/sise/sise_index.nhn?code=KPI200)')
st.sidebar.markdown('나스닥200 Link : [All Nasdaq200 Symbols](https://kr.investing.com/indices/nq-100-components)')
