import requests as r
import pandas as pd

def comment_query(**kwargs):
    """
    A generic function that submits a query via the pushshift API

    Returns a pandas data frame of the data
    """
    url = "https://api.pushshift.io/reddit/search/comment/"
    request = r.get(url, params = kwargs)
    return pd.DataFrame.from_records(request.json().get('data'))
