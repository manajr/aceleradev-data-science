import streamlit as st
import pandas as pd

def main():
    st.title('Seman AceleraDev Data Science')
    files = st.file_uploader("Upload your arquivo", type = 'csv')
    if files is not None:
        slider = st.slider('Valores', 1,100)
        df = pd.read_csv('IRIS.csv')
        st.dataframe(df.head(slider))
        st.markdown('Table')
        st.table(df.head(slider))
        st.write(df.columns)
        
if __name__ == '__main__':
    main()