import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("民間移管を「知る会」のアンケート結果")

st.write("これは、2021/06/13に開催された、民間移管を「知る会」のアンケート結果をまとめたものです。")
st.write("情報が特定されないように、個人名や園名は伏せてあります。")

df = pd.read_csv("Results.csv", encoding='shift_jis')

st.dataframe(df)

# 保育園
shiba = df["保育園"][df["保育園"]=="A保育園"].count()
shiba_ob = df["保育園"][df["保育園"]=="A保育園（OB）"].count()
taishi = df["保育園"][df["保育園"]=="B保育園"].count()
taishi_ob = df["保育園"][df["保育園"]=="B保育園（OB）"].count()

member = np.array([shiba, shiba_ob, taishi, taishi_ob])

# 学年
zero_one = df["学年"][df["学年"]=="0-1歳児"].count()
two = df["学年"][df["学年"]=="2歳児"].count()
three = df["学年"][df["学年"]=="3歳児"].count()
four = df["学年"][df["学年"]=="4歳児"].count()
five = df["学年"][df["学年"]=="5歳児"].count()
ob = df["学年"][df["学年"]=="OB"].count()

grade = np.array([zero_one, two, three, four, five, ob])

# 民間移管への関心
concern_a = df["民間移管への関心"][df["民間移管への関心"]=="とても関心がある"].count()
concern_b = df["民間移管への関心"][df["民間移管への関心"]=="関心がある"].count()
concern_c = df["民間移管への関心"][df["民間移管への関心"]=="あまり関心がない"].count()

concern = np.array([concern_a, concern_b, concern_c])

# 民間移管に対する気持ち
feeling_a = df["民間移管に対する気持ち"][df["民間移管に対する気持ち"]=="とても不安を感じている"].count()
feeling_b = df["民間移管に対する気持ち"][df["民間移管に対する気持ち"]=="不安を感じている"].count()
feeling_c = df["民間移管に対する気持ち"][df["民間移管に対する気持ち"]=="あまり不安を感じていない"].count()

feeling = np.array([feeling_a, feeling_b, feeling_c])


# 民間移管への関心の変化
change_a = df["民間移管への関心の変化"][df["民間移管への関心の変化"]=="とても関心が高まった"].count()
change_b = df["民間移管への関心の変化"][df["民間移管への関心の変化"]=="関心が高まった"].count()
change_c = df["民間移管への関心の変化"][df["民間移管への関心の変化"]=="全く変わらない"].count()

change = np.array([change_a, change_b, change_c])


#保育園	学年	民間移管への関心	民間移管への関心の理由	民間移管に対する気持ち	民間移管に対する気持ちとその理由	民間移管の実情への理解	A保育園の行事の内容1	A保育園の行事の内容2	民間移管への関心の変化	良かった点	要改善点	民間移管の実情を共有することは有益か？？	その他

option = st.selectbox(
     '何を表示させますか？？',
     ('参加者の構成', '学年', '民間移管への関心とその理由', "民間移管に対する気持ちとその理由", "民間移管の実情に対する理解", "行事について", "民間移管への関心の変化", "良かった点", "要改善点", "民間移管の実情を共有することは有益か？？", "その他"))

# st.write('選択されたもの:', option)


if option == '参加者の構成':

    fig, ax = plt.subplots()
    ax.bar(x=["A", "A_OB", "B", "B_OB"], height=member,
        color='green', width=0.6, alpha=0.6)
    st.subheader('参加者の構成')
    st.pyplot(fig)

elif option == '学年':

    fig, ax = plt.subplots()
    ax.bar(x=["0-1year", "2years", "3years", "4years", "5years", "OB"], height=grade,
        color='blue', width=0.6, alpha=0.6)
    st.subheader('学年')
    st.pyplot(fig)

elif option == '民間移管への関心とその理由':

    fig, ax = plt.subplots()
    ax.bar(x=["High Concern", "Concern", "Less Concern"], height=concern,
        color='blue', width=0.6, alpha=0.6)
    st.subheader('民間移管への関心')
    st.pyplot(fig)

    for reason in range(0, len(df["民間移管への関心の理由"])):
        if df["民間移管への関心の理由"][reason] is np.nan:
            pass
        else:
            st.write(df['民間移管への関心の理由'][reason])

elif option == '民間移管に対する気持ちとその理由':

    fig, ax = plt.subplots()
    ax.bar(x=["High Negative", "Negative", "Not Negative"], height=concern,
        color='blue', width=0.6, alpha=0.6)
    st.subheader('民間移管に対する気持ち')
    st.pyplot(fig)

    for reason in range(0, len(df["民間移管に対する気持ちの理由"])):
        if df["民間移管に対する気持ちの理由"][reason] is np.nan:
            pass
        else:
            st.write(df['民間移管に対する気持ちの理由'][reason])


elif option == '民間移管への関心の変化とその理由':

    fig, ax = plt.subplots()
    ax.bar(x=["High Concern", "Concern", "Less Concern"], height=concern,
        color='blue', width=0.6, alpha=0.6)
    st.subheader('民間移管への関心')
    st.pyplot(fig)

    for reason in range(0, len(df["民間移管への関心の理由"])):
        if df["民間移管への関心の理由"][reason] is np.nan:
            pass
        else:
            st.write(df['民間移管への関心の理由'][reason])

elif option == '良かった点':

    for reason in range(0, len(df["良かった点"])):
        if df["良かった点"][reason] is np.nan:
            pass
        else:
            st.write(df['良かった点'][reason])

elif option == '要改善点':

    for reason in range(0, len(df["要改善点"])):
        if df["要改善点"][reason] is np.nan:
            pass
        else:
            st.write(df['要改善点'][reason])

elif option == '民間移管の実情を共有することは有益か？？':

    fig, ax = plt.subplots()
    ax.bar(x=["High Effective", "Effective", "Less Effective"], height=concern,
        color='blue', width=0.6, alpha=0.6)
    st.subheader('民間移管の実情を共有することは有益か？？')
    st.pyplot(fig)

elif option == 'その他':

    for reason in range(0, len(df["その他"])):
        if df["その他"][reason] is np.nan:
            pass
        else:
            st.write(df['その他'][reason])


else:
     st.write("未完成")















