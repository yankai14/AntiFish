import os
from wsgiref.headers import _HeaderList
from google.cloud import firestore
import json
from difflib import SequenceMatcher
from urllib.parse import unquote


db = firestore.Client()

class RequestResponseProcessor:
  def __init__(self, request):
    self.req = request
    self.dat = []
    self.fish = False

  def pullData(self):

    docs = db.collection(u'antifish').stream()

    for doc in docs:
      self.dat.append(doc.to_dict())

  def calculateSim(self):
    highestCoef = 0.0
    for i in self.dat:
      temp = SequenceMatcher(None,i["url"] ,self.req["url"])
      print(temp.get_matching_blocks())
      if temp.ratio() > highestCoef:
        highestCoef = temp.ratio()
    
    print(highestCoef)

    if highestCoef > float(os.environ["THRESHHOLD"]) and highestCoef != 1:
      self.fish = True

  def checkIfOffending(self):
    with open('phish.txt') as f:
      lines = set(map(str.strip, f.readlines()))
    if self.req["url"] in lines:
      self.fish = True

  def orchestrate(self):
    self.pullData()
    self.calculateSim()
    return {"fish": self.fish}

def process(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }

        return ('', 204, headers)

    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    request_json = {"url":unquote(request.args.get('url'))}
    rrp = RequestResponseProcessor(request_json)
    return (str(rrp.orchestrate()),200, headers )
