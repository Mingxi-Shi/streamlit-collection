# Done by Muench

import  streamlit as st


def main():

    st.set_page_config(page_title="进制转换", page_icon="🌸", layout="wide")

    sysmenu = '''
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility:hidden;}
            '''
    st.markdown(sysmenu, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns([1, 1, 1, 1], gap='large')
    with col1:
        bin_num = st.text_input(label="二进制转换", value=1010)
        st.write("八进制：", oct(eval('0b' + bin_num))[2:])
        # st.write("十进制：", eval('0b' + bin_num))
        st.write("十进制：", int(bin_num, 2))
        st.write("十六进制：", hex(eval('0b' + bin_num))[2:])

    with col2:
        oct_num = st.text_input(label="八进制转换", value=12)
        st.write("二进制：",  bin(int(oct_num, 8))[2:])
        st.write("十进制：", int(oct_num, 8))
        st.write("十六进制：", hex(eval('0o'+oct_num))[2:])

    with col3:
        int_num = st.text_input(label='十进制转换', value=10)
        st.write("二进制：", bin(int(int_num))[2:])
        st.write("八进制：", oct(int(int_num))[2:])
        st.write("十六进制：", hex(int(int_num))[2:])

    with col4:
        hex_num = st.text_input(label="十六进制转换", value='a')
        st.write("二进制：", bin(int(hex_num, 16))[2:])
        st.write("八进制：", oct(int(hex_num, 16))[2:])
        st.write("十进制：", int(hex_num, 16))


if __name__ == '__main__':
    main()