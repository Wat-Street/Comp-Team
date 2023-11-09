from polygon import RESTClient

# docs
# https://polygon.io/docs/indices/get_v1_open-close__indicesticker___date
# https://polygon-api-client.readthedocs.io/en/latest/Aggs.html#get-daily-open-close-agg

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

# make request
request = client.get_daily_open_close_agg(
    "I:SPX",
    "2023-03-28",
)

print(request)
