import requests as r
import pandas as pd
from datetime import datetime as dt

def comment_query(**kwargs):
    """
    A generic function that submits a query via the pushshift API

    Returns a json file of the data
    """
    url = "https://api.pushshift.io/reddit/search/comment/"
    request = r.get(url, params = kwargs)
    return request.json()

def generate_epoch(date: str, format = "%d-%m-%Y %H:%M:%S"):
    """
    Generates a unix epoch timestamp from the date provided

    standard format is "%d-%m-%Y %H:%M:%S", but alternate can be specified
    in the function argument

    Returns epoch stting

    """
    date = dt.strptime(date, format)

    return str(int(date.timestamp()))

