import requests
import json
import psycopg2


conn = psycopg2.connect("host = 'localhost' port='5432' dbname='stack' user='root' password='root'")

req = requests.get('https://api.stackexchange.com/2.2/tags?fromdate=1420070400&order='
                 'desc&min=1&max=1000&sort=popular&site=stackoverflow')

data = req.json()

cur = conn.cursor()

for each in data['items']:
    countField = each['count']
    nameField = each['name']
    cur.execute("INSERT INTO api_tags(count,name) VALUES (%s, %s)",
                (countField, nameField))

conn.commit()

conn.close()
