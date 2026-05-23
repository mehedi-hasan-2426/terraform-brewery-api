import json
import os
import urllib.request
import urllib.error
import boto3
from datetime import datetime, timezone

DYNAMODB_TABLE = os.environ["DYNAMODB_TABLE"]
BREWERY_API_URL = "https://api.openbrewerydb.org/v1/breweries/random?size=5"

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(DYNAMODB_TABLE)


def lambda_handler(event, context):
    try:
        with urllib.request.urlopen(BREWERY_API_URL, timeout=10) as response:
            breweries = json.loads(response.read().decode())
    except urllib.error.URLError as error:
        print("Failed to fetch breweries:", str(error))
        raise

    stored = 0
    for brewery in breweries:
        item = {
            "id":           brewery.get("id", "unknown"),
            "name":         brewery.get("name", ""),
            "brewery_type": brewery.get("brewery_type", ""),
            "city":         brewery.get("city", ""),
            "state":        brewery.get("state_province", ""),
            "country":      brewery.get("country", ""),
            "website_url":  brewery.get("website_url") or "",
            "fetched_at":   datetime.now(timezone.utc).isoformat(),
        }
        table.put_item(Item=item)
        stored += 1
        print(f"Stored brewery: {item['name']} ({item['city']}, {item['state']})")

    print(f"Done. Stored {stored} breweries.")
    return {"statusCode": 200, "stored": stored}
