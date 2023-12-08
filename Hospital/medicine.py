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
 if(b1=="Save"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['medicine']
   a=0
   for x in collection.find({}):
    if(x['med_id']==t1):
     a=1;
     break;
   if(a==1): 
    print("<script>alert('Medicine ID already exist')</script>")
    print("<script>window.open('Medicine.html','_self')</script>")
   else:
    insert1={'med_id':t1,'med_nm':t2}
    collection.insert_one(insert1)
    print("<script>alert('Record Saved...')</script>")
    print("<script>window.open('Medicine.html','_self')</script>")
 if(b1=="Delete"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['medicine']
   insert1={'med_id':t1}
   collection.delete_many(insert1)
   print("<script>alert('Record Deleted...')</script>")
   print("<script>window.open('Medicine.html','_self')</script>")
 if(b1=="Update"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['medicine']
   collection.update_many({'med_id':t1},{'$set':{'med_nm':t2}})
   print("<script>alert('Record Updated...')</script>")
   print("<script>window.open('Medicine.html','_self')</script>")
 if(b1=="All search"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['medicine']
   print("<body bgcolor=pink><table border=2 bgcolor=grey><tr><th>Medicine Id</th><th>Medicine name</th></tr>")
   for x in collection.find({}):
    print("<tr><th>",x["med_id"],"</th>","<th>",x["med_nm"],"</th>","</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")
 if(b1=="Psearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['medicine']
   print("<body bgcolor=pink><table border=2 bgcolor=grey><tr><th>Medicine Id</th><th>Medicine name</th></tr>")
   for x in collection.find({'med_id':t1}):
    print("<tr><th>",x["med_id"],"</th>","<th>",x["med_nm"],"</th>","</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")
 if(b1=="Menu"):
  print("<script>window.open('Menu.html','_self')</script>")
except Exception:
        traceback.print_exc()