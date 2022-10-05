from flask import Flask, jsonify, request
import api

app = Flask(__name__)

@app.route("/api/hosts/list")
def apiHostsList():
    response = api.apiHostsList()

    return jsonify(response)

@app.route("/api/hosts/generate")
def apiHostsGenerate():
    response = api.apiHostsGenerate()

    return jsonify(response)

@app.route("/api/hosts/add")
def apiHostsAdd():
    response = api.apiHostsAdd(request.args.get("id"), request.args.get("name"))

    return jsonify(response)

@app.route("/api/hosts/view")
def apiHostsView():
    response = api.apiHostsView(request.args.get("host"))

    return jsonify(response)

@app.route("/api/hosts/delete")
def apiHostsDelete():
    response = api.apiHostsDelete(request.args.get("host"))

    return jsonify(response)

@app.route("/api/tasks/list")
def apiTasksList():
    response = api.apiTasksList()

    return jsonify(response)

@app.route("/api/tasks/view")
def apiTasksView():
    response = api.apiTasksView(request.args.get("host"), request.args.get("task"))

    return jsonify(response)

@app.route("/api/tasks/add", methods=["POST"])
def apiTasksAdd():
    response = api.apiTasksAdd(request.args.get("host"), request.json)

    return jsonify(response)

@app.route("/api/tasks/delete")
def apiTasksDelete():
    response = api.apiTasksDelete(request.args.get("id"))

    return jsonify(response)

@app.route("/api/database/check")
def apiDatabaseCheck():
    response = api.apiDatabaseCheck()

    return jsonify(response)

@app.route("/api/database/settings/view")
def apiDatabaseSettingsView():
    response = api.apiDatabaseSettingsView()

    return jsonify(response)

@app.route("/api/database/settings/modify")
def apiDatabaseSettingsModify():
    response = api.apiDatabaseSettingsModify(request.args.get("host"), request.args.get("user"), request.args.get("password"), request.args.get("database"))

    return jsonify(response)

if __name__ == "__main__":
    app.run()