import csv
import psycopg2
import json

def createChildNode(name):
    childNode = {
        "name": name,
        "size": 1,
        "children": []
    }
    return childNode


def getExistingChildNode(name, parent):
    # Find the node in parent with parameter "name": name
    for obj in parent:
        if obj["name"] == name:
            obj["size"] += 1
            return obj


contents = {
    "name": "stackoverflow",
    "children": []
}

with open('./DATA/QueryResults.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        rowTags = row['tags'].replace('>', '').split('<')[1:]
        parent = contents["children"]

        for tag in rowTags:
            childName = tag
            childNameList = [obj["name"] for obj in parent]

            if childName not in childNameList:
                childNode = createChildNode(childName)
                parent.append(childNode)
            else:
                childNode = getExistingChildNode(childName, parent)

            parent = childNode["children"]

# with open('./DATA/tags.json', 'w') as fp:
#     json.dump(contents, fp, indent=2)

conn = psycopg2.connect("host = 'localhost' port='5432' dbname='stack' user='root' password='root'")
cur = conn.cursor()
cur.execute("truncate api_nwq")
cur.execute("INSERT")