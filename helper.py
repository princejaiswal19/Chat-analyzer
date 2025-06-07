from urlextract import URLExtract

extract = URLExtract()

def fetch_stats(selected_user, df):
    if selected_user !='Overall':
        df=df[df['user']==selected_user]
    num_messages=df.shape[0]
    words=[]
    for message in df['message']:
        words.extend(message.split())
       
    
    
    
    num_media_messages=df[df['message']=='image omitted\n'].shape[0]
    # return num_messages, len(words), num_media_messages
    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_messages,len(words),num_media_messages,len(links)
   
    
    


    # fetch the number of messages
    

    # fetch the total number of words
    # words = []
    # for message in df['message']:
    #     words.extend(message.split())
    # return num_messages,len(words)   
        
    # fetch number of media messages
    # num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]

    # # fetch number of links shared
    # links = []
    # for message in df['message']:
    #     links.extend(extract.find_urls(message))

    # return num_messages,len(words),num_media_messages,len(links)
    
