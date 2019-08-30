#import mysql.connector

# # mydb = mysql.connector.connect(
# # #     host = "localhost",
# # #     user = "root"
# # #     password = ""
# # # )
# #
# # print(mydb)

# Test verisi : https://github.com/datacharmer/test_db
# Yüklenişi: https://github.com/datacharmer/test_db/blob/master/README.md
# Zorlanırsanız tüm veriyi mysql\bin klasörünüzün altında bir klasöre atın
# Terminal ekranında o klasörde iken alttaki komut ile yükleyebilirsiniz.
# Localde şifreli root kullanıyorsanız -pŞifrem olarak yazın.
# ..\mysql.exe -u root -p -t < employees.sql

import pymysql
import time

db = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="employees",
    charset="latin1",
    cursorclass=pymysql.cursors.DictCursor
)

baglanti = db.cursor()
#INSERT SORGUSU
# tarih = time.strptime('2010-20-09','%Y-%d-%m')
# tarih2 = time.strptime('1978-09-10','%Y-%d-%m')
#
# baglanti.execute("insert into employees (emp_no,birth_date,first_name,last_name,gender,hire_date) values ('500000',%s,%s,%s,%s,%s)",
#                  (tarih2,"Ridvan","Bilgin","M",tarih))
# db.commit()
# print(baglanti.rowcount," kayıt eklendi")
#SELECT SORGUSU
baglanti.execute("select first_name, last_name, gender from employees where emp_no < %s and first_name = %s",(10012, "Parto"))
users = baglanti.fetchall()
dur = 0
for i in users:
    if i["gender"] == "F":
        greeting = "Mrs."
    else:
        greeting = "Mr."
    print(greeting + " " + i["first_name"] + " " + i["last_name"])

print("******************")

print("*****LIKE KULLANIMI*****")
baglanti.execute("select first_name, last_name, gender from employees where emp_no > %s and first_name like %s limit 10",(10012, "%Rod%"))
users = baglanti.fetchall()
dur = 0
for i in users:
    if i["gender"] == "F":
        greeting = "Mrs."
    else:
        greeting = "Mr."
    print(greeting + " " + i["first_name"] + " " + i["last_name"])

print("******************")
print("*** GROUP BY ve HAVING BY ****")
baglanti.execute("select first_name, count(*) as sayi from employees group by first_name having sayi<270 order by sayi DESC limit 10")
roddy = baglanti.fetchall()
for i in  roddy:
    print(i)


#UPDATE SORGUSU
# baglanti.execute("update employees set last_name = %s where emp_no = %s", ("OMER",500000))
# db.commit()
# print(baglanti.rowcount, " kayıt değiştirildi.")
#DELETE SORGUSU
# baglanti.execute("delete from employees where first_name = %s and last_name = %s",("Ramzi","Erde"))
# db.commit() #
# print(baglanti.rowcount, " kayıt silindi.")
print("******************")
print("***** JOIN KULLANIMI *****")
print("******************")
print("Pythondan çok SQL öğrenimi ile alakalı konu o yüzden üçlü kombo sorgusu ile geçiyorum.")
print("******************")
print("employees dept_emp ve departmens isimli 3 tablo var. ilk tablodan personelin ismini,")
print("ikinci tablodan departman kodunu ve üçüncü tablodanda departman ismini eşleştiren inner join örneği")

baglanti.execute("select departments.dept_name, employees.first_name,employees.last_name, count(*) as sayi from employees inner join dept_emp on employees.emp_no = dept_emp.emp_no inner join departments on dept_emp.dept_no = departments.dept_no group by departments.dept_name having (count(departments.dept_name)) limit 10")
rdy = baglanti.fetchall()
for i in  rdy:
    print(i)

print("******************")

baglanti.close()