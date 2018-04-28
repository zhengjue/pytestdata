import MySQLdb
conn = MySQLdb.connect(host='172.18.0.3',user='root',passwd='centos',db='pytest',charset='utf8')
cursor=conn.cursor()

print(conn)
print(cursor)

cursor.close()
conn.close()
