from utilities import comment_query, generate_epoch
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt
from datetime import timedelta
import re

# Specify query parameters
object = "Insert type of object here"       # e.g. 'comment', 'submission'..
q = "Trump"
after = "29-09-2020 23:00:00"        # format: Epoch (format = "%d-%m-%Y %M:%D:%Y") or Value+ ('s','m','h','d') for second, minute...
before = "29-09-2020 20:00:00"        # format: Epoch (format = "%d-%m-%Y %M:%D:%Y") or Value+ ('s','m','h','d') for second, minute...
size = "500"        # Integer
sort_type = "Param specifying how to sort the results"      # one of "score", "num_comments", "created_utc"
sort = "'asc' or 'dsc' specifying order of sorting"
subreddit = "politics"
metadata = "true/fale indicating whether to return metadata with request"
aggs = "subreddit"      # 'author' or 'link_id' or 'created_utc' or 'subreddit'


start_date = dt.strptime(before, "%d-%m-%Y %H:%M:%S")
regex = r"trump|donald"
counts = []
times = []
time = -60
end_date = dt.strptime(after, "%d-%m-%Y %H:%M:%S")

bdate = start_date # Initialize at date
edate = start_date + timedelta(minutes = 30)

i = 0
while edate <= end_date:
    times.append(time)
    time = time + 30
    json_bdata = comment_query(q=q, size=size, after = generate_epoch(bdate.strftime("%d-%m-%Y %H:%M:%S")),
    before = generate_epoch(edate.strftime("%d-%m-%Y %H:%M:%S")), subreddit= subreddit)
    df = pd.DataFrame.from_records(json_bdata.get('data'))
    comments = df.body.to_list()
    count = sum([bool(re.search(regex, comment, flags = re.IGNORECASE)) for comment in comments])
    counts.append(count)
    bdate = bdate + timedelta(minutes = 30)
    edate = edate + timedelta(minutes = 30)
    i = i + 1
    print(i)
    print(len(comments))
print(counts)
print(times)
plt.plot(times, counts)
plt.show()
