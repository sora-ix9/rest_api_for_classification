import pandas as pd
import os
import http.client, urllib.parse
import json
import time

pd.set_option('display.max_colwidth', 1000)

API_KEY = os.environ.get('MEDIASTACK_API_KEY')

conn = http.client.HTTPConnection('api.mediastack.com')

def get_news(text_query, debug=False):
    news_list = []
    news_no = 50

    try:
        params = urllib.parse.urlencode({
            'access_key': API_KEY,
            'limit': news_no,
            'languages': 'en',
            'keywords': text_query,
        })
        conn.request('GET', '/v1/news?{}'.format(params))
        res = conn.getresponse()
        data = res.read() # The variable "data" is in type of bytes. 
        data = data.decode('utf-8') # The variable "data" is decoded to be type of string. 
        data = json.loads(data) # The variable "data" is converted to be type of dictionary. 

        if debug == True:
            print(data)
        for news in data['data']:
            if debug == True:
                print(news['title'])
            news_list.append({
                'title': news['title'],
                'content': news['description'],
                'publisher': news['source'],
                'category': news['category'],
                'country': news['country'],
                'published time': news['published_at'],
                'url': news['url']
                
            })

        return pd.DataFrame.from_dict(news_list)
        
    except BaseException as e:
        print('Failed on_status,', str(e))
        print(0)
        time.sleep(3)