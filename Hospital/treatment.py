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
b1=f.getvalue("b1")
try:
 if(b1=="Save"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['treatment']
   a=0
   for x in collection.find({}):
    if(x['t_id']==t1):
     a=1
     break
   collection=db['appointment']
   b=0
   for x in collection.find({}):
    if(x['app_id']==t2):
     b=1
     break
   if(a==1): 
    print("<script>alert('Treatment ID already exist')</script>")
    print("<script>window.open('Treatment.html','_self')</script>")
   elif(b==0):
    print("<script>alert('Appointment Id does not exist')</script>")
    print("<script>window.open('Treatment.html','_self')</script>")
   elif((a==0)and(b==1)):
    collection=db['treatment']
    insert1={'t_id':t1,'app_id':t2,'rem':t3}
    collection.insert_one(insert1)
    print("<script>alert('Record Saved...')</script>")
    print("<script>window.open('Treatment.html','_self')</script>")
 if(b1=="Delete"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['treatment']
   insert1={'t_id':t1}
   collection.delete_many(insert1)
   print("<script>alert('Record Deleted...')</script>")
   print("<script>window.open('Treatment.html','_self')</script>")
 if(b1=="Update"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['treatment']
   collection.update_many({'t_id':t1},{'$set':{'app_id':t2,'rem':t3}})
   print("<script>alert('Record Updated...')</script>")
   print("<script>window.open('Treatment.html','_self')</script>")
 if(b1=="All search"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['treatment']
   print("<body bgcolor=pink><table border=2 bgcolor=grey><tr><th>Treatment Id</th><th>Appointment Id</th><th>Remarks</th></tr>")
   for x in collection.find({}):
    print("<tr><th>",x["t_id"],"</th>","<th>",x["app_id"],"</th>","<th>",x["rem"],"</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")
 if(b1=="Psearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['treatment']
   print("<body bgcolor=pink><table border=2 bgcolor=grey><tr><th>Treatment Id</th><th>Appointment Id</th><th>Remarks</th></tr>")
   for x in collection.find({'t_id':t1}):
    print("<tr><th>",x["t_id"],"</th>","<th>",x["app_id"],"</th>","<th>",x["rem"],"</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")
 if(b1=="Menu"):
  print("<script>window.open('Menu.html','_self')</script>")
except Exception:
       traceback.print_exc()