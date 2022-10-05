from flask import Flask, render_template, request
import json
import db

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

def loadConfig():
    try:
        with open("settings.json", "r") as f:
            config = json.load(f)
        return config
    except:
        return {"settings": {"host": "", "user": "", "password": "", "database": ""}}

def hosts():
    return render_template("hosts.html", text=language(), hosts=db.hosts())

def hostsAdd():
    return render_template("hostsAdd.html", text=language(), hostId=db.hostExists())

def hostView(id):
    return render_template("hostView.html", text=language(), tasks=db.hostView(id), id=id)

def tasks():
    return render_template("tasks.html", text=language(), tasks=db.tasksView())

def settings():
    return render_template("settings.html", text=language(), config=loadConfig())