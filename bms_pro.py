import pymysql #importing mysql library
from flask import Flask,render_template,request
#Flask class is inbuilt class of flask library
#request inbuilt function of python , to access value from html'control to python
#render_template inbuilt function
app=Flask(__name__)#app user defined object of Flask
#routing is used create the page
@app.route('/') #home page decorator
def hello():
    return '''<div style="background-color:lightpink";>
<h1 align="center" style="color:red;"><strong>Welcome to Bank Management System</strong></h1></div>
              <div style="background-color:cyan";"align:center";><a href="/signup">Sign Up</a></div> <br>
              <div style="background-color:yellow";><a href="/signin">Sign In</a></div>'''

@app.route('/signup')#signup page decorator
def add_signup():
    return render_template('signup.html') #rendering html file from templates folder

@app.route('/saverec',methods=['POST','GET']) #data inserting from user
def save():
    if request.method=='POST' :
        try:
            a=request.form["fname"]
            b=request.form["pno"]
            c=request.form["add"]
            d=request.form["acc_num"]
            e=request.form["acct_p"]
            f=request.form["bal"]
            g=request.form["e_id"]
            h=request.form["uname"]
            i=request.form["pwd"]
            #create connection to bankserver database
            con=pymysql.connect(host="localhost", user='root',password='',database='bankserver')   
            cur=con.cursor()
            #firing query to insert data from web page
            cur.execute("insert into acc_holder_details values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(a,b,c,d,e,f,g,h,i)) 
            con.commit()  #save record permanently into table
            msg="Record successfully Added"
        except:
            msg="Unsuccessful"  
        finally:
            return render_template('success2.html',msg=msg)
        
        
@app.route('/signin')
def add_signin():
    return render_template('signin.html')

@app.route('/login',methods=['POST','GET'])
def validation():
    if request.method=='POST':
        try:
            h=request.form["uname"]
            i=request.form["pwd"]
            #con
            conn=pymysql.connect(host="localhost",user='root',password='',database='bankserver')
            cur=conn.cursor()
            cur.execute("select * from acc_holder_details where username=%s and password=%s",(h,i))
            res=cur.fetchall()#fetching all data into tuple
        except:
            msg="error"
            return render_template("error.html",smsg=msg)
        finally:
            conn.close()
            return render_template("my_display.html",dresult=res)
           
        
@app.route('/delete')
def del_data():
    return render_template('delete.html')

@app.route('/delete1',methods=['POST','GET'])
def delete_record1():
    msg=" "
    if request.method=='POST' :
        try:
            uname=request.form["uname"]
            #create connection
            con= pymysql.connect(host="localhost", user='root',password='',database='bankserver')   
            cur = con.cursor()
            cur.execute("Delete from acc_holder_details where username=%s",(uname))
            con.commit()  #delete record permanently into table
            res=cur.fetchall()#fetching all data into tuple
            msg = "Customer Record successfully Deleted"  
        except:  
            msg = "We can not delete the customer data into table"
            return render_template("error.html",smsg=msg)
        finally:
            con.close()
            return render_template("my_display2.html")
        

@app.route('/view_all')
def displayall():
     #create connection
    try:
            con= pymysql.connect(host="localhost", user='root',password='',database='bankserver')   
            cur = con.cursor()
            cur.execute("Select * from acc_holder_details")
            result=cur.fetchall() #result which hold the all records from table
            con.close()
            return render_template('display.html',result=result)
    except:
        msg="error"
        return render_template("error.html",smsg=msg)

@app.route('/update')
def update_data():
    return render_template('update.html')

@app.route('/update1',methods=['POST','GET'])
def update_record1():
    msg=" "
    if request.method=='POST' :
        try:
            uname=request.form["uname"]
            pwd=request.form["pwd"]
            #create connection
            con= pymysql.connect(host="localhost", user='root',password='',database='bankserver')   
            cur = con.cursor()
            cur.execute("Update acc_holder_details set password=%s where username=%s",(pwd,uname))
            con.commit()  #Update record permanently into table
            res=cur.fetchall()#fetching all data into tuple
            msg = "Customer Record successfully Updated"  
        except:  
            msg = "We can not Update the customer data into table"
            return render_template("error.html",smsg=msg)
        finally:
            con.close()
            return render_template("showupdate.html")



#main program
app.run(debug=True)
