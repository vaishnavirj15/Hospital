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
 if(b1=="Ok"):
  client=pymongo.MongoClient("mongodb://localhost:27017/")
  db=client['hospital']
  collection=db['admin']
  a=0
  b=0
  for x in collection.find({}):
   if(x["id"]==t1):
    if(x["id"]=="admin"):
     a=1
    elif(x["id"]=="admin1" and t2=="admin1"):
     a=2
     b=2
     break
    if(x["pwd"]==t2):
     b=1
  if(a==0):
   print("<script>alert('Admin id is Incorrect')</script>")
  elif(b==0):
   print("<script>alert('Password is Incorrect')</script>")
  elif(a==1 and b==1):
   print("<script>window.open('signup.html','_self')</script>")
  elif(a==2 and b==2):
   print("<script>window.open('reset.html','_self')</script>")
except Exception:
       traceback.print_exc()