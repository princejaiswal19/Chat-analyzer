import streamlit as st
import preprocessor 
import helper

st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)  

    st.dataframe(df)
    # fetch unique user
    user_list=df['user'].unique().tolist()
   
    
    selected_user=st.sidebar.selectbox("Show analysis wrt", user_list)
     
    if st.sidebar.button("Show Analysis"):
        num_messages,words,num_media_messages,num_links=helper.fetch_stats(selected_user,df)
        col1, col2, col3 ,col4 = st.columns(4)
        
        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Total Media Messages")
            st.title(num_media_messages)
        with col4:
            st.header("Links Shared")
            st.title(num_links)
        
      
    