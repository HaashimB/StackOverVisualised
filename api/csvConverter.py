import csv
import psycopg2
from psycopg2.extensions import AsIs

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





columns = contents.keys()
values = [contents[column] for column in columns]

insert_statement = 'insert into api_newtags(%s) values %s'




conn = psycopg2.connect("host = 'localhost' port='5432' dbname='stack' user='root' password='root'")
cur = conn.cursor()
cur.execute("TRUNCATE api_newtags")
cur.execute(insert_statement, (AsIs(','.join(columns)), tuple(values)))