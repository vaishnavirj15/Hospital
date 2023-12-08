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
t4=int(f.getvalue("t4"))
b1=f.getvalue("b1")
if(b1=="save"):
 client=pymongo.MongoClient("mongodb://localhost:27017/")
 db=client['hospital']
 collection=db['login']
 a=0
 for x in collection.find({}):
  if(x["id"]==t1):
   a=1
   break
 if(a==1):
  print("<script>alert('Id already exist')</script>")
 elif(t2!=t3):
  print("<script>alert('Password does not match')</script>")
 elif(a==0 and t2==t3):
  insert1={'id':t1,'pwd':t2,'count':t4}
  collection.insert_one(insert1)
  print("<script>alert('Record Saved')</script>")
  print("<script>window.open('index.html','_self')</script>")
 