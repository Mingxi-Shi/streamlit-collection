# Done by Muench

import streamlit as st
import pdfplumber
import io
from pandas import DataFrame
import pandas as pd
import fitz
import streamlit.components.v1 as components


def convert_df(df):
    st.download_button(
        label="点我下载表格",
        data=df.to_csv().encode('gbk'),
        file_name='table.csv',
        mime='text/csv',
    )

def draw_table(df, theme, table_height):
    columns = df.columns
    thead1="""<thead><th scope="col"></th>"""
    thead_temp = []
    for k in range(len(list(columns))):
        thead_temp.append("""<th scope="col" class="text-white">"""+str(list(columns)[k])+"""</th>""")
    header = thead1+"".join(thead_temp)+"""</tr></thead>"""
    rows = []
    rows_temp = []
    for i in range(df.shape[0]):
        rows.append("""<th scope="row">"""+str(i+1)+"""</th>""")
        rows_temp.append(df.iloc[i].values.tolist())
    td_temp = []
    for j in range(len(rows_temp)):
        for m in range(len(rows_temp[j])):
            td_temp.append("""<td class="text-white">"""+str(rows_temp[j][m])+"""</td>""")
    td_temp2 = []
    for n in range(len(td_temp)):
        td_temp2.append(td_temp[n:n+df.shape[1]])
    td_temp3 = []
    for x in range(len(td_temp2)):
        if int(x % (df.shape[1])) == 0:
            td_temp3.append(td_temp2[x])
    td_temp4 = []
    for y in range(len(td_temp3)):
        td_temp4.append("".join(td_temp3[y]))
    td_temp5 = []
    for v in range(len(td_temp4)):
        td_temp5.append("""<tr><th scope="row" class="text-white">"""+str(v+1)+"""</th>"""+str(td_temp4[v])+"""</tr>""")
    table_html = """<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">"""+\
    """<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>"""+\
    """<table class="table text-center table-bordered """+str(theme)+'"'+">""" + \
    header+"""<tbody>"""+"".join(td_temp5)+"""</tbody></table>"""
    return components.html(table_html,height=table_height, scrolling=True)


def main():
    st.set_page_config(page_title="pdf_extract", page_icon="🌸", layout="wide")

    css = """<style>
    #MainMenu {visibility:hidden;}
    footer {visibility:hidden;}

    .stDownloadButton>button {
        background-color: #0099ff;
        color:#ffffff;
    }

    .stDownloadButton>button:hover {
        background-color: #00ff00;
        color:#ff0000;
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
    file = st.file_uploader("请上传PDF")
    if file is not None:
        doc = fitz.open(stream=file.read(), filetype="pdf")
        st.success("PDF基本信息:")
        st.write(pd.DataFrame(data=doc.metadata, index=["value"]))

        text = ""
        for page in doc:
            text += page.getText()
        st.success("PDF文字内容:")
        st.text_area("", text, height=300)

        st.success("PDF表格内容:")
        with pdfplumber.open(io.BufferedReader(file)) as p:
            for i in range(int(doc.page_count)):
                try:
                    page = p.pages[i]
                    table = page.extract_table()
                    if table is not None:
                        temp = {}
                        for j in range(len(table)):
                            temp[str(j)] = table[j]
                        df = DataFrame(temp)
                        df2 = pd.DataFrame(df.values.T, index=df.columns, columns=df.index)

                        def change_df(df):
                            arr = df.values
                            new_df = pd.DataFrame(arr[1:, 1:], index=arr[1:, 0], columns=arr[0, 1:])
                            new_df.index.name = arr[0, 0]
                            return draw_table(new_df.reset_index(), "bg-info", 200)

                        change_df(df2)
                        convert_df(df2)
                except ValueError:
                    pass
        doc.close()


if __name__ == '__main__':
    main()