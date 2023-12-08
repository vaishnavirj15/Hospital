#!C:/Users/my/AppData/Local/Programs/Python/Python311/python
print("Content-Type:text/html")
print()
import cgi
import traceback
from pymongo import MongoClient
import pymongo
f=cgi.FieldStorage()
t1=f.getvalue("t1")
t2=int(f.getvalue("t2"))
b1=f.getvalue("b1")
try:
 if(b1=="set"):
  client=pymongo.MongoClient("mongodb://localhost:27017/")
  db=client['hospital']
  collection=db['login']
  collection.update_many({'id':t1},{'$set':{'count':t2}})
  print("<script>alert('Record update...')</script>")
  print("<script>window.open('index.html','_self')</script>")
except Exception:
        traceback.print_exc()
 
 