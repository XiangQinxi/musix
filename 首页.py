import streamlit as st

st.set_page_config(
    page_title="Musix",
    page_icon="🎶",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items=None
)

st.header("Musix")

st.text("免费搜索下载音乐（基于cloudmusic）")

with st.expander("源代码-首页"):
    st.code(open("首页.py", "r", encoding="utf-8").read(), line_numbers=4)

with st.expander("源代码-搜索歌曲"):
    st.code(open("pages/搜索歌曲.py", "r", encoding="utf-8").read(), line_numbers=4)

with st.expander("源代码-配置"):
    st.code(open(".streamlit/config.toml", "r", encoding="utf-8").read(), line_numbers=4)