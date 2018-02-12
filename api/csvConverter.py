import psycopg2

conn = psycopg2.connect("host = 'localhost' port='5432' dbname='stack' user='root' password='root'")
cur = conn.cursor()
with open('./DATA/QueryResults.txt', 'r') as f:
    next(f)
    cur.copy_from(f, 'api_post')

conn.commit()



