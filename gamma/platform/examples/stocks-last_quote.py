from polygon import RESTClient

# docs
# https://polygon.io/docs/stocks/get_v2_last_nbbo__stocksticker
# https://polygon-api-client.readthedocs.io/en/latest/Quotes.html#get-last-quote

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

quote = client.get_last_quote(
    "AAPL",
)

print(quote)
