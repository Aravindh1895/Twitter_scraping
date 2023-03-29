# -*- coding: utf-8 -*-
"""twt_scarp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kwDC2e4K9UnsAIKEucYybKlHOI9zZSpc
"""

!pip install snscrape
!pip install streamlit
!pip install jedi

!pip install pymongo

!pip install -q streamlit

# Commented out IPython magic to ensure Python compatibility.
# %%writefile tweet_scarp.py
# import snscrape.modules.twitter as sntwitter
# import pymongo
# import datetime
# import streamlit as st
# import pandas as pd
# import json
# import base64
# from google.colab import files
# from PIL import Image
# from io import BytesIO
# import plotly.express as px
# 
# twitter_banner = Image.open('/content/twitter_logo.jpg')
# st.image(twitter_banner)
# 
# #title of api
# st.title('Twitter scraping')
# st.write('Twitter scraping API allows developers to extract data from Twitter, such as tweets, followers, and user profiles. This data can be used for various purposes, such as sentiment analysis, social media monitoring, and market research.')
# 
# with st.sidebar:
# #user input search query from user
#   search_query = st.text_input('Enter your search query: ')
# 
# #user input starting data 
#   start_date = st.date_input('select a date in YYYY-MM-DD format: ')
# 
# #user input end date
#   end_date = st.date_input('select a date in YYYY-MM-DD format: ', key='end_date')
# 
# #slider to limit the scrape
#   tweet_limit = st.slider('Enter the number of tweets you want to scrape: ', 0, 5000)
# 
# #enabling start button to search query 
#   start= st.button("Start Scrape")
# 
# #def func for start scrapping the required data
# def tweet_scrap(search_query,start_date,end_date,tweet_limit):
#   tweet_list=[]
#   for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{search_query} since:{start_date} until:{end_date} filter:links -filter:replies').get_items()):
#     data={
#             'keyword': search_query,
#             'date': tweet.date,
#             'id': tweet.id,
#             'url': tweet.url,
#             'user': tweet.user.username,
#             'content': tweet.content,
#             'replies': tweet.replyCount,
#             'likes': tweet.likeCount,
#             'retweets': tweet.retweetCount,
#             'lang': tweet.lang,
#             'source': tweet.source
#           }    
#     tweet_list.append(data)
#     if i==tweet_limit - 1:
#       break
#   
#   return tweet_list
# 
# #def func for data frame creation
# def display_df(tweet_list):
#    df = pd.DataFrame(tweet_list, columns=["keyword","date","id","url","user","content","replies","likes","Retweets","lang","source"])
#    return df
# 
# #enabling start button to search query 
# #start= st.button("Start Scrape")
# if start:
#   start = tweet_scrap(search_query,start_date,end_date,tweet_limit)
#   mongo_data = display_df(start)
#   data_frame = display_df(start).head()
#   st.success("Here's your sample data : ")
#   st.dataframe(data_frame)
# #MongoDB connection and database collection setup
#   client = pymongo.MongoClient("mongodb+srv://aravindh1895:18Alpacino@cluster0.xmbwreu.mongodb.net/?retryWrites=true&w=majority")
#   db = client['twitter_scrape']
#   collection = db['snscrape_2']
#   collection.delete_many({})
#   dataframe_json= json.loads(mongo_data.to_json(orient='records'))
#   collection.insert_many(dataframe_json)
#   st.success('file ready for download')
# 
# #user selection download option
# download_option = st.radio("please select your desired format",('JSON','CSV'))
# 
# #to download in json format   
# if download_option=='JSON':
#        start = tweet_scrap(search_query,start_date,end_date,tweet_limit)
#        data_frame = display_df(start)
#        st.write("click the link to download the file")
#        json_string = data_frame.to_json(indent=2)
#        b64 =  base64.b64encode(json_string.encode()).decode()
#        json_filename = search_query.replace(' ', '_') + '.json'
#        href = f'<a href="data:file/json;base64,{b64}" download="{json_filename}">Download json File</a>'
#        st.markdown(href, unsafe_allow_html=True)
# 
# #to download in csv format       
# else:
#        start = tweet_scrap(search_query,start_date,end_date,tweet_limit)
#        data_frame = display_df(start)
#        st.write("click the link to download the file")
#        csv = data_frame.to_csv(index=False)
#        b64 =  base64.b64encode(csv.encode()).decode()
#        csv_filename = search_query.replace(' ', '_') + '.csv'
#        href = f'<a href="data:file/csv;base64,{b64}" download="{csv_filename}">Download CSV File</a>'
#        st.markdown(href, unsafe_allow_html=True)
# with st.sidebar:
#   st.subheader("Choose to have a graphical insights")    
#   option_name = ["most liked tweets","most retweeted tweets"]
#   option = st.radio("View in graph", option_name, index=1)
# 
#   if option == "most liked tweets":
#     tweet_eda = tweet_scrap(search_query,start_date,end_date,tweet_limit)
#     tweet_data = display_df(tweet_eda)
#     st.write("most liked tweets shown here")
#     fig=px.bar(tweet_data,x="user",y="likes")
#     st.write(fig)
#   else:
#     tweet_retweet = tweet_scrap(search_query, start_date, end_date, tweet_limit)
#     tweet_data = display_df(tweet_retweet)
#     st.write("most retweeted tweets shown here")
#     figure=px.bar(tweet_data,x="user",y="Retweets")
#     st.write(figure)
#  
#   
# 
# 
# 
#

#run streamlit in background
!streamlit run /content/tweet_scrap.py &>/content/logs.txt &

!npx localtunnel --port 8501

from google.colab import files
from PIL import Image
from io import BytesIO
uploaded = files.upload()
im = Image.open(BytesIO(uploaded['twitter_logo.jpg']))
