from flask import render_template, request, redirect, url_for, flash
import json, requests

api = None

def config():  
    global api
    try:
        with open("settings.json") as f:
            data = json.load(f)
        
        f.close()

        api = data["settings"]["api"]

    except FileNotFoundError:
        pass

def language():
    languages = {
        "en": "English",
        "es": "Spanish",
        "ca": "Catalan"
    }

    lang = request.accept_languages.best_match(languages.keys())

    try:
        if lang == "es":
            with open("languages/es.json", "r") as f:
                text = json.load(f)
        elif lang == "ca":
            with open("languages/ca.json", "r") as f:
                text = json.load(f)
        else:
            with open("languages/en.json", "r") as f:
                text = json.load(f)
            
        return text
    except:
        return {}

def viewIndex():
    global api
    if api is None:
            config()

    url = api + "/api/database/check"
    r = requests.get(url)

    return redirect(url_for("viewStats"))

def viewStats():
    global api
    if api is None:
            config()

    url = api + "/api/stats/tasks"
    r = requests.get(url)
    data_tasks = json.loads(r.text)

    url = api + "/api/stats/size"
    r = requests.get(url)
    data_size = json.loads(r.text)
    
    return render_template("stats.html", text=language(), data_tasks=data_tasks, data_size=data_size)

def viewHostsList():
    global api
    if api is None:
            config()

    url = api + "/api/hosts/list"
    r = requests.get(url)
    data = json.loads(r.text)

    return render_template("hosts/list.html", data=data, text=language(), domain=request.url_root)

def viewHostsCreate():
    global api
    if api is None:
            config()

    url = api + "/api/hosts/generate"
    r = requests.get(url)
    data = json.loads(r.text)

    return render_template("hosts/create.html", text=language(), domain=request.url_root, data=data)

def viewHostsCreatePost():
    global api
    if api is None:
            config()

    url = api + "/api/hosts/add?id=" + request.form.get("id") + "&name=" + request.form.get("name")
    r = requests.get(url)
    data = json.loads(r.text)

    flash(data["Data"]["Result"])

    return redirect(url_for("viewHostsList"))

def viewHostsView():
    global api
    if api is None:
            config()

    url = api + "/api/hosts/view?host=" + request.args.get("host")
    r = requests.get(url)
    data = json.loads(r.text)

    return render_template("hosts/view.html", data=data, text=language(), domain=request.url_root, host=request.args.get("host"))

def viewHostsDelete():
    global api
    if api is None:
            config()

    url = api + "/api/hosts/delete?host=" + request.args.get("host")
    r = requests.get(url)
    data = json.loads(r.text)

    flash(data["Data"]["Result"])

    return redirect(url_for("viewHostsList"))

def viewTasksList():
    global api
    if api is None:
            config()

    url = api + "/api/tasks/list"
    r = requests.get(url)
    data = json.loads(r.text)

    return render_template("tasks/list.html", data=data, text=language(), domain=request.url_root, previous_url=request.referrer)

def viewTasksView():
    global api
    if api is None:
            config()

    url = api + "/api/tasks/history?task=" + request.args.get("task")
    r = requests.get(url)
    data_history = json.loads(r.text)

    url = api + "/api/tasks/view?task=" + request.args.get("task")
    r = requests.get(url)
    data = json.loads(r.text)

    return render_template("tasks/view.html", data=data, data_history=data_history, text=language(), domain=request.url_root, previous_url=request.referrer, task=request.args.get("task"))

def viewTasksDelete():
    global api
    if api is None:
            config()

    url = api + "/api/tasks/delete?id=" + request.args.get("id")
    r = requests.get(url)
    data = json.loads(r.text)

    flash(data["Data"]["Result"])

    return redirect(url_for("viewHostsList"))

def viewSettingsView():
    global api
    if api is None:
            config()

    url = api + "/api/database/settings/view"
    r = requests.get(url)
    data = json.loads(r.text)

    return render_template("settings/view.html", data=data, text=language(), domain=request.url_root)

def viewSettingsModify():
    global api
    if api is None:
            config()

    url = api + "/api/database/settings/modify?host=" + request.form.get("host") + "&database=" + request.form.get("database") + "&user=" + request.form.get("user") + "&password=" + request.form.get("password")
    r = requests.get(url)
    data = json.loads(r.text)

    flash(data["Data"]["Result"])

    return redirect(url_for("viewSettingsView"))