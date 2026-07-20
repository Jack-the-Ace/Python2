# pip install yfinance

import yfinance as yf

#주식종목명(회사명)을 ticker 티커라고 부름 (회사명에 부여된 명칭)
ticker= "AAPL"  # Apple Inc. 의 주식 티커 명칭
ticker= "005930.KS"  #한국 주식의 경우 KS or KQ 접미사 필요
stock= yf.Ticker(ticker=ticker)
print(stock)

info= stock.info
print('회사명:', info['longName'])
print('업종:', info['sector'])
print('사업요약:', info['longBusinessSummary'])
print('현재 주가:', info['regularMarketPrice'], 'USD')
print('='*100)

#회사명을 넣으면 주식 티커를 반환해주는 기능 사용!
from yfinance import Search
search= Search('Apple')
for q in search.quotes:
    print('ticker',q['symbol'])
print('-'*100)

from yfinance import Search
search= Search('삼성전자')  # 한글회사명은 검색안됨
for q in search.quotes:
    print('ticker',q['symbol'])
print('-'*100)

from yfinance import Search
search= Search('Samsung')  # 
for q in search.quotes:
    print('ticker',q['symbol'])
print('-'*100)

#과거 주가 데이터 조회 가능(결과를 표형태인 판다스의 DataFrameFrame으로 반환)
#history= stock.history(period='1d', interval='1h')
history= stock.history(period='5d', interval='1h')
print(history)

