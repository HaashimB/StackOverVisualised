import psycopg2
import csv


conn = psycopg2.connect("host = 'localhost' port='5432' dbname='stack' user='root' password='root'")

cur = conn.cursor()

#cur.execute('truncate api_post')



# d = []
# c = []
# with open('./DATA/QueryResults.csv') as csvfile:
#     next(csvfile)
#
#     reader = csv.reader(csvfile)
#     s = list(reader)
#     for row in s:
#         aList = (row[0].split())
#         if aList == '<javascript>':
#             print(aList)
#             for ele in aList:
#                 ele1 = ele.strip('<')
#                 #print([ele1])
#                 c.append(ele1.split("[']"))
#
#     for a in c:
#         if a == "javascript":
#             d.append([a])
#









    # for row in s:
    #
    #     d.append(aList[0].strip('<'))
    #     d = list(set(d))
    #     for ele in aList:
    #         aList = ele.strip('<').split(',')
    #
    #         c.append(aList)


contents = {}

with open('./DATA/QueryResults.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        splitRow = row['tags'].split('<')
        key = "<" + splitRow[1]
        print(key)
        # Because the key isn't there yet we need to add it
        if key not in contents:
            contents[key] = []
            key_inner = []

            itemCounter = 2
            while itemCounter < len(splitRow):
                # 0 is going to be space, 1 is going to be the key so we can ignore those
                key_inner.append("<" + splitRow[itemCounter])
                itemCounter += 1

            contents[key].append(key_inner)
        else:
            itemCounter = 2
            while itemCounter < len(splitRow):
                splitItem = "<" + splitRow[itemCounter]

                key_inner = []

                # Additional check to see if the value is already part of the key list
                if splitItem not in contents[key]:
                    key_inner.append(splitItem)
                itemCounter += 1
            contents[key].append(key_inner)

print(contents)

cur.executemany('INSERT INTO api_post (key, values) VALUES (%s, %s)', contents.items())

conn.commit()

conn.close()


