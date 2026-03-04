import os
from notion_client import Client
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("NOTION_TOKEN")
database_id = os.getenv("NOTION_DATABASE_ID")

print(f"Loaded Token: '{token}'")
print(f"Loaded DB ID: '{database_id}'")

client = Client(auth=token)
try:
    res = client.databases.retrieve(database_id=database_id)
    print("Database retrieved successfully! The title is:", res.get("title", [{}])[0].get("plain_text", "No Title"))
except Exception as e:
    print("Notion API Error:", e)
