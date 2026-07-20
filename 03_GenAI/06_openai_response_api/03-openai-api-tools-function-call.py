#함수호출도구 사용의 워크플로(파이프라인)
#사용자 질문 -> 1차. Response API -> 모델이 스스로(일반 답변 or function_call 선택)
#(만약. 함수호출을 선택했을 경우) : -> 내가 만든 함수 실행 -> 실행결과를 function_call_output 전송 -> 2차. response api -> 최종답변
#(만약. 함수호출이 필요 없다면)  : -> 1차 응답결과를 출력

from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client= OpenAI()

#1. 답변에 사용할 도구 설정 : 함수호출. 도구로 사용할 함수의 구조를 미리 설계(모델에게 알려줄 함수의 명세서 JSON Schema)
tools= [
    {
        "type":"function",
        "name":"get_weather",
        "description":"현재 날씨를 조회한다.",
        "parameters":{
            "type":"object", #파라미터가 여러개일 수 있어서.. 객체로
            "properties":{
                "city":{
                    "type":"string",
                    "description":"도시 이름"
                }
            },
            "required":["city"]
        }
    }
]

#2. 사용자의 질문에 함수호출이 필요한지 모델이 판단하도록 1차 responses api 요청
response= client.responses.create(
    model='gpt-4o-mini',
    #(1) 함수호출이 필요할만한 질문
    #input='현재 서울 날씨 알려줘.',
    #(2) 함수 호출이 필요없는 질문
    input='서울은 어느나라의 수도인가?',

    tools= tools, #도구 지정
    tool_choice='auto'  # 모델이 알아서 도구 사용 여부를 결정 -- default
)
# 응답결과 출력
print(response)
print()
# 만약, 모델이 함수를 호출해야 한다고 판단하면 JSON 구조로 응답함.
print(response.output)
print()

#3. 모델의 args로 city를 전달받아. 날씨 api를 이용하여 해당 지역의 날씨 정보를 
#  json으로 응답해주는 함수.... 즉, 도구로 사용될 함수 정의
def get_weather(city):
    # 실제호는 여기서 해당 city의 기상청 날씨 open api로 데이터를 가져와서 리턴함.
    return {"city":city, "temperature":31, "condition":"맑음"}

#4. 최종응답을 위해 함수 호출이 필요한지, 그냥 응답이 가능한지 확인하기
# 모델이 함수호출이 필요하다고 느꼈을때... 의 함수항목들을 저장하는 리스트(여러개일 수도 있어서)
# 리스트 컴프리헨션 문법 : 응답 도구 중 '함수호출'인 것들만 추출
function_calls= [ item for item in response.output if item.type=='function_call' ]

if function_calls:  #함수 호출이 필요하다고 판단된 경우
    print('모델이 함수호출로 응답해야 한다고 판단!!')

    # 여러 함수가 필요하다고 판단했을 수도 있기에..
    for call in function_calls:
        print('함수 이름:', call.name)
        print('함수호출 식별ID:', call.call_id)
        print('모델이 선별한 함수의 파라미터들:', call.arguments)

    # 모델이 인식하기 편하도록.. response.output[0] 의 arguments결과는 json이어서 이를 dict로 변환하여 사용
    import json
    call= response.output[0]
    args= json.loads(call.arguments)  # "{'city':'서울'}" --> {'city':'서울'}

    #함수를 직접호출하여 날씨 결과를 얻기
    weather= get_weather(args['city'])  # '서울'을 전달하고 함수의 결과 받기
    print('함수 실행결과 확인:', weather)

    #4. 함수 실행결과(weather)를 2차 responses api에 전달하여 최종 응답 받기
    response= client.responses.create(
        model='gpt-4o-mini',
        previous_response_id=response.id,  # 이전 1차 응답을 참조하도록..

        #사용자의 질문은 1차에서 이미 완료되었고..
        #함수호출의 결과를 2차에게 제공하여 최종 응답하도록
        input=[
            {
                "type":"function_call_output",
                "call_id":call.call_id,
                "output":json.dumps(weather)   #dict --> ai model은 json형식을 선호(변환)
            }
        ]
    )
    # 최종 응답 결과 출력
    print()
    print(response.output_text)


else:   #함수 호출이 필요하지 않다고 느꼈다면.. 1차 응답결과로 글씨가 나옴.
    print('함수 호출 도구 없이 일반 응답으로 처리 가능하다고 판단!!')
    print(response.output_text)




















