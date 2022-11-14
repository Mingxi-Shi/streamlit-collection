# Done by Muench

import streamlit as st
from streamlit_tree_select import  tree_select


def main():
    st.set_page_config(page_title="多选树测试", page_icon="🌸", layout="wide")

    sysmenu = '''
                <style>
                #MainMenu {visibility:hidden;}
                footer {visibility:hidden;}
                '''
    st.markdown(sysmenu, unsafe_allow_html=True)
    nodes = [
        {"label": "北京", "value": "北京"},
        {
            "label": "上海",
            "value": "上海",
            "children": [
                {"label": "浦东", "value": "浦东"},
                {"label": "杨浦", "value": "杨浦"},
                {"label": "虹口", "value": "虹口"},
                {"label": "黄浦", "value": "黄浦"},
            ],
        },
        {
            "label": "广州",
            "value": "广州",
            "children": [
                {"label": "番禺区", "value": "番禺区"},
                {
                    "label": "白云区",
                    "value": "白云区",
                    "children": [
                        {"label": "三元里街", "value": "三元里街"},
                        {"label": "松洲街", "value": "松洲街"},
                    ],
                },
                {"label": "珠江新区", "value": "珠江新区"},
            ],
        },
    ]

    return_select = tree_select(nodes)
    st.json(return_select["checked"])
    st.image('./img/multiselect-tree-1.png')
    st.image('./img/multiselect-tree-2.png')


if __name__ == '__main__':
    main()