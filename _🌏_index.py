# done by Muench
# Creation Date: 2022/6/6 16:44
# -*- coding:utf-8 -*-

import streamlit as st


def main():
    st.set_page_config(page_title="工具合集", page_icon="🌏", layout="wide")

    sysmenu = '''
    <style>
    #MainMenu {visibility:hidden;}
    footer {visibility:hidden;}
    '''
    st.markdown(sysmenu, unsafe_allow_html=True)
    st.write(1111111)


if __name__ == '__main__':
    main()