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
    aList.append(line[0].split('>', 1)[0]
                 .strip('<'))
    bList = list(set(aList))
    print(line[0].split('<', 0)[0].strip('<>')[0])

print(aList.count('python'))
print(bList.count('python'))
print(cList)
#cur.copy_to(f, 'api_post')

#conn.commit()



