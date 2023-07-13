from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder
)
import streamlit as st
from streamlit_chat import message
from utils import *

model = ["gpt-3.5-turbo",
         "gpt-3.5-turbo-16k-0613",

         ]
st.subheader("روبوت محادثة اعتماد على بيانات سابق باستحدام تقنية الذكاء الاصطناعي")

if 'responses' not in st.session_state:
    st.session_state['responses'] = ["مرحبا كيف يمكنني مساعدتك ؟"]

if 'requests' not in st.session_state:
    st.session_state['requests'] = []

llm = ChatOpenAI(model_name=model[0],
                 openai_api_key="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")

if 'buffer_memory' not in st.session_state:
    st.session_state.buffer_memory = ConversationBufferWindowMemory(k=3, return_messages=True)

system_msg_template = SystemMessagePromptTemplate.from_template(template="""أجب على السؤال بأكبر قدر ممكن من الصدق 
باستخدام السياق المتوفر ، وأريد الإجابة كلها باللغة العربية وإذا لم تكن الإجابة موجودة في النص أدناه ، قل "لا أعرف 
واذا تم سؤال من انت قول انا روبوت دردشة معتمد على بيانات سابقة تم تدريبي عليها  "'""")

human_msg_template = HumanMessagePromptTemplate.from_template(template="{input}")

prompt_template = ChatPromptTemplate.from_messages \
        (
        [
            system_msg_template,
            MessagesPlaceholder(variable_name="history"),
            human_msg_template
        ]
    )

conversation = ConversationChain(memory=st.session_state.buffer_memory, prompt=prompt_template, llm=llm, verbose=True)

# container for chat history
response_container = st.container()
# container for text box
textcontainer = st.container()

with textcontainer:
    query = st.text_input("Query: ", key="input")
    if st.button("Process"):
        if query:
            with st.spinner("typing..."):
                conversation_string = get_conversation_string()
                # refined_query = query_refiner(conversation_string, query,model[0])
                # st.subheader("Refined Query:")
                # st.write(refined_query)
                context = find_match(query, model[0])
                response = conversation.predict(input=f"Context:\n {context} \n\n Query:\n{query}")
            st.session_state.requests.append(query)
            st.session_state.responses.append(response)
with response_container:
    if st.session_state['responses']:

        for i in range(len(st.session_state['responses'])):
            message(st.session_state['responses'][i], is_user=True, key=str(i))
            if i < len(st.session_state['requests']):
                message(st.session_state["requests"][i], key=str(i) + '_user')
