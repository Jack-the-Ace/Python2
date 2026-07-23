import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

st.set_page_config(page_title="건설기술진흥법 AI 상담원", page_icon="🏗️")
st.title("🏗️ 건설기술진흥법 전문 AI Agent")

st.sidebar.header("⚙️ 모델 설정")
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.1, 0.1)
max_tokens = st.sidebar.number_input("Max Tokens", min_value=100, max_value=2000, value=500)

@st.cache_resource
def load_retriever():
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
    return vectorstore.as_retriever(search_kwargs={"k": 3})

retriever = load_retriever()

llm = ChatOpenAI(
    model="gpt-4o-mini", 
    temperature=temperature, 
    max_tokens=max_tokens
)

@tool
def search_construction_law(query: str) -> str:
    """건설기술진흥법 관련 법률 조항이나 규정을 검색할 때 사용합니다."""
        
    prompt = ChatPromptTemplate.from_messages([
        ("system", """당신은 토목 엔지니어링 현업에서 20년 이상 일해온 건설기술진흥법 전문 법률 AI 서포터입니다.
기본적으로는 아래 제공된 [법률 문서 내용]을 기반으로 사용자의 질문에 정확하고 명확하게 답변하는데,
[법률 문서 내용]에 정보가 없더라도 웹 검색을 통해 최대한 답변을 정확하고 명확하게 도출해냅니다.
법 조항이 있다면 제X조 X항 및 시행령 내용까지 언급하여 정확성을 높이세요. 
숫자 뒤에 .이 있는(예. 1.) 것이 '항' 입니다. (예. 1. = 1항)
특히, "https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EA%B1%B4%EC%84%A4%EA%B8%B0%EC%88%A0%EC%A7%84%ED%9D%A5%EB%B2%95" 이 사이트를 최우선으로 참고합니다.
제공된 정보에 내용이 없다면 '해당 내용은 제공된 건설기술진흥법 데이터에서 찾을 수 없습니다'라고 답변하세요.

[법률 문서 내용]:
{context}"""),
        ("human", "{question}")
    ])

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)
    
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    return rag_chain.invoke(query)

@tool
def calculate_safety_cost(direct_cost: float) -> str:
    """공사 직접비(원)를 입력받아 대략적인 안전관리비 추정액을 계산하는 도구입니다."""
    cost = direct_cost * 0.015
    return f"직접공사비 {direct_cost:,.0f}원 기준, 추정 안전관리비(약 1.5%)는 {cost:,.0f}원입니다."

tools = [search_construction_law, calculate_safety_cost]
tools_by_name = {tool.name: tool for tool in tools}
llm_with_tools = llm.bind_tools(tools)

def run_agent_workflow(user_input: str, history: list):
    
    system_prompt = ("system", """당신은 건설기술 진흥법 및 건설안전 관리 분야의 친절하고 정확한 AI 상담원입니다.
사용자의 질문 의도에 맞춰 알맞은 Tool을 사용하세요.
- 법률/조항 문의 -> search_construction_law 도구 사용
- 안전관리비 계산 문의 -> calculate_safety_cost 도구 사용""")
    
    messages = [system_prompt] + history + [("human", user_input)]
    
    response = llm_with_tools.invoke(messages)
    
    if response.tool_calls:
        tool_results = []
        for tool_call in response.tool_calls:
            selected_tool = tools_by_name[tool_call["name"]]
            tool_output = selected_tool.invoke(tool_call["args"])
            tool_results.append(tool_output)
        
        final_prompt = f"사용자 질문: {user_input}\n\n도구 실행 결과: {tool_results}\n위 결과를 바탕으로 친절하고 완성된 답변을 작성해주세요."
        final_response = llm.invoke([system_prompt, ("human", final_prompt)])
        return final_response.content
    else:
        return response.content

# =======================================================================================================================================
# 6. Streamlit UI

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt_text := st.chat_input("건설기술진흥법에 대해 궁금한 점을 물어보세요!"):
    st.session_state.messages.append({"role": "user", "content": prompt_text})
    st.chat_message("user").write(prompt_text)

    with st.chat_message("assistant"):
        with st.spinner("법령 및 데이터 처리 중..."):
            
            chat_history = []
            for m in st.session_state.messages[:-1]:
                chat_history.append((m["role"], m["content"]))

            output_text = run_agent_workflow(prompt_text, chat_history)
            st.write(output_text)
            
            st.session_state.messages.append({"role": "assistant", "content": output_text})