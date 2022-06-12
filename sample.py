import streamlit as st
import numpy as np
import pandas as pd

st.title("Streamlitの基本的な使い方")

st.write("Hello World!")

st.write("## Hello World!")

st.write("- Hello World!")

st.markdown("**Hello World**")

st.code("""
import streamlit as st

st.title("Streamlitの基本的な使い方")

""", language="python")

df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=(f"col {i}" for i in range(20)))

st.dataframe(df.style.highlight_max(axis=0))

st.table(df)


chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"])

st.dataframe(chart_data)

st.line_chart(chart_data)

st.area_chart(chart_data)

st.bar_chart(chart_data)


import altair as alt

source = pd.DataFrame({
    "a":["A", "B", "C", "D", "E", "F", "G", "H", "I"],
    "b": [28, 55, 43, 91, 81, 53, 19, 87, 52]
})

c = alt.Chart(source).mark_bar().encode(
    x="a",
    y="b"
)

st.altair_chart(c, use_container_width=True)


val = st.radio("選択してください", ["a", "b", "c"])
st.write(f"選択した値 : {val}")

val2 = st.multiselect("選択してください", ["e", "f", "g"])
st.write(f"選択した値 : {val2}")


val3 = st.selectbox("選択してください", ["h", "i", "j"])
st.write(f"選択した値 : {val3}")

num = st.slider("選択してください", min_value=0, max_value=100, value=30)
st.write(f"選択した値 : {num}")


#num2 = st.sidebar.slider("選択してください", min_value=0, max_value=100, value=30)
#st.write(f"選択した値 : {num2}")

with st.sidebar:
    num3 = st.slider("選択してください", min_value=-100, max_value=100, value=0)
    val4 = st.selectbox("選択して", ["A", "B"])
    st.write(f"選択した値 : {num3}")
    st.write(f"選択した値 : {val4}")
    
col1, col2 = st.columns(2)

with st.col1:
    num4 = st.slider("選択してください", min_value=-200, max_value=200, value=0)
    st.write(f"選択した値 : {num4}")
    
with st.col2:
    num5 = st.slider("選択してください", min_value=-300, max_value=300, value=0)
    st.write(f"選択した値 : {num5}")





