from flask import render_template
from . import main 
from ..request import get_news



@main.route('/')
def index():



    news = get_news()
    title = 'BBCNEWS'
    return render_template('index.html',title =title,articles=news)
    
    