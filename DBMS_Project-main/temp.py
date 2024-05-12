# conn = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='udmysql@@2005',
#     database='Retail_store',
#     port=3306
# )


from flask import Flask, render_template, request, redirect, url_for
import pymysql


app = Flask(__name__)

# Connect to MySQL database
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='udmysql@@2005',
    database='Retail_store',
    port=3306
)

@app.route('/')
def index():
    return render_template('wow.html')

li=['customer','shop','Customer']


@app.route('/button_click', methods=['POST'])
def button_click():
    role = request.form['role']
    if role=='admin':
        li[0]='admin'
        li[2] = 'Admin'
        li[1]="admin"
    elif role == 'vendor':
        li[0]='Vendor'
        li[2] = 'Vendor'
        li[1]="Vendorpage"
    elif role == 'customer':
        print("hello cutomer")
        li[0]='customer'
        li[2] = 'Customer'
        li[1]="shop"
    else:
        print('Invalid role')
    print("button click ",role)
    return role

print("print is ",li[1])

@app.route('/login', methods=['GET', 'POST'])
def login():
    print("camehere1")
    if request.method == 'POST':
        print("camehere2")
        # role = request.form['adminForm']
        username = request.form[li[0]+'Username']
        password = request.form[li[0]+'Password']
        print("camehere2")
        print(username+" "+password+" "+li[0])
        try:
            if conn.open:
                with conn.cursor() as cursor:
                    if(li[0]=="customer"):
                        query = f"SELECT * FROM {li[2]} WHERE email_id=%s AND Cust_pass=%s"
                    elif (li[0]=="Vendor"):
                        query = f"SELECT * FROM {li[2]} WHERE E_Mail=%s AND Pass=%s"
                    else:
                        query = f"SELECT * FROM {li[2]} WHERE Mail=%s AND Pass=%s"
                    cursor.execute(query, (username, password))
                    user = cursor.fetchone()
                    if user:
                        print("camehere2")
                        # Redirect to dashboard or specific page based on role
                        
                        return redirect("/"+li[0]+"_dashboard")
                    else:
                        return 'Invalid credentials'
            else:
                return 'Connection to database failed'
        except Exception as e:
            print("Error:", e)

    return render_template('wow.html') #

@app.route('/admin_dashboard')
def admin_dashboard():
    try:
        if conn.open:
            with conn.cursor() as cursor:
                query1 = "SELECT * FROM Customer"
                query2= "SELECT * FROM Item" # Assuming the columns are Name, Email, Phone
                query3 = "SELECT * FROM Vendor"
                cursor.execute(query1)
                cust_data = cursor.fetchall()
                cursor.execute(query2)
                item_data= cursor.fetchall()
                cursor.execute(query3)
                vendor_data=cursor.fetchall()
                return render_template('admin.html', data=[cust_data,item_data,vendor_data])
        else:
            return 'Connection to database failed'
    except Exception as e:
        print("Error:", e)
        return 'An error occurred while fetching data from the database'


@app.route('/vendor_dashboard')
def vendor_dashboard():
    # Add logic for vendor dashboard
    return render_template('vendorpage.html')

@app.route('/customer_dashboard')
def customer_dashboard():
    # Add logic for customer dashboard
    print("tarandeep is here")
    return render_template('shop.html')

if __name__ == '__main__':
    app.run(debug=True)
