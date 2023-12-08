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
t8=f.getvalue("t8")
t7=t7+t8
b1=f.getvalue("b1")
try:
 if(b1=="Save"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['patient']
   a=0
   for x in collection.find({}):
    if(x['pat_id']==t1):
     a=1;
     break;
   if(a==1): 
    print("<script>alert('Patient ID already exist')</script>")
    print("<script>window.open('Patient.html','_self')</script>")
   else:
    insert1={'pat_id':t1,'pat_nm':t2,'gender':t3,'nation':t4,'b_date':t5,'con_no':t6,'blood_g':t7}
    collection.insert_one(insert1)
    print("<script>alert('Record Saved...')</script>")
    print("<script>window.open('Patient.html','_self')</script>")
 if(b1=="Delete"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['patient']
   insert1={'pat_id':t1}
   collection.delete_many(insert1)
   print("<script>alert('Record Deleted...')</script>")
   print("<script>window.open('Patient.html','_self')</script>")
 if(b1=="Update"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['patient']
   collection.update_many({'pat_id':t1},{'$set':{'pat_nm':t2,'gender':t3,'nation':t4,'b_date':t5,'con_no':t6,'blood_g':t7}})
   print("<script>alert('Record Updated...')</script>")
   print("<script>window.open('Patient.html','_self')</script>")
 if(b1=="All search"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['patient']
   print("<body bgcolor=pink><table border=2 bgcolor=grey><tr><th>Patient Id</th><th>Patient name</th><th>Gender</th><th>Nationality</th><th> Birth date</th><th>Contact no.</th><th>Blood group</th></tr>")
   for x in collection.find({}):
    print("<tr><th>",x["pat_id"],"</th>","<th>",x["pat_nm"],"</th>","<th>",x["gender"],"</th>","<th>",x["nation"],"</th>","<th>",x["b_date"],"</th>","<th>",x["con_no"],"</th>","<th>",x["blood_g"],"</th>","</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")
 if(b1=="Psearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['hospital']
   collection=db['patient']
   print("<body bgcolor=pink><table border=2 bgcolor=grey><tr><th>Patient Id</th><th>Patient name</th><th>Gender</th><th>Nationality</th><th> Birth date</th><th>Contact no.</th><th>Blood group</th></tr>")
   for x in collection.find({'pat_id':t1}):
    print("<tr><th>",x["pat_id"],"</th>","<th>",x["pat_nm"],"</th>","<th>",x["gender"],"</th>","<th>",x["nation"],"</th>","<th>",x["b_date"],"</th>","<th>",x["con_no"],"</th>","<th>",x["blood_g"],"</th>","</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")
 if(b1=="Menu"):
  print("<script>window.open('Menu.html','_self')</script>")
except Exception:
        traceback.print_exc()
