import streamlit as st
import datetime
import talib
import tushare as ts
import pandas as pd



def main():

    ts.set_token('c39390bea3d991c5fb95742039636dd7ce191ec196e06a4767b4947e')
    pro = ts.pro_api()

    # data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    # data = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')

    stock_list = pro.query('stock_basic', exchange='', list_status='L', fields='symbol,name')
    stock_list.drop(labels=range(4938, 5099), axis=0, inplace=True)
    stock_list = stock_list.reset_index(drop=True)
    st.write(stock_list)
    # st.write(stock_list['symbol'][4938])

    # st日历选择开始和结束
    start_date = st.date_input(label="选择开始的日期", value=datetime.datetime.now() + datetime.timedelta(days=-datetime.datetime.now().weekday()))
    end_date = st.date_input("选择结束的日期", value=datetime.datetime.now() + datetime.timedelta(days=-datetime.datetime.now().weekday()+4))
    start_date = start_date.strftime('%Y-%m-%d')
    end_date = end_date.strftime('%Y-%m-%d')
    # 获取这个星期的数据
    # for i in range(len(stock_list['symbol'])-1):
    #     test = ts.get_hist_data(code=stock_list['symbol'][i], start=start_date, end=end_date)
    #     try:
    #         if (test['price_change'][-5:] > 0).all() or ((test['price_change'][-4:]<0).all() and test['price_change'][-1]>0):
    #             st.write(stock_list['symbol'][i])
    #
    #     except IndexError:
    #         pass
    #     except TypeError:
    #         pass

    # selected_stocks = []
    # for i in stock_list['symbol']:
    #     # 获取股票的历史K线数据
    #     df = ts.get_hist_data(code=i, start=start_date, end=end_date)
    #     try:
    #         # 计算股票的MACD指标
    #         df['ema12'] = df['close'].ewm(span=12, adjust=False).mean()
    #         df['ema26'] = df['close'].ewm(span=26, adjust=False).mean()
    #         df['diff'] = df['ema12'] - df['ema26']
    #         df['dea'] = df['diff'].ewm(span=9, adjust=False).mean()
    #         df['macd'] = 2 * (df['diff'] - df['dea'])
    #
    #         # 判断股票是否符合条件
    #         if (df['macd'][-5:] > 0).all() or ((df['macd'][-4:] < 0).all() and df['macd'][-1] > 0):
    #             selected_stocks.append(i)
    #     except IndexError:
    #         pass
    #     except TypeError:
    #         pass
    #
    # st.write(selected_stocks)

    # df = ts.get_hist_data(code='689009', start=start_date, end=end_date)
    # st.write(df)
    #
    # df['ema12'] = df['close'].ewm(span=12, adjust=False).mean()
    # df['ema26'] = df['close'].ewm(span=26, adjust=False).mean()
    # df['diff'] = df['ema12'] - df['ema26']
    # df['dea'] = df['diff'].ewm(span=9, adjust=False).mean()
    # df['macd'] = 2 * (df['diff'] - df['dea'])
    # st.write(df)

    # df2 = pro.stk_factor(ts_code='689009.SH', start_date=start_date, end_date=end_date, fields='ts_code,trade_date,macd')
    # df2 = ts.pro_bar(ts_code='689009.SH', adj='qfq', start_date=start_date, end_date=end_date)
    # st.write(df2)



    # df = ts.get_hist_data(code='689009', start=start_date, end=end_date)
    # # 初始化ema12、ema26、DIF和DEA值
    # ema12 = [df.iloc[0]['close']] * 12
    # ema26 = [df.iloc[0]['close']] * 26
    # dif = [0] * 25 + [df.iloc[0]['close']]
    # dea = [0] * 25 + [df.iloc[0]['close']]
    #
    # # 计算EMA和MACD指标
    # for i in range(25, len(df)):
    #     # 计算EMA
    #     ema12.append(ema12[-1] * 11 / 13 + df.iloc[i]['close'] * 2 / 13)
    #     ema26.append(ema26[-1] * 25 / 27 + df.iloc[i]['close'] * 2 / 27)
    #
    #     # 计算DIF
    #     dif.append(ema12[-1] - ema26[-1])
    #
    #     # 计算DEA
    #     dea.append(dea[-1] * 8 / 10 + dif[-1] * 2 / 10)
    #
    # # 计算MACD
    # macd = 2 * (dif - dea)
    #
    # # 将MACD值添加到dataframe中
    # df['macd'] = macd
    #
    # # 输出最后一天的MACD值
    # st.write(df.iloc[-1]['macd'])

    df = ts.get_hist_data(code='689009', start=start_date, end=end_date)
    st.write(df)
    macd, signal, hist = talib.MACD(df['close'], fastperiod=12, slowperiod=26, signalperiod=9)
    st.write(macd)




if __name__ == '__main__':
    main()