#This is no longer used in the project
#It was initially used to retrieve data from the RestAPI


import requests
import psycopg2


conn = psycopg2.connect("host = 'localhost' port='5432' dbname='stack' user='root' password='root'")

req = requests.get('https://api.stackexchange.com/2.2/tags?order=desc&sort=popular&site=stackoverflow')

data = req.json()

cur = conn.cursor()

cur.execute('truncate api_tags')
for each in data['items']:
    countField = each['count']
    nameField = each['name']
    cur.execute('INSERT INTO api_tags(count,name) VALUES (%s, %s)', (countField, nameField))

conn.commit()

conn.close()
