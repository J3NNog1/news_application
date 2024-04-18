import openai
import os
from dotenv import find_dotenv, load_dotenv
import time
import logging
from datetime import datetime


load_dotenv()

news_api_key = os.environ.get("NEWS_API_KEY")
client = openai.OpenAI()
model = "gpt-3.5-turbo-16k"

# def main():
#     pass

# if __name__ == "__main__":
#     main()

def get_news(topic):
    url = (
        f"https://newsapi.org/v2/everything?q={topic}&apiKey={news_api_key}&pageSize=5"

    )