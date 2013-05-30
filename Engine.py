# -*- coding: cp1252 -*-

#Dependencias
import urllib
import json
import oauth2 as oauth

"""
Motor de extracción de tweets
"""

"""
Retorna los n-tweets de un usuario que no tiene su cuenta protegida.
@param user: Usuario
@param nTweets: Número de tweets a extraer.
@param rt: Variable para decidir si se incluye o no retweets.
@return lsTweets: Retorna la lista de nTweets del usuario user.
"""
def getTweetsUser(user,nTweets,rt):
    url = "http://api.twitter.com/1/statuses/user_timeline.json?screen_name=%s&count=%s&include_rts=%s" % (user, nTweets,rt)
    response = urllib.urlopen(url)
    lsTweets = json.load(response)
    return lsTweets

"""
Busca tweets dado un query.
@param query: Término a buscar.
@param count: Número de tweets a buscar.
@param lang:  Busca tweets en el idioma especificado, por defecto español.
@param result: Especifica el tipo de búsqueda: popular, reciente, mezclada.
@param since: Especifica desde donde se buscaran los tweets
"""
def searchTweets(query):
    #if (lang == " "):
    #    lang = "es"
    url = "http://search.twitter.com/search.json?q=%s&result_type=mixed&page=15&rpp=200"%(query)
    #url = "https://www.api.twitter.com/1.1/search/tweets.json?q=%s&result_type=mixed&count=1000"%(query)
    response = urllib.urlopen(url)
    results = json.load(response)
    return results


def auth():
    ck = 'cAYogkcO8qrg8uarYXw'
    cks = '7fRJ6sZY4nJP8IMTdSTOcbDtTuOuF5UX22OjcND2LE'
    at = '103998535-saAt56xCjXpnFnI2ZVEuoEsHWatPrWW1qvkZnx7S'
    ats = 'enpuB0wNpnM5181u9k8d6r3fMzxfy4GnVh10ZnoL20'
    consumer = oauth.Consumer(key = ck, secret = cks)
    access_token = oauth.Token(key = at, secret = ats)
    client = oauth.Client(consumer, access_token)

