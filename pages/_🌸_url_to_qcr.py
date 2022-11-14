# Done by Muench

import streamlit as st
import office as oe
from PIL import Image
import qrcode

def main():
    st.set_page_config(page_title="链接转二维码", page_icon="📘", layout="wide")

    sysmenu = '''
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility:hidden;}
            '''
    st.markdown(sysmenu, unsafe_allow_html=True)

    b = st.text_input(label='输入链接生成二维码')
    # b = oe.tools.qrcodetools(url=url)
    if b:
        qr = qrcode.QRCode(version=1, box_size=5, border=2)
        qr.add_data(b)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        st.image(img.get_image())


if __name__ == '__main__':
    main()