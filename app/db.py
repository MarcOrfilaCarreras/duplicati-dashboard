from flask import request, redirect, url_for
import json
import random, string
import threading
import mysql.connector

host = None
user = None
password = None
database = None

def loadConfig():
    global host, user, password, database

    try:
        with open("settings.json", "r") as f:
            config = json.load(f)
    except:
        config = {"settings": {"host": "", "user": "", "password": "", "database": ""}}
    
    host = config["settings"]["host"]
    user = config["settings"]["user"]
    password = config["settings"]["password"]
    database = config["settings"]["database"]

def mysqlConnection():
    global host, user, password, database

    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    return mydb

def hosts():
    global host, user, password, database
    try:
        if host is None or user is None or password is None or database is None:
            loadConfig()

        mydb = mysqlConnection()

        cursor = mydb.cursor()

        sql = """SELECT * FROM hosts"""
        cursor.execute(sql)

        result = cursor.fetchall()

        mydb.commit()
        mydb.close()

        return result
    except:
        return iter([])

def hostExists():
    stop = True

    while (stop):
        chars = string.ascii_lowercase + string.digits
        id = ''.join(random.choice(chars) for i in range(12))

        global host, user, password, database
        try:
            if host is None or user is None or password is None or database is None:
                loadConfig()

            mydb = mysqlConnection()

            cursor = mydb.cursor()

            sql = """SELECT 1 FROM hosts where id = (%s)"""
            cursor.execute(sql, (id, ))

            result = cursor.fetchone()

            mydb.commit()
            mydb.close()

            if result is None:
                stop = False
            
            return id
        except:
            return None

def hostAdd():
    global host, user, password, database
    try:
        if host is None or user is None or password is None or database is None:
            loadConfig()

        mydb = mysqlConnection()

        cursor = mydb.cursor()

        sql = """INSERT INTO hosts (id, name) Values ((%s), (%s))"""
        cursor.execute(sql, (request.form['id'], request.form['name']), multi=True)

        mydb.commit()
        mydb.close()

        return redirect(url_for('hosts'))
    except:
        return redirect(url_for('hostsAdd'))

def hostView(id):
    global host, user, password, database
    try:
        if host is None or user is None or password is None or database is None:
            loadConfig()
        
        mydb = mysqlConnection()

        cursor = mydb.cursor()

        sql = """SELECT * FROM tasks where host = (%s)"""
        cursor.execute(sql, (id,))

        result = cursor.fetchall()
        
        mydb.commit()
        mydb.close()

        return result
    except Exception as e:
        print(e)
        return iter([])

def tasksView():
    global host, user, password, database
    try:
        if host is None or user is None or password is None or database is None:
            loadConfig()

        mydb = mysqlConnection()

        cursor = mydb.cursor()

        sql = """SELECT * FROM tasks"""
        cursor.execute(sql)

        result = cursor.fetchall()

        mydb.commit()
        mydb.close()

        return result
    except:
        return iter([])

def taskAdd(id, content):
    content = json.loads(json.dumps(content))

    global host, user, password, database
    try:
        if host is None or user is None or password is None or database is None:
            loadConfig()

        mydb = mysqlConnection()

        cursor = mydb.cursor()

        sql = ()
        cursor.execute("SELECT name FROM tasks where name = '%s' and host = hola" % (id))
        result = cursor.fetchall()

        name = content['Extra']['backup-name']
        hostId = id
        known_file_size = (content['Data']['BackendStatistics']['KnownFileSize'] / 1024) / 1024
        parsed_result = (content['Data']['BackendStatistics']['ParsedResult'])
        backup_list_count = (content['Data']['BackendStatistics']['BackupListCount'])
        
        if not result:
            sql = """INSERT INTO tasks (name, host, known_file_size, parsed_result, backup_list_count) Values ((%s), (%s), (%s), (%s), (%s))"""
            cursor.execute(sql, (name, hostId, known_file_size, parsed_result, backup_list_count), multi=True)
        else:
            sql = """UPDATE tasks SET known_file_size = (%s), parsed_result = (%s), backup_list_count = (%s) WHERE name = (%s) and host = (%s)"""
            cursor.execute(sql, (known_file_size, parsed_result, backup_list_count, name, hostId), multi=True)

        mydb.commit()
        mydb.close()
    except Exception as e:
        pass

def taskReceive(id):
    content = request.get_json(silent=True)

    thread = threading.Thread(target = taskAdd, args=(id, content))
    thread.start()

    return ("", 204)

def settingsSave():
    try:
        host = request.form['host']
        user = request.form['user']
        password = request.form['password']
        database = request.form['database']

        config = {
            "settings": {
                "host": host,
                "user": user,
                "password": password,
                "database": database
            }
        }
        
        # Serializing json
        json_object = json.dumps(config, indent=4)
        
        # Writing to sample.json
        with open("settings.json", "w") as outfile:
            outfile.write(json_object)

        loadConfig()

    except:
        pass
    
    return redirect(url_for('settings'))