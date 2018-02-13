import psycopg2

conn = psycopg2.connect("host = 'localhost' port='5432' dbname='stack' user='root' password='root'")
cur = conn.cursor()
with open('./DATA/QueryResults2.csv', 'w') as f:
    cur.copy_to(f, 'api_post')

conn.commit()



