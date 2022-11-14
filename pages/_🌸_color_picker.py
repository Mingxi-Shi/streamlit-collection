# done by Muench
# Creation Date: 2022/6/6 16:44
# -*- coding:utf-8 -*-

import streamlit as st


def hex_to_rgb(hex_color):

    r = int('0x' + hex_color[1:3], 16)
    g = int('0x' + hex_color[3:5], 16)
    b = int('0x' + hex_color[5:7], 16)
    rgb_color = str(r) + ',' + str(g) + ',' + str(b)
    return rgb_color


def main():
    st.set_page_config(page_title="取色器", page_icon="🌸", layout="wide")

    sysmenu = '''
        <style>
        #MainMenu {visibility:hidden;}
        footer {visibility:hidden;}
        '''
    st.markdown(sysmenu, unsafe_allow_html=True)

    color_picked = st.color_picker('选取一种颜色', '#000000')
    st.write('当前的hex颜色是 ', color_picked)
    st.write('当前的rgb颜色是 ', hex_to_rgb(color_picked))


if __name__ == '__main__':
    main()
