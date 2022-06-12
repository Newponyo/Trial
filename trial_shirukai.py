import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("民間移管を「知る会」のアンケート結果(2021.6.13)開催")

df = pd.read_csv("Results.csv", encoding='shift_jis')

st.dataframe(df)

shiba = df["園"][df["園"]=="芝"].count()
shiba_ob = df["園"][df["園"]=="芝（OB）"].count()
taishi = df["園"][df["園"]=="太子"].count()
taishi_ob = df["園"][df["園"]=="太子（OB）"].count()

member = np.array([shiba, shiba_ob, taishi, taishi_ob])


genre = st.radio(
     "何を表示させますか？？",
     ('参加者の構成', '学年', '民間移管への関心とその理由', "民間移管に対する気持ちとその理由", "民間移管の実情に対する理解", "行事について", "民間移管への関心の変化", "良かった点", "要改善点", "その他"))

if genre == '参加者の構成':

    fig, ax = plt.subplots()
    ax.bar(x=["SHIBA", "SHIBA_OB", "TAISHI", "TAISHI_OB"], height=member,
        color='green', width=0.6, alpha=0.6)
    st.subheader('参加者の構成')
    st.pyplot(fig)

else:
     st.write("未完成")















