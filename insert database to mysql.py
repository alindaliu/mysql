import pymysql

host = 'localhost'
user = 'root'
password = '123456'
db = 'test'
port = 3306
conn = pymysql.connect(host, user, password, db, port, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
print('连接成功')
#sql语句
sql='insert into black_list(id, cert_no, name, cert_type, provider, expire_date, creat_time, update_time) values (%s, %s, %s, %s, %s, %s, %s, %s);'
#获取游标
cur = conn.cursor()

#往数据库x表中批量插入数据
for i in range(1, 5):
    str_i = str(i)
    id = '20200103' + str_i
    cert_no = '45620' + str_i
    name = 'liuying'
    cert_type = '01'
    provider = '行数据' + str_i
    expire_date = '2099-01-03 15:19:47.0'
    create_time = '2020-01-03 15:19:47.0'
    update_time = '2020-01-03 15:20:12.0'
    #参数化方式传参
    row_count = cur.execute(sql,[id, cert_no, name, cert_type, provider, expire_date,create_time, update_time])
    print('执行', i, '条语句')

#统一提交
conn.commit()
print(name)
#关闭游标
cur.close()
#关闭连接
conn.close()