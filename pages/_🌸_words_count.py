# done by Muench
# Creation Date: 2022/6/9 9:21
# -*- coding:utf-8 -*-

import streamlit as st


def main():
    st.set_page_config(page_title="中英文字数统计", page_icon="🌸", layout="wide")

    sysmenu = '''
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility:hidden;}
            '''
    st.markdown(sysmenu, unsafe_allow_html=True)

    input_chinese_text = st.text_area(label="输入中文文本")
    chinese_words_number = len(input_chinese_text)
    if input_chinese_text:
        st.write('中文字数为(包括标点符号): ', chinese_words_number)

    input_english_text = st.text_area(label="输入英文文本")
    english_words_number = len(input_english_text.split(" "))
    if input_english_text:
        st.write('英文单词数为(不包括标点符号): ', english_words_number)



if __name__ == '__main__':
    main()