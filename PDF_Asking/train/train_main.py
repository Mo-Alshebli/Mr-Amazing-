import os
import streamlit as st

from Data_train import My_own_gpt

models = [
    "gpt-3.5-turbo-16k-0613",
    "gpt-3.5-turbo",
    "text-davinci-003",
    "davinci",
    "babbage",
    "ada",
    "curie",
    "text-davinci-001",
    "ZeyadAhmed/AraElectra-Arabic-SQuADv2-QA",
]
# API="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"
API = "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"
api_key = "eb457224-95f8-4881-a32d-b28bcf8adb23"
env = "us-west4-gcp-free"
index_name = "chat"




def main():
    st.set_page_config(page_title="تدريب بياناتك  📝📗")
    st.header("ادخل البيانات  📝📗")
    pdf_docs = st.file_uploader(
        "Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
    if st.button("Process"):
        with st.spinner("Processing"):
            My_own_gpt(pdf_docs, models[0], API, api_key, env, index_name)
            st.text(" 🎩🏆تم التدريب بنجاح")



if __name__ == "__main__":
    main()
