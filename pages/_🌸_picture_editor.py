# done by Muench
# Creation Date: 2022/6/9 16:10
# -*- coding:utf-8 -*-
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from streamlit_cropper import st_cropper


def main():
    st.set_page_config(page_title="图片编辑器", page_icon="🌸", layout="wide")

    sysmenu = '''
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility:hidden;}
            '''
    st.markdown(sysmenu, unsafe_allow_html=True)

    img_file = st.sidebar.file_uploader(label='上传图片', type=['png', 'jpg'])
    realtime_update = st.sidebar.checkbox(label="Update in Real Time", value=True)
    aspect_choice = st.sidebar.radio(label="纵横比", options=["1:1", "16:9", "4:3", "2:3", "自定义"])
    aspect_dict = {
        "1:1": (1, 1),
        "16:9": (16, 9),
        "4:3": (4, 3),
        "2:3": (2, 3),
        "自定义": None
    }
    aspect_ratio = aspect_dict[aspect_choice]

    if img_file:
        img = Image.open(img_file)

        if not realtime_update:
            st.write("Double click to save crop")
        # Get a cropped image from the frontend
        cropped_img = st_cropper(
            img,
            realtime_update=realtime_update,
            aspect_ratio=aspect_ratio,
            return_type='image'
        )

        # Manipulate cropped image at will
        st.write("Preview")
        _ = cropped_img.thumbnail((150, 150))
        st.image(cropped_img)


if __name__ == '__main__':
    main()