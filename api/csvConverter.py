#For a detailed explanation of this code please refer to page 43 of the Final Year Project Manual

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
    for node in parent:
        if node["name"] == name:
            node["size"] += score
            return node


contents = {
    "name": "stackoverflow",
    "children": []
}

file = input("please enter dataset: ")
print("running conversion algorithm")

with open('./DATA/QueryResults' + str(file) + '.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        rowTags = row['tags'].replace('>', '').split('<')[1:]
        rowScore = row['score']
        parent = contents["children"]

        for tag in rowTags:
            childName = tag
            childNameList = [node["name"] for node in parent]

            if childName not in childNameList:
                childNode = createChildNode(childName, rowScore)
                parent.append(childNode)
            else:
                childNode = getExistingChildNode(childName, parent, rowScore)

            parent = childNode["children"]

print(type(parent))
insert_statement = "insert into api_newtags(id, content) values (%s, %s)"
cur.execute("TRUNCATE api_newtags")
cur.execute(insert_statement, (1, json.dumps(contents)))
conn.commit()
conn.close()
