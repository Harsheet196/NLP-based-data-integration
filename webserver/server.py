from flask import Flask, request, redirect, url_for
import mysql_mongodb as connector
import mongo_to_mongo as conn2
import csv_mongodb as conn3

app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return 'task is: %s' % name


@app.route('/mysql_mongo', methods=['post', 'get'])
def hello_world():
    host_mo = request.form['host_mo']
    host_mysql = request.form['host_mysql']
    client_mo = request.form['client_mo']
    db_mysql = request.form['db_mysql']
    user_mysql = request.form['user_mysql']
    pass_mysql = request.form['pass_mysql']
    val = connector.migrate(host_mo, host_mysql, client_mo,
                            db_mysql, user_mysql, pass_mysql)
    print(val)
    return redirect(url_for('success', name=val))


@app.route('/mongo', methods=['post'])
def new():
    path = request.form['path']
    val = conn2.migrate(path)
    print(val)
    return redirect(url_for('success', name=val))


@app.route('/csv', methods=['post'])
def new2():
    # path = request.form['path']
    val = conn3.mongoimportcsv(
        'C:/Users/Harsheet/Downloads/Github repos/NLP-based-data-integration/connectors/cities_final.csv', 'temp1', 'temp')
    print(val)
    return redirect(url_for('success', name=val))


@app.route('/index', methods=['post'])
def login():
    email = request.form['email']
    password = request.form['password']
    if (email == "harsh@gmail.com" and password == "harsh"):
        print("Successful login")
        return redirect("http://127.0.0.1:5500/webserver/templates/index.html")


if __name__ == '__main__':
    app.run()
