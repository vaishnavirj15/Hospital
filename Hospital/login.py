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
b1=f.getvalue("b1")
try:
 if(b1=="Login"):
  client=pymongo.MongoClient("mongodb://localhost:27017/")
  db=client['hospital']
  collection=db['login']
  a=0
  for x in collection.find({}):
   if(x["id"]==t1):
    a=1
    break
  if(a==0):
   print("<script>alert('Invalid user id')</script>")
  else:
   if(x["id"]==t1 and x["pwd"]==t2 and x["count"]>0):
    collection.update_many({'id':t1},{'$set':{'count':x["count"]-1}})
    print("<script>window.open('Menu.html','_self')</script>")
   elif(x["count"]==0):
    print("<script>alert('Re-register please')</script>")
    print("<script>window.open('admin.html','_self')</script>")
   else:
    print("<script>alert('Invalid Password')</script>")
 if(b1=="New User"):
   print("<script>window.open('admin.html','_self')</script>")
except Exception:
       traceback.print_exc()
  
    


 
 