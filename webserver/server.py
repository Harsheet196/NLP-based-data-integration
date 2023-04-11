from flask import Flask, request, redirect, url_for
import mysql_mongodb as connector
import mongo_to_mongo as conn2

app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return 'welcome your login success: %s' % name


@app.route('/thanks', methods=['post'])
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


if __name__ == '__main__':
    app.run()
