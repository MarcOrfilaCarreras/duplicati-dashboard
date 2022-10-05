from flask import Flask
import views, db

app = Flask(__name__)

app.add_url_rule('/', view_func=views.hosts)
app.add_url_rule('/hosts', view_func=views.hosts)
app.add_url_rule('/hosts/add', view_func=views.hostsAdd)
app.add_url_rule('/hosts/<id>', view_func=views.hostView)

app.add_url_rule('/tasks', view_func=views.tasks)

app.add_url_rule('/settings', view_func=views.settings)
app.add_url_rule('/settings/save', view_func=db.settingsSave, methods=["POST"])

app.add_url_rule('/api/hosts/add', view_func=db.hostAdd, methods=["POST"])
app.add_url_rule('/api/send/<id>', view_func=db.taskReceive, methods=["POST"])

if __name__ == "__main__":
    app.run(host='0.0.0.0')