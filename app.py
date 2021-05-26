from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from apicall import latest_news
from pageScraper import *
from sentAnalysis import *

app = Flask(__name__)  # initializing a flask app


@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    api_news = latest_news()
    return render_template("index.html",api_news=api_news)

@app.route('/politics',methods=['GET'])
@cross_origin()
def politics():
    url = 'https://abcnews.go.com/Politics'
    soup = soupee(url)
    headlines,Desc = parser(soup)
    sentiment = Sentiment_Analysis(headlines)
    return render_template("news.html",news = "Politics",len = len(headlines),stories=Desc,heading=headlines,sentiment=sentiment)

    


@app.route('/international',methods=['GET'])
@cross_origin()
def international():
    url = 'https://abcnews.go.com/International'
    soup = soupee(url)
    headlines,Desc = parser(soup)
    sentiment = Sentiment_Analysis(headlines)
    return render_template("news.html",news = "International",len = len(headlines),stories=Desc,heading=headlines,sentiment=sentiment)

@app.route('/technology',methods=['GET'])
@cross_origin()
def technology():
    url = 'https://abcnews.go.com/Technology'
    soup = soupee(url)
    headlines,Desc = parser(soup)
    sentiment = Sentiment_Analysis(headlines)
    return render_template("news.html",news = "Technology",len = len(headlines),stories=Desc,heading=headlines,sentiment=sentiment)

@app.route('/business',methods=['GET'])
@cross_origin()
def business():
    url = 'https://abcnews.go.com/Business'
    soup = soupee(url)
    headlines,Desc = parser(soup)
    sentiment = Sentiment_Analysis(headlines)
    return render_template("news.html",news = "Business",len = len(headlines),stories=Desc,heading=headlines,sentiment=sentiment)

@app.route('/sports',methods=['GET'])
@cross_origin()
def sports():
    url = 'https://abcnews.go.com/Sports'
    soup = soupee(url)
    headlines,Desc = parser(soup)
    sentiment = Sentiment_Analysis(headlines)
    return render_template("news.html",news = "Sports",len = len(headlines),stories=Desc,heading=headlines,sentiment=sentiment)

@app.route('/entertainment',methods=['GET'])
@cross_origin()
def entertainment():
    url = 'https://abcnews.go.com/Entertainment'
    soup = soupee(url)
    headlines,Desc = parser(soup)
    sentiment = Sentiment_Analysis(headlines)
    return render_template("news.html",news = "Entertainment",len = len(headlines),stories=Desc,heading=headlines,sentiment=sentiment)

if __name__ == "__main__":
    app.run(debug=True)  # running the app
