import re
import pandas as pd
def preprocess(data):
    pattern='\[\d{2}/\d{2}/\d{2}, \d{2}:\d{2}:\d{2}\]'
    
    message=re.split(pattern, data)[1:]
    dates=re.findall(pattern, data)
    
    df = pd.DataFrame({'user_message': message, 'message_date': dates})

    df['message_date'] = pd.to_datetime(df['message_date'], format='[%d/%m/%y, %H:%M:%S]')


    df.rename(columns={'message_date': 'date'}, inplace=True)
    
    users = []
    messages = []

    for p in df['user_message']:
        entry = re.split(r'([^:]+):\s', p, maxsplit=1)
        if len(entry) == 3:
            # entry[1] = user, entry[2] = message
            users.append(entry[1])
            messages.append(entry[2])
        else:
            # No user found, treat as group notification
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages

    # Drop the original column
    df.drop(columns=['user_message'], inplace=True)
    
    df['year']=df['date'].dt.year
    df['month']=df['date'].dt.month_name()
    df['day']=df['date'].dt.day
    df['hour']=df['date'].dt.hour
    df['minute']=df['date'].dt.minute
    df['second']=df['date'].dt.second
    
    return df
