import json, random, string
import pymysql

host = None
user = None
password = None
database = None

def loadSettings():
    global host, user, password, database

    try:
        with open("settings.json", "r") as f:
            config = json.load(f)
    
    except FileNotFoundError:
        config = {"settings": {"host": "", "user": "", "password": "", "database": ""}}
        
        with open("settings.json", "w") as f:
            f.write(json.dumps(config, indent=4))
    except:
        pass

    host = config["settings"]["host"]
    user = config["settings"]["user"]
    password = config["settings"]["password"]
    database = config["settings"]["database"]

def databaseConnection():
    global host, user, password, database

    db = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    return db

def apiHostsList():
    global host, user, password, database
    try:
        if host is None or user is None or password is None or database is None:
            loadSettings()

        db = databaseConnection()

        cursor = db.cursor()

        sql = """SELECT * FROM hosts"""
        cursor.execute(sql)

        result = cursor.fetchall()

        response = {"Data": {}}

        for row in result:
            host_json = {"Name": row[1], "DateCreated": row[2], "LastBackup": row[3]}
            response["Data"][row[0]] = host_json

        db.commit()
        db.close()
    except pymysql.Error as e:
            response = {"Data": {"Status": "Bad", "Result": e.args[1]}}

    except Exception as e:
        response = {"Data": {"Status": "Bad", "Result": "There was an error when connecting to the database"}}
    
    return response

def apiHostsGenerate():
    stop = True

    while (stop):
        chars = string.ascii_lowercase + string.digits
        id = ''.join(random.choice(chars) for i in range(12))

        global host, user, password, database

        try:
            if host is None or user is None or password is None or database is None:
                loadSettings()

            db = databaseConnection()

            cursor = db.cursor()

            sql = """SELECT 1 FROM hosts where id = (%s)"""
            cursor.execute(sql, (id, ))

            result = cursor.fetchone()

            db.commit()
            db.close()

            if result is None:
                stop = False
                response = {"Data": {"Status": "Ok", "Result": id}}

        except pymysql.Error as e:
            stop = False
            response = {"Data": {"Status": "Bad", "Result": e.args[1]}}

        except Exception as e:
            response = {"Data": {"Status": "Bad", "Result": "There was an error when connecting to the database"}}
    
    return response

def apiHostsAdd(id, name):
    global host, user, password, database
    try:
        if host is None or user is None or password is None or database is None:
            loadSettings()

        db = databaseConnection()

        cursor = db.cursor()

        sql = """INSERT INTO hosts (id, name) Values ((%s), (%s))"""
        cursor.execute(sql, (id, name))

        response = {"Data": {"Status": "Ok", "Result": "The host was added to the database"}}

        db.commit()
        db.close()
    except pymysql.Error as e:
            response = {"Data": {"Status": "Bad", "Result": e.args[1]}}

    except Exception as e:
        response = {"Data": {"Status": "Bad", "Result": "There was an error when connecting to the database"}}
    
    return response

def apiHostsView(host_id):
    global host, user, password, database
    try:
        if host is None or user is None or password is None or database is None:
            loadSettings()
        
        db = databaseConnection()

        cursor = db.cursor()

        sql = """SELECT * FROM tasks where host = (%s)"""
        
        cursor.execute(sql, (host_id, ))

        result = cursor.fetchall()

        response = {"Data": {}}

        for row in result:
            host_json = {"Name": row[1],"Host": row[2], "DateCreated": row[3], "LastBackup": row[4], "KnownFileSize": row[5], "ParsedResult": row[6], "BackupCountList": row[7]}
            response["Data"][row[0]] = host_json
        
        db.commit()
        db.close()
    except pymysql.Error as e:
            response = {"Data": {"Status": "Bad", "Result": e.args[1]}}

    except Exception as e:
        response = {"Data": {"Status": "Bad", "Result": "There was an error when connecting to the database"}}
    
    return response

def apiHostsDelete(host_id):
    global host, user, password, database
    try:
        if host is None or user is None or password is None or database is None:
            loadSettings()
        
        db = databaseConnection()

        cursor = db.cursor()

        sql = """DELETE FROM hosts WHERE id = (%s)"""
        
        cursor.execute(sql, (host_id, ))

        if cursor.rowcount == 1:
            response = {"Data": {"Status": "Ok", "Result": "The host was deleted from the database"}}
        else:
            response = {"Data": {"Status": "Bad", "Result": "The host was not deleted from the database"}}

        db.commit()
        db.close()

    except pymysql.Error as e:
            response = {"Data": {"Status": "Bad", "Result": e.args[1]}}

    except Exception as e:
        response = {"Data": {"Status": "Bad", "Result": "There was an error when connecting to the database"}}
    
    return response

def apiTasksList():
    global host, user, password, database
    try:
        if host is None or user is None or password is None or database is None:
            loadSettings()

        db = databaseConnection()

        cursor = db.cursor()

        sql = """SELECT * FROM tasks"""
        cursor.execute(sql)

        result = cursor.fetchall()

        response = {"Data": {}}

        for row in result:
            host_json = {"Name": row[1],"Host": row[2], "DateCreated": row[3], "LastBackup": row[4], "KnownFileSize": row[5], "ParsedResult": row[6], "BackupCountList": row[7]}
            response["Data"][row[0]] = host_json

        db.commit()
        db.close()

        return response
    except pymysql.Error as e:
            response = {"Data": {"Status": "Bad", "Result": e.args[1]}}

    except Exception as e:
        response = {"Data": {"Status": "Bad", "Result": "There was an error when connecting to the database"}}
    
    return response

def apiTasksView(host_id, task_id):
    global host, user, password, database
    response = {}
    try:
        if host is None or user is None or password is None or database is None:
            loadSettings()

        db = databaseConnection()

        cursor = db.cursor()

        sql = """SELECT * FROM tasks where id = (%s) and host = (%s)"""
        cursor.execute(sql, (task_id, host_id))

        result = cursor.fetchall()

        response = {"Data": {}}

        for row in result:
            host_json = {"Name": row[1],"Host": row[2], "DateCreated": row[3], "LastBackup": row[4], "KnownFileSize": row[5], "ParsedResult": row[6], "BackupCountList": row[7]}
            response["Data"][row[0]] = host_json

        db.commit()
        db.close()
    except pymysql.Error as e:
            response = {"Data": {"Status": "Bad", "Result": e.args[1]}}

    except Exception as e:
        response = {"Data": {"Status": "Bad", "Result": "There was an error when connecting to the database"}}
    
    return response

def apiTasksAdd(host_id, content):
    global host, user, password, database
    try:
        if host is None or user is None or password is None or database is None:
            loadSettings()

        db = databaseConnection()

        cursor = db.cursor()

        name = content['Extra']['backup-name']
        known_file_size = round((content['Data']['BackendStatistics']['KnownFileSize'] / 1024) / 1024, 2)
        parsed_result = (content['Data']['BackendStatistics']['ParsedResult'])
        backup_list_count = (content['Data']['BackendStatistics']['BackupListCount'])

        sql = """SELECT name FROM tasks where name = (%s) and host = (%s)"""
        cursor.execute(sql, (name, host_id))
        result = cursor.fetchall()

        if not result:
            sql = """INSERT INTO tasks (name, host, last_backup, known_file_size, parsed_result, backup_count_list) Values ((%s), (%s), current_timestamp(), (%s), (%s), (%s))"""
            cursor.execute(sql, (name, host_id, known_file_size, parsed_result, backup_list_count))
            response = {"Data": {"Status": "Ok", "Result": "The task was added to the database"}}
        else:
            sql = """UPDATE tasks SET last_backup = current_timestamp(), known_file_size = (%s), parsed_result = (%s), backup_count_list = (%s) WHERE name = (%s) and host = (%s)"""
            cursor.execute(sql, (known_file_size, parsed_result, backup_list_count, name, host_id))
            response = {"Data": {"Status": "Ok", "Result": "The task was updated in the database"}}

        db.commit()
        db.close()
    except pymysql.Error as e:
            response = {"Data": {"Status": "Bad", "Result": e.args[1]}}

    except Exception as e:
        response = {"Data": {"Status": "Bad", "Result": "There was an error when connecting to the database"}}
    
    return response

def apiTasksDelete(task):
    global host, user, password, database
    try:
        if host is None or user is None or password is None or database is None:
            loadSettings()
        
        db = databaseConnection()

        cursor = db.cursor()
        sql = """DELETE FROM tasks WHERE id = (%s)"""
        
        cursor.execute(sql, (task, ))

        if cursor.rowcount == 1:
            response = {"Data": {"Status": "Ok", "Result": "The task was deleted from the database"}}
        else:
            response = {"Data": {"Status": "Bad", "Result": "The task was not deleted from the database"}}
        db.commit()
        db.close()
    except pymysql.Error as e:
            response = {"Data": {"Status": "Bad", "Result": e.args[1]}}

    except Exception as e:
        response = {"Data": {"Status": "Bad", "Result": "There was an error when connecting to the database"}}
    
    return response

def apiDatabaseCheck():
    global host, user, password, database

    response = {"Data": {"Status": "Ok", "Results": {"Hosts": "", "Tasks": ""}}}
    try:
        if host is None or user is None or password is None or database is None:
            loadSettings()

        db = databaseConnection()

        cursor = db.cursor()

        try:
            sql="""SELECT 1 FROM hosts"""
            cursor.execute(sql)

            result = cursor.fetchall()

            if result == []:
                response["Data"]["Results"]["Hosts"] = "The database exists but is empty"
            else:
                response["Data"]["Results"]["Hosts"] = "The database exists and has data"

        except pymysql.Error as e:
            if e.args[0] == 1146:
                sql = """CREATE TABLE IF NOT EXISTS hosts (id varchar(12) NOT NULL PRIMARY KEY, name varchar(200) NOT NULL, date_created datetime NOT NULL DEFAULT current_timestamp(), last_backup datetime DEFAULT NULL);"""
                cursor.execute(sql)
                
                response["Data"]["Results"]["Hosts"] = "The database did not exist but has been created and is empty"
        
        try:
            sql="""SELECT 1 FROM tasks"""
            cursor.execute(sql)

            result = cursor.fetchall()

            if result == []:
                response["Data"]["Results"]["Tasks"] = "The database exists but is empty"
            else:
                response["Data"]["Results"]["Tasks"] = "The database exists and has data"

        except pymysql.Error as e:
            if e.args[0] == 1146:
                sql = """CREATE TABLE IF NOT EXISTS tasks (id int(12) NOT NULL PRIMARY KEY AUTO_INCREMENT, name varchar(200) NOT NULL, host varchar(12) NOT NULL REFERENCES hosts(id) ON DELETE CASCADE ON UPDATE CASCADE, date_created datetime NOT NULL DEFAULT current_timestamp(), last_backup datetime DEFAULT NULL, known_file_size float NOT NULL DEFAULT 0, parsed_result varchar(50), backup_count_list int(11) NOT NULL DEFAULT 0);"""
                cursor.execute(sql)
                
                response["Data"]["Results"]["Tasks"] = "The database did not exist but has been created and is empty"
        db.commit()
        db.close()

        return response
            
    except Exception as e:
        response = {"Data": {"Status": "Bad", "Result": "There was an error when connecting to the database"}}
        return response

def apiDatabaseSettingsView():
    global host, user, password, database
    
    response = {"settings": {"host": host, "user": user, "password": password, "database": database}}

    return response

def apiDatabaseSettingsModify(host, user, password, database):
    if not host is None and not user is None and not password is None and not database is None:
        try:
            config = {
                "settings": {
                    "host": host,
                    "user": user,
                    "password": password,
                    "database": database
                }
            }
            
            json_object = json.dumps(config, indent=4)
            
            with open("settings.json", "w") as outfile:
                outfile.write(json_object)

            loadSettings()

            response = {"Data": {"Status": "Ok", "Result": "The settings have been modified"}}

        except:
            response = {"Data": {"Status": "Bad", "Result": "The settings have not been modified"}}
    else:
        response = {"Data": {"Status": "Bad", "Result": "The settings have not been modified because one or more arguments where null"}}    
    return response
