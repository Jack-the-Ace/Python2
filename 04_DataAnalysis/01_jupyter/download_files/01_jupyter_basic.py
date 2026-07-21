#!/usr/bin/env python
# coding: utf-8

# In[1]:


#주피터 노트북: 파이썬 쉘 환경 + 코드 파일 작성을 동시에 수행하고 코드와 실행결과를 하나의 파일에 저장할 수 있는 웹 기반 개발환경
#파일확장자 .ipynb 

#코드를 작성할 수 있는 이 박스를 cell 이라고 부름.

print('Hello jupyter notebook')


# In[2]:


name= 'sam'
print(name)


# In[3]:


100


# In[4]:


50+30


# In[5]:


# cell 실행모드 3가지
print('Hello')


# In[6]:


print('Hello')


# In[7]:


num=100


# In[8]:


num+=50


# In[9]:


print(num)


# In[11]:


# 에러 발생위치 확인
name='robin'
print(name)
print(nice to meet you)


# In[81]:


import random
num= random.randint(1,46)
print(num)


# In[92]:


get_ipython().run_line_magic('pinfo', 'random.randint')


# In[87]:


#[]안에 숫자가 있어야 실행완료.. 혹시 * 이면 실행중
import time
for i in range(10):
    print(i)
    time.sleep(0.5)


# In[88]:


#주피터 노트북의 장점 - 설명을 작성하기 위한 cell을 만들 수 있음.
#코드 cell이 아닌 마크다운문법을 사용할 수 있는 설명 cell을 사용해보기


# 마크다운 문법을 작성할 수 있어요. 실행은 코드처럼 ctrl + Enter 로 실행하면 마크다운을 랜더링한 결과 화면이 보여짐.
# 마크다운 문법이기에 엔터를 친다고 줄바꿈 되지 않음. 줄바꿈 하려면 br태그같은 역할의 문법.
# 띄어쓰기 두번  
# 이렇게...
# 
# 
# 마크다운 언어의 제목요소 표시 h1~h6를 대체.. #의 개수로 (띄어쓰기 있어야 함)  
# # 제목1
# ## 제목2
# ### 제목3
# #### 제목4
# ##### 제목5
# ###### 제목6
# ####### 제목7은 없음.
# 
# **bold** 또는 __bold__ 를 통해 strong(강하게) 표시 가능  
# *italic* 또는 _italic_ 를 통해 emphasize(강조) 표시 가능  
# ***bold and italic*** 또는 ___bold and italic___ 를 통해 bold + italic 표시 가능  

# >인용구를 만들수도 있음  
# >인용구도 공백문자 2개가 있어야 줄바꿈 됨.    
# >이렇게
# 
# ---
# 
# ### unordered list
# - 리스트1
# - 리스트2
# - 리스트3
# 
# ### ordered list
# 1. aaa
# 2. bbb
# 3. ccc
# 
# 순서가 있는 리스트는 모두 1을 써도 자동 증가됨
# 1. aaa
# 1. bbb
# 4. ccc
# 
# ***

# ## 이미지 표시
# - windows 에서 print screen 으로 이미지 캡쳐하여 붙여넣기 하면 이미지가 표시됨
#  ![image.png](attachment:046118eb-e4b8-44e2-91b1-31a841d500c9.png)
# 
# - 특정 이미지의 경로를 직접 지정 (스타일지정 {  }는 GitHub에서는 인식되고, 주피터노트북에서는 안됨)
#     ![computer](./computer.png){: width="100" height="100"}
# 
# - 크기 지정을 하려면 마크업언어 사용
# <img src="./computer.png" alt="computer" width="100">

# ## 마크다운 링크(anchor) 요소
# 
# [네이버](https://www.naver.com)
# 
# ---
# 
# ## 유튜브 영상 링크
# 유튜브 동영상에 마우스 우클릭하여 **소스코드 복사**를 누르고 cell에 붙여넣기
# <iframe width="1337" height="752" src="https://www.youtube.com/embed/UkFLk0-xf58" title="[MV] 헌트릭스(HUNTR/X) - Golden l 한글자막 뮤직비디오" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
# 
# iframe의 사용은 코드 cell 에서 %%html 을 입력한 다음 붙여넣기 해야 함.

# In[95]:


get_ipython().run_cell_magic('html', '', '<iframe width="400" height="400" src="https://www.youtube.com/embed/UkFLk0-xf58" title="[MV] 헌트릭스(HUNTR/X) - Golden l 한글자막 뮤직비디오" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>\n')


# In[96]:


# 노트북 파일 .ipynb 파일을 다른 형태로 변환하여 추출 및 다운로드 가능.

#1. html 파일로 다운로드 (파이썬 개발환경이 없는 곳에서 코드와 실행결과 확인가능)
#2. pdf 파일로 다운로드 (파이썬 개발환경이 없는 곳에서 코드와 실행결과 확인가능)
#3. .py 파일로 다운로드 (코드가 아닌 cell들은 모두 주석처리됨)

