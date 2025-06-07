import streamlit as st
import preprocessor 

st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)  

    st.dataframe(df)
    # fetch unique user
    user_list=df['user'].unique().tolist()
    # user_list.remove('CSEC 1+2+3')
    # user_list.sort()
    # user_list.insert(0,"Overall")
    
    st.sidebar.selectbox("Show analysis wrt", user_list)
     
    st.sidebar.button("Show Analysis")
      
    