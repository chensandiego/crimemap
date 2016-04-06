import pymysql
import dbconfig
connection = pymysql.connect(host='localhost',user=dbconfig.db_user,passwd=dbconfig.db_password)

try:
	with connection.cursor() as cursor:
		sql="create database if not exists crimemap"
		cursor.execute(sql)
		sql="""create table if not exists crimemap.crimes(id int not null auto_increment,latitude float(10,6),
			longitude float(10,6),date DATETIME,category varchar(50), description varchar(1000), updated_at timestamp,primary key(id))"""
		cursor.execute(sql)
	connection.commit()
finally:
	connection.close()
	