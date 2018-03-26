import psycopg2
import csv

conn = psycopg2.connect("host = 'localhost' port='5432' dbname='stack' user='root' password='root'")

cur = conn.cursor()

#cur.execute('truncate api_tags')


with open('./DATA/QueryResults.csv', 'r') as f:
    reader = csv.reader(f)
    s = list(reader)

aList = []
cList = []
for line in s:
    aList.append(line[0].split('>')[0]
                 .strip('<'))
    bList = list(set(aList))
    cList.append(line[0].split('>'))

print(cList)

#cur.copy_to(f, 'api_post')

#conn.commit()



