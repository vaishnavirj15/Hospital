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
t5=f.getvalue("t5")
t6=f.getvalue("t6")
b1=f.getvalue("b1")
try:
 if(b1=="Save"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['staff']
   a=0
   for x in collection.find({}):
    if(x['staff_id']==t1):
     a=1
     break
   collection=db['hospital']
   b=0
   for x in collection.find({}):
    if(x['hos_id']==t6):
     b=1
     break
   if(a==1): 
    print("<script>alert('Staff ID already exist')</script>")
    print("<script>window.open('Staff.html','_self')</script>")
   elif(b==0):
    print("<script>alert('Hospital id does not exist')</script>")
    print("<script>window.open('Staff.html','_self')</script>")
   elif((a==0)and(b==1)):
    collection=db['staff']
    insert1={'staff_id':t1,'staff_nm':t2,'desig':t3,'con_no':t4,'e_mail':t5,'hos_id':t6}
    collection.insert_one(insert1)
    print("<script>alert('Record Saved...')</script>")
    print("<script>window.open('Staff.html','_self')</script>")
 if(b1=="Delete"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['staff']
   insert1={'staff_id':t1}
   collection.delete_many(insert1)
   print("<script>alert('Record Deleted...')</script>")
   print("<script>window.open('Staff.html','_self')</script>")
 if(b1=="Update"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['staff']
   collection.update_many({'staff_id':t1},{'$set':{'staff_nm':t2,'desig':t3,'con_no':t4,'e_mail':t5,'hos_id':t6}})
   print("<script>alert('Record Updated...')</script>")
   print("<script>window.open('Staff.html','_self')</script>")
 if(b1=="All search"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['staff']
   print("<body bgcolor=pink><table border=2 bgcolor=grey><tr><th>Staff Id</th><th>Staff name</th><th>Designation</th><th>Contact no.</th><th>Email</th><th>Hospital Id</th></tr>")
   for x in collection.find({}):
    print("<tr><th>",x["staff_id"],"</th>","<th>",x["staff_nm"],"</th>","<th>",x["desig"],"</th>","<th>",x["con_no"],"</th>","<th>",x["e_mail"],"</th>","<th>",x["hos_id"],"</th>","</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")
 if(b1=="Psearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['staff']
   print("<body bgcolor=pink><table border=2 bgcolor=grey><tr><th>Staff Id</th><th>Staff name</th><th>Designation</th><th>Contact no.</th><th>Email</th><th>Hospital Id</th></tr>")
   for x in collection.find({'staff_id':t1}):
    print("<tr><th>",x["staff_id"],"</th>","<th>",x["staff_nm"],"</th>","<th>",x["desig"],"</th>","<th>",x["con_no"],"</th>","<th>",x["e_mail"],"</th>","<th>",x["hos_id"],"</th>","</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")
 if(b1=="Menu"):
  print("<script>window.open('Menu.html','_self')</script>")
except Exception:
        traceback.print_exc()


