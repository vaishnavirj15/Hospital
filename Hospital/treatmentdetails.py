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
   collection=db['treatment']
   a=0
   for x in collection.find({}):
    if(x['t_id']==t1):
     a=1
     break
   collection=db['medicine']
   b=0
   for x in collection.find({}):
    if(x['med_id']==t2):
     b=1
     break
   if(a==0):
    print("<script>alert('Treatment id does not exist')</script>")
    print("<script>window.open('TreatmentDetails.html','_self')</script>")
   elif(b==0):
    print("<script>alert('Medicine id does not exist')</script>")
    print("<script>window.open('TreatmentDetails.html','_self')</script>")
   elif((a==1)and(b==1)):
    collection=db['treatmentdetails']
    insert1={'t_id':t1,'med_id':t2,'quan':t3,'dose':t4}
    collection.insert_one(insert1)
    print("<script>alert('Record Saved...')</script>")
    print("<script>window.open('TreatmentDetails.html','_self')</script>")
 if(b1=="Delete"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['treatmentdetails']
   insert1={'t_id':t1}
   collection.delete_many(insert1)
   print("<script>alert('Record Deleted...')</script>")
   print("<script>window.open('TreatmentDetails.html','_self')</script>")
 if(b1=="Update"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['treatmentdetails']
   collection.update_many({'t_id':t1},{'$set':{'med_id':t2,'quan':t3,'dose':t4}})
   print("<script>alert('Record Updated...')</script>")
   print("<script>window.open('TreatmentDetails.html','_self')</script>")
 if(b1=="All search"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['treatmentdetails']
   print("<table border=2 bgcolor=grey><tr><th>Treatment Id</th><th>Medicine Id</th><th>Quantity</th><th>Dose</th></tr>")
   for x in collection.find({}):
    print("<tr><th>",x["t_id"],"</th>","<th>",x["med_id"],"</th>","<th>",x["quan"],"</th>","<th>",x["dose"],"</th>","</th></tr>")
   print("<body bgcolor=pink><input type=button value='Print' onclick=window.print()></body>")
 if(b1=="Psearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['treatmentdetails']
   print("<body bgcolor=pink><table border=2 bgcolor=grey><tr><th>Treatment Id</th><th>Medicine Id</th><th>Quantity</th><th>Dose</th></tr>")
   for x in collection.find({'t_id':t1}):
    print("<tr><th>",x["t_id"],"</th>","<th>",x["med_id"],"</th>","<th>",x["quan"],"</th>","<th>",x["dose"],"</th>","</th></tr>")
   print("<body bgcolor><input type=button value='Print' onclick=window.print()></body>")
 if(b1=="Menu"):
  print("<script>window.open('Menu.html','_self')</script>")
except Exception:
        traceback.print_exc()
