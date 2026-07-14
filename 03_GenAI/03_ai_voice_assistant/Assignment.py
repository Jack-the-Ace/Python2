from openai import OpenAI
from pathlib import Path
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
client= OpenAI()

import os
import io
import base64
from PIL import Image

def desc(image_data):
    #url='https://cdn.pixabay.com/photo/2017/06/12/01/53/zombie-2394124_1280.jpg'
    response= client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[{"role":"user",
                   "content":[
                       {"type":"text","text":"이 이미지에 대해서 임팩트 있지만 간결하게 묘사해줘"},
                       {"type":"image_url","image_url":{"url":image_data}}
                    ]
                }],
        max_tokens=1200
    )
    return response.choices[0].message.content

def TTS(response):
    with client.audio.speech.with_streaming_response.create(
        model='gpt-4o-mini-tts',
        voice='onyx',
        input=response
    ) as response:
        filename="output.mp3"
        response.stream_to_file(filename)

    with open(filename, "rb") as f:
        data= f.read()
        b64= base64.b64encode(data).decode()
        md= f"""
            <audio autoplay="True">
                <source src= "data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)
    os.remove(filename)

def main():
    st.image('https://cdn.pixabay.com/photo/2017/06/12/01/53/zombie-2394124_1280.jpg', width=200)
    st.title("이미지를 해설해드립니다.")
    img_file_buffer= st.file_uploader('Upload a PNG image', type='png')
    if img_file_buffer is not None:
        image=Image.open(img_file_buffer)
        st.image(image, caption='Uploaded Image.', use_container_width=True)
        
        buffered= io.BytesIO()
        image.save(buffered, format='PNG')
        img_base64= base64.b64encode(buffered.getvalue())
        img_base64_str= img_base64.decode('utf-8')
        image= f"data:image/jpeg;base64,{img_base64_str}"

        text= desc(image)
        st.info(text)
        TTS(text)

if __name__ == "__main__":
    main()