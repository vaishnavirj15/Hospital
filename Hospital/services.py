#!C:/Users/my/AppData/Local/Programs/Python/Python311/python
print("Content-Type:text/html")
print()
import cgi
import traceback
from pymongo import MongoClient
import pymongo
f=cgi.FieldStorage()
t1=f.getvalue("t1")
t2=f.getvalue("t2")
t3=f.getvalue("t3")
t4=f.getvalue("t4")
b1=f.getvalue("b1")
try:
 if(b1=="Save"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['services']
   a=0
   for x in collection.find({}):
    if(x['serv_id']==t1):
     a=1
     break
   collection=db['hospital']
   b=0
   for x in collection.find({}):
    if(x['hos_id']==t4):
     b=1
     break
   if(a==1): 
    print("<script>alert('Service ID already exist')</script>")
    print("<script>window.open('Services.html','_self')</script>")
   elif(b==0):
    print("<script>alert('Hospital Id does not exist')</script>")
    print("<script>window.open('Services.html','_self')</script>")
   elif((a==0)and(b==1)):
    collection=db['services']
    insert1={'serv_id':t1,'serv_nm':t2,'fee':t3,'hos_id':t4}
    collection.insert_one(insert1)
    print("<script>alert('Record Saved...')</script>")
    print("<script>window.open('Services.html','_self')</script>")
 if(b1=="Delete"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['services']
   insert1={'serv_id':t1}
   collection.delete_many(insert1)
   print("<script>alert('Record Deleted...')</script>")
   print("<script>window.open('Services.html','_self')</script>")
 if(b1=="Update"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['services']
   collection.update_many({'serv_id':t1},{'$set':{'serv_nm':t2,'fee':t3,'hos_id':t4}})
   print("<script>alert('Record Updated...')</script>")
   print("<script>window.open('Services.html','_self')</script>")
 if(b1=="All search"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['services']
   print("<body bgcolor=pink><table border=2 bgcolor=grey><tr><th>Service Id</th><th>Service name</th><th>Fee</th><th>Hospital id</th></tr>")
   for x in collection.find({}):
    print("<tr><th>",x["serv_id"],"</th>","<th>",x["serv_nm"],"</th>","<th>",x["fee"],"</th>","<th>",x["hos_id"],"</th>","</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")
 if(b1=="Psearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['services']
   print("<body bgcolor=pink><table border=2 bgcolor=grey><tr><th>Service Id</th><th>Service name</th><th>Fee</th><th>Hospital id</th></tr>")
   for x in collection.find({'serv_id':t1}):
    print("<tr><th>",x["serv_id"],"</th>","<th>",x["serv_nm"],"</th>","<th>",x["fee"],"</th>","<th>",x["hos_id"],"</th>","</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")
 if(b1=="Menu"):
  print("<script>window.open('Menu.html','_self')</script>")
except Exception:
        traceback.print_exc()
