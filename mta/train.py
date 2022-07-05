import os 
import requests 

# set envirion variable for parsing: 
from dotenv import load_dotenv
load_dotenv()

# PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python 
from google.transit import gtfs_realtime_pb2

# Parse the feed 
feed = gtfs_realtime_pb2.FeedMessage()

# Endpoint for ACE trains
url = 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace'

# Set the headers 
header = {
    'Accept': 'application/x-google-protobuf',
    'x-api-key': os.getenv('MTA_KEY')
    }

# Call the URL 
resp = requests.get(url, headers=header, allow_redirects=True, stream=True)

feed.ParseFromString(resp.content)

for entity in feed.entity:
    print(entity)

