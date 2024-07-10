import streamlit as st
import model.model as mm
import base64
# 全新的AI助手，专用负责翻译
def main_bg(main_bg):
    main_bg_ext = "png"
    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )
main_bg("images/OIP-C1.jpg")
user_id = st.session_state.user_id  # 用户id就是某一个用户的唯一标识
username = st.session_state.username

# streamlit的session_state缓存器进行处理 新数据覆盖旧数据的问题
if "messages" not in st.session_state:
    # 缓存的数据以字典类型的数组来缓存
    # [{"role":user,context:xxx},{}]
    st.session_state.messages = []

# 需要从缓存中获取数据进行界面的渲染
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["context"])

if len(st.session_state.messages) <=0 :
    with st.chat_message("assistant"):
        st.write("你好，我是你的专属地理助手，可以回答你的任何的地理问题")

input = st.chat_input("请输入你要咨询的地理问题")
if input:
    with st.chat_message("user"):
        st.write(input)
    st.session_state.messages.append({"role":"user","context":input})
    result = mm.chain_invoke({"context":input})
    with st.chat_message("assistant"):
        st.write(result)
    st.session_state.messages.append({"role": "assistant", "context": result})