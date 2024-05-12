from flask import Flask, render_template, request, redirect, flash
import mysql.connector

app = Flask(_name_)

# Connect to MySQL database
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="pinki12345",
    database="ShoppingZone"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin_login():
    error = None
    if request.method == 'POST':
        admin_name = request.form['admin_name']
        password = request.form['password']
        if admin_name == 'admin' and password == 'pass':
            return redirect('/admin_dashboard')
        else:
            error = 'Incorrect admin name or password. Please try again.'
    return render_template('admin_login.html', error=error)


@app.route('/customer', methods=['GET', 'POST'])
def customer_login():
    error = None
    if request.method == 'POST':
        customerID = request.form['customerID']
        password = request.form['password']
        cursor = db.cursor()
        cursor.execute("SELECT * FROM customer WHERE customerID = %s AND password = %s", (customerID, password))
        customer = cursor.fetchone()
        if customer:
            return redirect('/customer_dashboard')
        else:
            error = 'Incorrect customer ID or password. Please try again.'
    return render_template('customer_login.html', error=error)


@app.route('/admin_dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')

@app.route('/orders')
def orders():
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(orderID) AS order_count FROM order")
    result = cursor.fetchone()[0]
    return f"<div style='font-size: 40px; font-weight: bold;'>Total Number of orders placed: {result}</div>"

@app.route('/products')
def products():
    cursor = db.cursor()
    cursor.execute("SELECT p.productID, p.name AS product_name, s.ownerID, s.name AS supplier_name FROM product p JOIN sells sp ON p.productID = sp.productID JOIN shopOwner s ON sp.ownerID = s.ownerID")
    results = cursor.fetchall()
    return render_template('products.html', products=results)

if _name_ == '_main_':
    app.run(debug=True)