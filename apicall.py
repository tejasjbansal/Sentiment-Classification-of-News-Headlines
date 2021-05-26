from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='7201723c0eed485799d973e04848d4a4')


def latest_news():
    latest = []

    sports = newsapi.get_everything(q='Sports News')
    international = newsapi.get_everything(q='International News')
    politics = newsapi.get_everything(q='Politics News')
    bussiness = newsapi.get_everything(q='Business News')
    tech = newsapi.get_everything(q='Technology News')
    entertainment = newsapi.get_everything(q='Entertainment News')

    latest.append(politics['articles'][0]['description'])
    latest.append(international['articles'][0]['description'])
    latest.append(tech['articles'][0]['description'])
    latest.append(bussiness['articles'][0]['description'])
    latest.append(sports['articles'][0]['description'])
    latest.append(entertainment['articles'][0]['description'])
    
    return latest