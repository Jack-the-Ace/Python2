import streamlit as st
st.write('## NOTE2*')
st.caption('# 설명이나 주석**')
st.code('print("==="*30)', language='python')
st.latex(r'c=\sqrt{a^{2}+b^{2}}', width='content')
st.divider()
name= st.text_input('이름을 입력하세요.')
st.write(f'입력된 이름: {name}')
message= st.text_area('메시지를 입력하세요.')
st.write(f'입력된 메시지:  \n{message}')
st.divider()
color= st.color_picker('color',value='#00ff00')
st.write(f'선택한 색상: {color}')
if st.button('click'):
    st.write('button clicked')
from PIL import Image
image= Image.open("./media_files/storm.jpg")
st.image(image)
st.divider()
st.json({1:2,3:4,5:6})
st.metric(label='ABC' ,value='USD 30,000', delta='5.02%')

import matplotlib.pyplot as plt
import numpy as np
import time

# progress_bar= st.progress(0)
# for person in range(0,101,5):
#     time.sleep(0.1)
#     progress_bar.progress(person)
# with st.spinner('loading...'):
#     time.sleep(1)
# st.success('Complete!')
# st.balloons()
# st.sidebar.title('Title')

tab1, tab2, tab3= st.tabs(["1","2","3"])
tab1.write('tab1')
tab2.write('tab2')
tab3.write('tab3')
st.divider()
with tab1:
    st.header('tab1')
    st.image('https://static.streamlit.io/examples/cat.jpg')
with tab2:
    st.header('tab2')
    st.image('https://static.streamlit.io/examples/owl.jpg')
with tab3:
    st.header('tab3')
    st.image('https://static.streamlit.io/examples/dog.jpg')

with st.expander('more'):
    st.write('additional information can be here')

with st.expander("more info 'bout cat"):
    st.write("here is cat's information more")
    st.image('https://static.streamlit.io/examples/cat.jpg', width=250)


