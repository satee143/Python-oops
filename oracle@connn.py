import cx_Oracle
con=cx_Oracle.connect('satee143/Satee1432@database-1.cq2nzhmfojgx.ap-south-1.rds.amazon.aws.com/orcl')
cursor=con.cursor()
cursor.execute('select * from tab;')
