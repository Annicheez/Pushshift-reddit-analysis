from utilities import comment_query
import requests

# Specify query parameters
object = "Insert type of object here"       # e.g. 'comment', 'submission'..
q = "Trump"
after = "Insert the date after which results are needed"        # format: Value+ ('s','m','h','d') for second, minute...
before = "Insert the date before which results are needed"        # format: Value+ ('s','m','h','d') for second, minute...
size = "50"        # Integer
sort_type = "Param specifying how to sort the results"      # one of "score", "num_comments", "created_utc"
sort = "'asc' or 'dsc' specifying order of sorting"
subreddit = "Specify subreddit to search"
metadata = "true/fale indicating whether to return metadata with request"
aggs = "subreddit"      # 'author' or 'link_id' or 'created_utc' or 'subreddit'


data = comment_query(q = q, size = size)

print(data.body[1])