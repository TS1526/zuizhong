import streamlit as st
import data.data as dd
import model.model as mm

# 现在有一个需求：想将数据在多个页面之间进行传递
# streamlit为多页面应用提供了一个会话session缓存器，缓存器可以存储页面变量，然后在其他页面当中获取变量进行使用
# 会话存储的变量数据只在当前浏览器中有效，如果把浏览器关闭之后重新打开，那么会话缓存的数据会自动清理
# session会话变量的基本用法
# 存储数据 st.session_state.xxx = 值
# 获取数据 res = st.session_state.xxx
# 获取缓存的用户id和用户账号
user_id = st.session_state.user_id  # 用户id就是某一个用户的唯一标识
username = st.session_state.username
# f"字符串{变量名}"
st.title("AI智能助手✌")
st.subheader(f"欢迎{username}使用")
col,col1 = st.columns([8,2])
with col:
    st.text("这是一个AI助手，可以回答你的任何问题，请尽情使用吧！")
with col1:
    back = st.button("返回")
    if back:
        st.switch_page("pages/chatbot.py")

# 渲染私人助手界面的时候，应该查询当前用户的历史聊天记录，用于进行界面的渲染
list = dd.query_message_by_user_id(user_id=user_id)
if list:
    # {"message_id":xx,"user_id":xx,message:xxx,role:xxx,message_time:xxx"}
    for msg in list:
        with st.chat_message(msg["role"]):
            st.write(msg["message"])
else:
    # 如果当前用户和AI助手没有任何的聊天记录，需要给他一个默认的助手欢迎语
    with st.chat_message("assistant"):
        st.write("我是你的智能AI助手，可以回答你的任何问题，请问你有什么问题？")

# 创建一个聊天输入框 接受用户输入的问题
problem = st.chat_input("请输入你的问题")
if problem:
    with st.chat_message("user"):
        st.write(problem)
    dd.add_chat_message(user_id, problem, "user")
    res = mm.model_invoke(problem)
    with st.chat_message("assistant"):
        st.write(res)
    dd.add_chat_message(user_id, res, "assistant")
