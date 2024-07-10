import streamlit as st
import base64

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
st.title("搭子选择页面")
if "xingge" not in st.session_state:
    st.session_state.xingge = ""
bt = st.button("吃饭搭子")
if bt:
    st.session_state.xingge="喜爱美食"
    st.switch_page("pages/aibot.py")
bt1 = st.button("游戏搭子")
if bt1:
    st.session_state.xingge="网瘾女孩"
    st.switch_page("pages/aibot.py")
bt2 = st.button("生活搭子")
if bt2:
    st.session_state.xingge="温柔可爱"
    st.switch_page("pages/aibot.py")