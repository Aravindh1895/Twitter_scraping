# Twitter scraping
A Twitter scraping project involves extracting data from Twitter's public APIs or web pages using a programming language like Python. The extracted data can be used for various purposes like sentiment analysis, social media monitoring, or data analysis.
#Project overview
This is a Python-based project that helps to scrape tweets from Twitter using the Snscrape library, convert them to pandas dataframe and store them in a MongoDB database, and download the query in required formats.
Installation
To run this project, you need to have Python 3.x installed on your system. You also need to install the following Python libraries:
•	snscrape
•	streamlit
•	pymongo
•	pandas
#User input options
The script will prompt you to enter a search query for tweets.The script will then allow user entering the starting and ending date of search query and will allow user to select number of tweets to be scraped using slider.
#Uploading to MongoDB database
Once the input are given by the user and after selecting the search option then the script will start scraping tweets that matches your search query. 
The scraped datas are stored in a MongoDB database,You can view the datas in the tweets collection in the MongoDB database.
The sample scraped datas are displayed using the pandas dataframe as mentioned in the script.
#Download in csv/json format
The scrapped datas are fetched from the MongoDB database and are available for download in CSV/JSON format as per the requirement.
