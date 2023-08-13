import streamlit as st
import pandas as pd


@st.cache_data
def read_data(fn):
    return pd.read_csv(fn)

def main():
    fn = st.sidebar.file_uploader("Upload a csv", type="csv")

    if not fn:
        return

    data = read_data(fn)

    st.text_area("Add Transformation")


if __name__ == "__main__":
    main()
