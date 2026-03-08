import os
import sys
from notion_client import Client
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('NOTION_TOKEN')
database_id = os.getenv('NOTION_DATABASE_ID')

if not token or not database_id:
    print("Missing token or DB ID")
    sys.exit(1)

client = Client(auth=token)
try:
    res = client.databases.retrieve(database_id=database_id)
    print("Database Title:", res.get("title", [{}])[0].get("plain_text", "No Title"))
    print('Properties in your Notion database:')
    props = res.get('properties', {})
    if not props:
        print("No properties found.")
    for prop_name, prop_info in props.items():
        print(f'- {prop_name} (type: {prop_info.get("type")})')
except Exception as e:
    print('Notion API Error:', e)
