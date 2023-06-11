# INIT

this is for your team to edit :)
ideal template for readme
/ team info, names, faces, whatever you want to add
/ projects done
/ instructions for repo (how to access models, notebooks, data, etc)

# Accessing data

## Reference data (supported assets, exchanges, instruments)

method: GET
base endpoint: https://reference-data-api.kaiko.io/v1
Assets endpoint: base endpoint + /assets
Exchanges endpoint: base endpoint + /exchanges
Instruments endpoint: base endpoint + /instruments
Auth: not needed

Example request: curl --compressed -H 'Accept: application/json' 'https://reference-data-api.kaiko.io/v1/exchanges'

Example response (json format):

{
"result": "success",
"data": [
{
"code": "bfly",
"name": "bitFlyer",
"kaiko_legacy_slug": "bl"
},
{
"code": "bfnx",
"name": "Bitfinex",
"kaiko_legacy_slug": "bf"
}
/* ... */
]
}

## Market Data

method: GET
base endpoint: https://us.market-api.kaiko.io/
Auth: Must specify an API key in the header of request (X-Api-Key: <client-api-key>)
Pagination: For larger data sets a continuation_token and next_url and specfied in the response. These will need to be used to make another call to retreieve the full dataset

Example request: curl --compressed -H 'Accept: application/json' -H 'X-Api-Key: <client-api-key>' 'https://<api_hostname>/<endpoint>'

Note you can run the curl commands through your terminal. Alternativley you can make requests using postman.

Refer to https://docs.kaiko.com/?python#usage for the full api docs
