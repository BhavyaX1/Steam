import mysql.connector
import random
from prettytable import PrettyTable
con=mysql.connector.connect(host="localhost",user="root",password="bhavya579",database="steamproject")
cur=con.cursor()
print("--------------------------------------------------------")
print("-------------------------LOGIN--------------------------")
print("--------------------------------------------------------")
print()
print("Please select 1 to  LOGIN if you are already a user")
print("Please select 2 to  REGISTER yourself as a new user")
print("Please select 3 to  LOGIN if you are the ADMIN")
print()

choice=int(input("Enter Your Choice:"))
print()

u=input("Enter the your user name:")

def Admin_menu():
print("--------------------------------------------------------")
print("--------------------------------Main menu--------------------------------")
print("---------------------------------------------------------")
print("1. Display All Game")
print("2. Display All DLC")
print("3. Add Game")
print("4. Add DLC")
print("5. Delete Game ")
print("6. Delete DLC")
print("7. Update Game Price")
print("8. Update DLC Price")
print("9. Exit")
print("---------------------------------------------------------")
a=int(input("Enter your Choice:"))
if(a==1):
cur=con.cursor()
cur.execute("Select * from games")
result=cur.fetchall()
t=PrettyTable(['G_ID','Name','Publisher','Price','Category'])
for i in result:
gid=i[0]
name=i[1]
pub=i[2]
pr=i[3]
cat=i[4]
t.add_row([gid,name,pub,pr,cat])
print(t)
Admin_menu()
elif(a==2):
cur=con.cursor()
cur.execute("Select * from dlc")
result=cur.fetchall()
t=PrettyTable(['D_ID','Name','DLC_Name','DLC_Price'])
for i in result:
did=i[0]
name=i[1]
dname=i[2]
dpr=i[3]
t.add_row([did,name,dname,dpr])
print(t)
Admin_menu()
elif(a==3):
print("-------------------------------------------------------")
print("******************Enter Details of Game*************")
print("--------------------------------------------------------")
R=input("Enter the ID of the game:")
N=input("ENter the Name of the game:")
F=input("Enter the Name of Publisher:")
D=input("Enter the Price of the Game:")
J=input("Enter the Category of the Game:")
cur=con.cursor()
sql="insert into games values(%s,%s,%s,%s,%s)"
cur.execute(sql,(R,N,F,D,J))
con.commit()
print("\t\t\t Information Saved")
print("---------------------------------------------------------")
Admin_menu()
elif(a==4):
print("-------------------------------------------------------")
print("******************Enter Details of DLC*************")
print("--------------------------------------------------------")
R=input("Enter the ID of the DLC:")
N=input("ENter the Name of the Game who's DLC you want to add:")
F=input("Enter the Name of DLC:")
D=input("Enter the Price of the DLC:")
cur=con.cursor()
sql="insert into dlc values(%s,%s,%s,%s)"
value=(R,N,F,D)
cur.execute(sql,(value,))
con.commit()
print("\t\t\t Information Saved")
print("---------------------------------------------------------")
Admin_menu()

elif(a==5):
r_1=input("Enter Game_ID  whose information you want to delete:")
cur=con.cursor()
cur.execute("delete from games where G_ID="+r_1)
con.commit()
print("\t\t\tRecord Deleted Successfully")
print("---------------------------------------------------------")
Admin_menu()

elif(a==6):
r_1=input("Enter DLC_ID whose information you want to delete:")
cur=con.cursor()
cur.execute("delete from dlc where G_ID="+r_1)
con.commit()
print("\t\t\tRecord Deleted Successfully")
print("---------------------------------------------------------")
Admin_menu()

elif(a==7):
r_1=input("Enter Game_ID  whose Price you want to Update=")
New=input("New Price:")
cur=con.cursor()
cur.execute("update Students set Fee= %s where Rollno=%s" %(New,r_1))
con.commit()
cur.execute("select * from students where Rollno= %s" %(r_1,))
result=cur.fetchall()
t=PrettyTable(['G_ID','Name','Publisher','Price'])
for i in result:
gid=i[0]
name=i[1]
pub=i[2]
pr=i[3]
cat=i[4]
t.add_row([gid,name,pub,pr,cat])
print(t)
Admin_menu()

elif(a==8):
r_1=input("Enter DLC_ID  whose Price you want to Update=")
New=input("New Price of the DLC:")
cur=con.cursor()
cur.execute("update Students set Fee= %s where Rollno=%s" %(New,r_1))
con.commit()
cur.execute("select * from students where Rollno= %s" %(r_1,))
result=cur.fetchall()
t=PrettyTable(['D_ID','Name','DLC_Name','DLC_Price'])
for i in result:
did=i[0]
name=i[1]
dname=i[2]
dpr=i[3]
t.add_row([did,name,dname,dpr])
print(t)
Admin_menu()




def user(o):
if choice==1:
q="select User_Name,password from login where User_Name= %s"
cur.execute(q,(o,))
f=cur.fetchall()
p=input("Enter your password:")
for i in f :
if i[1]==p:
print()
print("--------------------------------------------------------")
print("--------------------WELCOME TO STEAM--------------------")
print("--------------------------------------------------------")

print()
menu()
flag=1
else:
print("Incorrect password")
elif choice==2:
u=input("Enter your username:")
p=input("Enter your password:")
q="insert into login values(%s,%s)"
cur.execute(q,(u,p))
cur.execute(h,(u,))
print("Your Account has been created:")


def menu():
c='y'
while (c=='y'):
print("********************************************************")
print("***********************MAIN__MENU***********************")
print("********************************************************")
print()
print("1. ALL GAMES ")
print("2. ALL DLC ")
print("3. Catories")
print("4. Search Game")
print("5. Search DLC")
print("6. ADD game to your cart and checkout")
print("7. YOUR transition history")
print("8. Search in Transition history")
print("9. Exit The Application")
print()
c=int(input("Enter your choice:"))
if c==1:
print()
games()
print()
menu()
elif c==2:
print()
dlc()
print()
menu()
elif c==3:
print()
category()
print()
menu()
elif c==4:
print()
search()
print()
menu()
elif c==5:
print()
d_search()
print()
menu()
elif c==6:
print()
add(u)
print()
menu()
elif c==7:
print()
history(u)
print()
menu()
elif c==8:
print()
search_history(u)
print()
menu()
elif c==9:
print()
ch=input("Are you sure you want to leave the applicatiuon:")
if ch=="Yes"or "y"or"yes":
exit()
else:
menu()

def games():
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="bhavya579",database="steamproject")
cur=con.cursor()
q="select * from games"
f=cur.execute(q)
g=cur.fetchall()
t=PrettyTable(['G_ID',"Name","Publisher","Price","Category"])
for i in g:
gid=i[0]
name=i[1]
pub=i[2]
price=i[3]
cate=i[4]
t.add_row([gid,name,pub,price,cate])
print(t)
def dlc():
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="bhavya579",database="steamproject")
cur=con.cursor()
q="select * from dlc"
f=cur.execute(q)
g=cur.fetchall()
t=PrettyTable(['D_ID',"Name","DLC_Name","DLC_Price",])
for i in g:
did=i[0]
name=i[1]
dname=i[2]
dprice=i[3]

t.add_row([did,name,dname,dprice])
print(t)
def category():
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="bhavya579",database="steamproject")
cur=con.cursor()
print("1. Action")
print("2. Adventure")
print("3. FPS")
print("4. Racing")
print("5. Fighting")
y=input("Enter the preferred category")
q="select * from games where category = %s"
cur.execute(q,(y,))
k=cur.fetchall()
p=PrettyTable(['G_ID',"Name","Publisher","Price","Category"])
for i in k:
gid=i[0]
name=i[1]
pub=i[2]
price=i[3]
cate=i[4]
p.add_row([gid,name,pub,price,cate])
print(p)
def search():
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="bhavya579",database="steamproject")
cur=con.cursor()
y=input("Enter the Game")
q="select * from games where name = %s"
cur.execute(q,(y,))
k=cur.fetchall()
p=PrettyTable(['G_ID',"Name","Publisher","Price","Category"])
for i in k:
gid=i[0]
name=i[1]
pub=i[2]
price=i[3]
cate=i[4]
p.add_row([gid,name,pub,price,cate])
print(p)
def d_search():
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="bhavya579",database="steamproject")
cur=con.cursor()
y=input("Enter the Game")
q="select * from dlc group by Name having Name=%s"
cur.execute(q,(y,))
k=cur.fetchall()
t=PrettyTable(['D_ID',"Name","DLC_Name","DLC_Price",])
for i in k:
did=i[0]
name=i[1]
dname=i[2]
dprice=i[3]
t.add_row([did,name,dname,dprice])
print(t)
def add(u):
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="bhavya579",database="steamproject")
cur=con.cursor()
g=int(input("Please enter the ID of the Game you want to add to your cart: "))
w="select Name , price from games where G_Id=%s"
r=cur.execute(w,(g,))
f=cur.fetchall()
for i in f:
n=i[0]
gp=i[1]
print()
d=int(input("Please enter the ID of the DLC you want to add to your cart: "))
y="select DLC_Name,DLC_price from dlc where D_id=%s"
cur.execute(y,(d,))
l=cur.fetchall()
for i in l:
dn=i[0]
dp=i[1]
total=gp+dp


k="select Id,User_name from login where User_Name = '%s'"%(u,)
cur.execute(k)
a=cur.fetchall()
for i in a:
di=i[0]
un=i[1]
bid=random.randint(100,999)
j="insert into tran values(%s,%s,'%s','%s',%s,'%s',%s,%s)"%(bid,di,un,n,gp,dn,dp,total)
cur.execute(j)
con.commit()


t=PrettyTable(["B_ID","ID","User_Name","Name","Price","DLC_Name","DLC_Price","Amount",])

B_ID=bid
Id=di
User_name=un
Name=n
Price=gp
DLC_Name=dn
DLC_Price=dp
Amount=total
t.add_row([B_ID ,Id,User_name,Name,Price,DLC_Name,DLC_Price,Amount])
print()
print(t)

def history(u):
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="bhavya579",database="steamproject")
cur=con.cursor()
o="select * from tran where User_Name=%s"
cur.execute(o,(u,))
hi=cur.fetchall()
t=PrettyTable(["B_ID","Name","Price","DLC_Name","DLC_Price","Amount",])
for i in hi:
B_ID=i[0]
Name=i[3]
Price=i[4]
DLC_Name=i[5]
DLC_Price=i[6]
Amount=i[7]
t.add_row([B_ID,Name,Price,DLC_Name,DLC_Price,Amount])
print(t)

def search_history(u):
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="bhavya579",database="steamproject")
cur=con.cursor()
b=int(input("Please enter the Bill ID you ant to search: "))
o="select * from tran group by User_Name having User_Name=%s and B_ID=%s"
cur.execute(o,(u,b))
hi=cur.fetchall()

t=PrettyTable(["B_ID","Name","Price","DLC_Name","DLC_Price","Amount",])
for i in hi:
B_ID=i[0]
Name=i[3]
Price=i[4]
DLC_Name=i[5]
DLC_Price=i[6]
Amount=i[7]
t.add_row([B_ID,Name,Price,DLC_Name,DLC_Price,Amount]
if choice ==1:
user(u)
else:
Admin_menu()

con.commit()
