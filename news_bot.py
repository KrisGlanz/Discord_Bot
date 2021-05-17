def news(title):
    import os
    import requests
    import json
    from dotenv import load_dotenv
    NTOKEN = os.getenv('NEWS_TOKEN')
    news_List = []
    try:
        url = 'https://newsapi.org/v2/everything?qInTitle={0}&domains=bbc.co.uk&sortby=publishedAt&apiKey={1}'
        url2 = url.format(title,NTOKEN)

        response = requests.get(url2)
        response.raise_for_status()

        newsData = json.loads(response.text)
        mainNews = newsData['articles'][0]['url']
        return(mainNews)
        
    except IndexError:
        zero_result =(f"The search result of {title} brought back zero results")
        return(zero_result)
