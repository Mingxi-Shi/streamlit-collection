# done by Muench
# Creation Date: 2022/6/8 16:07
# -*- coding:utf-8 -*-

import streamlit as st
import hashlib


def main():
    st.set_page_config(page_title="文本加密", page_icon="🌸", layout="wide")

    sysmenu = '''
        <style>
        #MainMenu {visibility:hidden;}
        footer {visibility:hidden;}
        '''
    st.markdown(sysmenu, unsafe_allow_html=True)


    input_text = st.text_input(label='输入待加密文本')
    if st.button("加密"):
        st.write("md5: ", hashlib.md5(input_text.encode(encoding='UTF-8')).hexdigest())
        st.write("sha1: ", hashlib.sha1(input_text.encode(encoding='UTF-8')).hexdigest())
        st.write("sha256: ", hashlib.sha256(input_text.encode(encoding='UTF-8')).hexdigest())
        st.write("sha512: ", hashlib.sha512(input_text.encode(encoding='UTF-8')).hexdigest())


if __name__ == '__main__':
    main()