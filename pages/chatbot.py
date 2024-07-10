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
main_bg("images/R-C.jpg")
st.title('AI应用产品网🙂')

col,col1,col2 = st.columns(3)
with col:
    st.image("images/XB-AI.jpg")
    bt = st.button("小白助手")
    if bt:
        st.switch_page("pages/xiaobaibot.py")
with col1:
    st.image("images/FY-AI.jpg")
    bt1 = st.button("翻译助手")
    if bt1:
        st.switch_page("pages/dfswbot.py")
with col2:
    st.image("images/DZ-AI.jpg")
    bt2 = st.button("电子搭子")
    if bt2:
        st.switch_page("pages/friend.py")