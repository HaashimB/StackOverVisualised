import csv
import psycopg2

print('opening connection to psql database')
conn = psycopg2.connect("host = 'localhost' port='5432' dbname='stack' user='root' password='root'")
cur = conn.cursor()

contents = {
    "tags": [],
    "score": []
}

file = input("please enter dataset: ")

insert_statement = "insert into api_" + file + "csv (tags, score) values (%s, %s)"

cur.execute("TRUNCATE api_" + file + "csv")

print("running conversion algorithm")

with open('./DATA/' + file + '.csv', 'r') as csvfile:

    reader = csv.DictReader(csvfile)

    for row in reader:
        rowTags = row['tags'].replace('>', '.').replace('<', '')
        rowTags = rowTags[:-1]
        rowScore = row['score']

        cur.execute(insert_statement, (rowTags, rowScore))


conn.commit()
conn.close()
print('connection closed')


