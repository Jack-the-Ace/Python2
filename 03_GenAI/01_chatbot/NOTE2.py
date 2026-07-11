from google import genai
client= genai.Client(api_key='키입력하기')

def get_weather():
    import requests
    weather= requests.get('기상청 open api json')
    return weather

from google.genai import types
config= types.GenerateContentConfig(
    max_output_tokens= 2000,
    response_mime_type= 'text/plain',
    system_instruction= '필요한 말만 간결하게 하고 끝.',
    tools= [get_weather]
)
response= client.models.generate_content(
    model='gemini-3.5-flash',
    contents= '위가 건강하게 사는 방법',
    config=config
)
print(response.text)