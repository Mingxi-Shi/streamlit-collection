# done by Muench
# Creation Date: 2022/6/10 10:22
# -*- coding:utf-8 -*-

import streamlit as st

import io



def main():
    st.set_page_config(page_title="测试", page_icon=":eyes:", layout="wide")

    sysmenu = '''
        <style>
        #MainMenu {visibility:hidden;}
        footer {visibility:hidden;}
        '''
    st.markdown(sysmenu, unsafe_allow_html=True)
    st.write(":eyes:")
    st.write("😀")
    st.write("🌲")
    "♌"



if __name__ == '__main__':
    main()