# Done by Muench
import streamlit as st

from translate import Translator


def main():
    language_list = ["English", "Chinese", "Japanese", "Korean"]
    c_1 = st.selectbox(label="选择原翻译的语种", options=language_list)
    c_2 = st.selectbox(label="选择翻译后的语种", options=language_list, index=1)
    c_3 = st.text_input(label="输入要翻译的文本")
    # oe.tools.transtools(to_lang='Chinese', content='hello world')
    translator = Translator(from_lang=c_1, to_lang=c_2)
    translation = translator.translate(c_3)
    st.write(translation)


if __name__ == '__main__':
    main()