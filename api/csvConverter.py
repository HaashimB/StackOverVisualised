import csv
import psycopg2
import json

conn = psycopg2.connect("host = 'localhost' port='5432' dbname='stack' user='root' password='root'")
cur = conn.cursor()


def createChildNode(name, score):
    childNode = {
        "name": name,
        "size": score,
        "children": []
    }
    return childNode


def getExistingChildNode(name, parent, score):
    # Find the node in parent with parameter "name": name
    for obj in parent:
        if obj["name"] == name:
            obj["size"] += score
            return obj


contents = {
    "name": "stackoverflow",
    "children": []
}
print("running conversion algorithm")

with open('./DATA/QueryResults11.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        rowTags = row['tags'].replace('>', '').split('<')[1:]
        rowScore = row['score']
        parent = contents["children"]

        for tag in rowTags:
            childName = tag
            childNameList = [obj["name"] for obj in parent]

            if childName not in childNameList:
                childNode = createChildNode(childName, rowScore)
                parent.append(childNode)
            else:
                childNode = getExistingChildNode(childName, parent, rowScore)

            parent = childNode["children"]

print("inserting results into table")
insert_statement = "insert into api_newtags(id, content) values (%s, %s)"
cur.execute("TRUNCATE api_newtags")
cur.execute(insert_statement, (1, json.dumps(contents)))
conn.commit()
conn.close()
