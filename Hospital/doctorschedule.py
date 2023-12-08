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
b1=f.getvalue("b1")
try:
 if(b1=="Save"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['doctor']
   a=0
   for x in collection.find({}):
    if(x['doc_id']==t1):
     a=1;
     break;
   if(a==0): 
    print("<script>alert('Doctor ID does not exist')</script>")
    print("<script>window.open('DoctorSchedule.html','_self')</script>")
   else:
    collection=db['doctorschedule']
    insert1={'doc_id':t1,'s_date':t2,'e_date':t3,'s_time':t4,'e_time':t5}
    collection.insert_one(insert1)
    print("<script>alert('Record Saved...')</script>")
    print("<script>window.open('DoctorSchedule.html','_self')</script>")
 if(b1=="Delete"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['doctorschedule']
   insert1={'doc_id':t1}
   collection.delete_many(insert1)
   print("<script>alert('Record Deleted...')</script>")
   print("<script>window.open('DoctorSchedule.html','_self')</script>")
 if(b1=="Update"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['doctorschedule']
   collection.update_many({'doc_id':t1},{'$set':{'s_date':t2,'e_date':t3,'s_time':t4,'e_time':t5}})
   print("<script>alert('Record Updated...')</script>")
   print("<script>window.open('DoctorSchedule.html','_self')</script>") 
 if(b1=="All search"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['doctorschedule']
   print("<body bgcolor=pink><table border=2 bgcolor=grey><tr><th>Doctor Id</th><th>Start date</th><th>End date</th><th>Start time</th><th>End time</th></tr>")
   for x in collection.find({}):
    print("<tr><th>",x["doc_id"],"</th>","<th>",x["s_date"],"</th>","<th>",x["e_date"],"</th>","<th>",x["s_time"],"</th>","<th>",x["e_time"],"</th>","</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")
 if(b1=="Psearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['doctorschedule']
   print("<body bgcolor=pink><table border=2 bgcolor=grey><tr><th>Doctor Id</th><th>Start date</th><th>End date</th><th>Start time</th><th>End time</th></tr>")
   for x in collection.find({'doc_id':t1}):
    print("<tr><th>",x["doc_id"],"</th>","<th>",x["s_date"],"</th>","<th>",x["e_date"],"</th>","<th>",x["s_time"],"</th>","<th>",x["e_time"],"</th>","</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")
 if(b1=="Menu"):
  print("<script>window.open('Menu.html','_self')</script>")  
except Exception:
      traceback.print_exc()
