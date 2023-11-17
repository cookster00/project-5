"""
Creating insert and fetch functions for mongo testing
"""

import os
from pymongo import MongoClient
import arrow

# Setting up mongo client
client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)

# Use database "test_inputs"
db = client.test_inputs
# Using collection "test_lists"
collection = db.test_lists

# Define a constant variable for time
TIME1 = "2023-07-01T00:00"

# Function to insert attempt data into a collection
def insert_attempt(begin_time, brevet_dist, rows):
    # Use the collection object to insert a new document with the specified data
    output = collection.insert_one({
        "begin_time": begin_time,
        "brevet_dist": brevet_dist,
        "rows": rows
    })

    # Get the inserted document's ID and convert it to a string
    _id = output.inserted_id
    return str(_id)

# Function to fetch the latest attempt data from the collection
def fetch_attempt():
    # Use the collection object to find documents, sort them by "_id" in descending order, and limit to 1 result
    inputs = collection.find().sort("_id", -1).limit(1)

    # Iterate over the result (typically just one document)
    for value in inputs:
        # Return the values of "begin_time", "brevet_dist", and "rows" from the document
        return value["begin_time"], value['brevet_dist'], value['rows']
