''''''
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#mysql connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'n519L323$%'
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql = MySQL(app)

#Settings
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    print(data[0])
    mysql.connection.commit()
    return render_template('index.html', contacts = data)


@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        print('Fulname:')
        print(fullname)
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)', 
        (fullname,phone,email))
        mysql.connection.commit()
        flash('Contact saved sucessfully')
        return redirect(url_for('Index'))

@app.route('/update_contact/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        print('Fulname:')
        print(fullname)
        cur = mysql.connection.cursor()
        cur.execute("""UPDATE contacts 
            SET fullname = %s ,
            phone = %s ,
            email = %s
            WHERE id = %s"""
            , (fullname,phone,email, id))
        mysql.connection.commit()
        flash('Contact Updated sucessfully')
        return redirect(url_for('Index'))

@app.route('/edit/<id>')
def edit(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = {0}'.format(id))
    data = cur.fetchall()
    mysql.connection.commit()
    print(data)
    return render_template('edit_table.html', contact = data[0])

@app.route('/delete/<id>')
def delete(id):
    print(id)
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contact Removed Successfully')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)

print('Hello World')