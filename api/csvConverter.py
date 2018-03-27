import psycopg2
import csv

conn = psycopg2.connect("host = 'localhost' port='5432' dbname='stack' user='root' password='root'")

cur = conn.cursor()

#cur.execute('truncate api_tags')


contents = {}

with open('./DATA/QueryResults.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        splitRow = row['tags'].split('<')
        key = "<" + splitRow[1]
        print(key)
        # Because the key isn't there yet we need to add it
        if (key not in contents):
            contents[key] = []

            itemCounter = 2
            while itemCounter < len(splitRow):
                # 0 is going to be space, 1 is going to be the key so we can ignore those
                contents[key].append("<" + splitRow[itemCounter])
                itemCounter += 1
        else:
            itemCounter = 2
            while itemCounter < len(splitRow):
                splitItem = "<" + splitRow[itemCounter]

                # Additional check to see if the value is already part of the key list
                if splitItem not in contents[key]:
                    contents[key].append(splitItem)
                itemCounter += 1

print(contents)

#cur.copy_to(f, 'api_post')

#conn.commit()



