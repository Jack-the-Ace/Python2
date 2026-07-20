# openai api의 tools 다루기 - 사이트의 가이드문서 참고

from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client= OpenAI()

#response api 호출
response= client.responses.create(
    model='gpt-4o-mini',
    instructions='질문에 대한 답변을 간단하게 응답해. 한글 기준 100글자 안에 뭐든 대답해. 현재 시점에 대한 질문이 있다면 tools를 사용한 결과를 먼저 보여주고. 답변을 보여줘.',
    #input='대한민국의 지금 대통령이 누구야?',
    input='국제규격의 축구장 크기는 몇 cm야?',
    max_output_tokens=5000,
    #도구 연결 - 응답에 참고할 도구를 지정
    tools= [
        #1) 웹 검색 도구 사용
        #{'type':'web_search'},
        #2) 파일 검색 도구 사용 (문서를 vector db에 저장하고 검색하여 답변하는 RAG시스템)
        {'type':'file_search', 'vector_store_ids':['vs_6a5d7cac5798819180ab3792e5cbceb3']},
        # openai api 플랫폼 사이트에 문서를 업로드 하여 클라우드 환경의 RAG 구축가능
        # vector 는 하루마다 보관료 비용이 지불됨. (실습 후 삭제!!)
    ],
    # 웹검색 도구를 지정했다고 무조건 사용하지 않음. 도구를 사용할지 여부를 llm이 판단함
    # 판단에 대한 기준을 설정!
    #tool_choice='required',  #답변시 무조건 도구를 사용해라! (권장하지 않음.)
    # 웹검색이 필요없어도 무조건 웹검색 사용하며 토큰을 소진함!
    tool_choice='auto'  # default 이면서, 권장된다 -- 대신 지침으로 도구 사용 유도.
)

#응답결과 출력
print(response.output_text)
print('='*100)
print(response)  # 토큰 사용량 등 메타데이터까지 출력. 여러 속성들.




















