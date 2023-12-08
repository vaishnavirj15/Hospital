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
t7=f.getvalue("t7")
b1=f.getvalue("b1")
try:
 if(b1=="Save"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['appointment']
   a=0
   for x in collection.find({}):
    if(x['app_id']==t1):
     a=1
     break
   collection=db['hospital']
   b=0
   for x in collection.find({}):
    if(x['hos_id']==t2):
     b=1
     break
   collection=db['doctor']
   c=0
   for x in collection.find({}):
    if(x['doc_id']==t5):
     c=1
     break
   collection=db['services']
   d=0
   for x in collection.find({}):
    if(x['serv_id']==t6):
     d=1
     break
   collection=db['patient']
   e=0
   for x in collection.find({}):
    if(x['pat_id']==t7):
     e=1
     break
   if(a==1):
    print("<script>alert('Appointment id already exist')</script>")
    print("<script>window.open('Appointment.html','_self')</script>")
   elif(b==0):
    print("<script>alert('Hospital id does not exist')</script>")
    print("<script>window.open('Appointment.html','_self')</script>")
   elif(c==0):
    print("<script>alert('Doctor id does not exist')</script>")
    print("<script>window.open('Appointment.html','_self')</script>")
   elif(d==0):
    print("<script>alert('Services id does not exist')</script>")
    print("<script>window.open('Appointment.html','_self')</script>")
   elif(e==0):
    print("<script>alert('Patient id does not exist')</script>")
    print("<script>window.open('Appointment.html','_self')</script>")
   elif((a==0)and(b==1)and(c==1)and(d==1)and(e==1)):
    collection=db['appointment']
    insert1={'app_id':t1,'hos_id':t2,'app_date':t3,'app_time':t4,'doc_id':t5,'serv_id':t6,'pat_id':t7}
    collection.insert_one(insert1)
    print("<script>alert('Record Saved...')</script>")
    print("<script>window.open('Appointment.html','_self')</script>")
 if(b1=="Delete"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['appointment']
   insert1={'app_id':t1}
   collection.delete_many(insert1)
   print("<script>alert('Record Deleted...')</script>")
   print("<script>window.open('Appointment.html','_self')</script>")
 if(b1=="Update"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['appointment']
   collection.update_many({'app_id':t1},{'$set':{'hos_id':t2,'app_date':t3,'app_time':t4,'doc_id':t5,'serv_id':t6,'pat_id':t7}})
   print("<script>alert('Record Updated...')</script>")
   print("<script>window.open('Appointment.html','_self')</script>")
 if(b1=="All search"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['appointment']
   print("<body bgcolor=pink><table border=2 bgcolor=grey><tr><th>Appointment.id</th><th>Hospital Id</th><th>Appointment Date</th><th>Appointment time</th><th>Doctor id</th><th>Service Id</th><th>PatientId</th></tr>")
   for x in collection.find({}):
    print("<tr><th>",x["app_id"],"</th>","<th>",x["hos_id"],"</th>","<th>",x["app_date"],"<th>",x["app_time"],"<th>",x["doc_id"],"<th>",x["serv_id"],"<th>",x["pat_id"],"</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")
 if(b1=="Psearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['appointment']
   print("<body bgcolor=pink><table border=2 bgcolor=grey><tr><th>Appointment.id</th><th>Hospital Id</th><th>Appointment Date</th><th>Appointment time</th><th>Doctor id</th><th>Service Id</th><th>PatientId</th></tr>")
   for x in collection.find({'app_id':t1}):
    print("<tr><th>",x["app_id"],"</th>","<th>",x["hos_id"],"</th>","<th>",x["app_date"],"<th>",x["app_time"],"<th>",x["doc_id"],"<th>",x["serv_id"],"<th>",x["pat_id"],"</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")
 if(b1=="Menu"):
  print("<script>window.open('Menu.html','_self')</script>")
except Exception:
       traceback.print_exc()
