#워크플로 (파이프라인 구축)
#사용자 질문(회사의 주가 정보) -> 1차 responses api -> 모델이 스스로 (일반답변 or 함수호출 선택)
#(만약. 함수호출을 선택했을 경우)     : 내 서버의 함수를 실행(주가정보 api) -> function_call_output 전송 -> 2차 responses api -> 최종답변 
#(만약. 함수호출이 필요하지 않을 경우) : 1차 responses api의 응답글씨를 출력

from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
client= OpenAI()


# 현재 주식가격 불러오기 yahoo finance 라이브러리(yfinance)를 사용하여 구현 가능
# 1차 모델에게 args로 company_name 을 전달받아 yahoo finance 모듈을 사용하여
# 주식티커의 현재 가격을 가져오는 함수
def get_current_stock_price(company_name):
    import yfinance as yf
    from yfinance import Search

    search= Search(company_name)
    ticker= None
    if len(search.quotes) >= 1:
        ticker= search.quotes[0]['symbol']
    print(ticker)

    if not ticker:
        return '해당 종목에 대한 정보가 없습니다.'

    stock= yf.Ticker(ticker=ticker)
    info= stock.info

    return info['regularMarketPrice']  #현재 주식가격 반환
#-------------------------------------------------------------------------------------------------------------------------------------

#1. 모델이 사용자 질문에 대응하기 위해 정보를 가져올 함수의 규격(명세서)을 정하기 [json schema]
tools= [
    {
        'type':'function',
        'name':'get_current_stock_price',
        'description':'파라미터로 받은 회사명의 ticker명을 구하여 주식의 현재 가격을 알려주는 함수',  #모델은 이 설명을 보고 언제 이 함수를 사용할지를 판단.
        'parameters':{
            'type':'object',
            'properties':{
                'company_name':{'type':'string', 'description':'주식 정보를 얻고싶은 회사명'}  #모델이 이 설명을 보고 추출할 args를 결정함
            },
            'required':['company_name'],
            'additionalProperties':False,  #False면 properties로 정의되지 않은 파라미터는 허용하지 않음.
        },
        'strict':True  # true면 이 명세서 규칙(json schema)를 엄격히 따르도록 함.
    },    
]

#2. 사용자의 질문에 함수호출이 필요한지 모델이 판단하도록 1차 responses api 요청
response= client.responses.create(
    model='gpt-4o-mini',
    #input='Samsung 의 현재 주가를 알려줘.',
    input='삼성의 현재 주가를 알려줘',  # 한글안됨 --  지침으로 해결 가능.
    #input= '하이닉스는 어때?',
    #input= '서울은 어느 나라 수도인가?',

    tools=tools,
    tool_choice='auto',

    #지침.- 프롬프트 엔지니어링
    instructions="""
    [역할]
    너는 주식 전문가야.

    [규칙]
    1. 사용자가 회사 또는 종목에 대해 주가를 물어보면 tools를 활용하여 회사의 현재 주식가격과 회사정보를 답변해줘.
    2. 사용자가 한글로 회사명을 입력하면 영문명으로 변경하여 함수에 전달해.
    3. 질문에 대한 답변을 간단하게 응답해.
    4. 한글기준 100글자 안에 대답해.
    """,
)

#3. 응답을 위해 함수 호출이 필요한지, or 그냥 응답이 가능한지 확인해보기
function_calls= [ item for item in response.output if item.type=='function_call' ]

#4. 함수호출 필요여부에 따라 분기처리
if function_calls:
    print('모델이 함수호출로 응답한다고 판단!!!')

    # 모델이 질문에서 추출한 함수에 필요한 파라미터값(회사명) 얻기
    import json
    args= json.loads(response.output[0].arguments)
    print(args)  # {'company_name':'Samsung'}

    # 개발자가 미리 정의한 함수를 호출하여 현재 주식가격 취득
    stock_price= get_current_stock_price(args['company_name'])
    print('함수 실행결과:', stock_price)

    #5. 함수의 실행결과(주식가격)을 2차 response api에 함수결과로서 전달하여 최종응답받기
    response= client.responses.create(
        model='gpt-4o-mini',
        previous_response_id= response.id,

        input=[
            {
                'type':'function_call_output',
                'call_id':response.output[0].call_id,
                'output':json.dumps(stock_price)
            }
        ]
    )

    #최종 응답 결과 출력
    print(response.output_text)

else:
    print('모델이 함수호출이 필요없다고 판단!!!')
    print(response.output_text)





















