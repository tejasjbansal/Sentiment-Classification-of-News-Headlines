import pickle5 as pickle


def Sentiment_Analysis(headline_list):
    loaded_model = pickle.load(open('models/finalized_model.sav', 'rb'))
    predictions = loaded_model.predict(headline_list)
    sentiment = []
    for i in predictions:
        if(i==0):
            sentiment.append("Neutral")
        elif(i==1):
            sentiment.append("Positive")
        else:
            sentiment.append("Negative")

    return sentiment
