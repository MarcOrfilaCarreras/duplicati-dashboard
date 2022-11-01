from crypt import methods
from flask import Flask
import views

app = Flask(__name__)
app.secret_key = "5#y2LF4Q8z\n\xec]/"

app.add_url_rule('/', view_func=views.viewIndex)
app.add_url_rule('/hosts', view_func=views.viewHostsList)
app.add_url_rule('/hosts/create', view_func=views.viewHostsCreate)
app.add_url_rule('/hosts/create', methods=["POST"], view_func=views.viewHostsCreatePost)
app.add_url_rule('/hosts/view', view_func=views.viewHostsView)
app.add_url_rule('/hosts/delete', view_func=views.viewHostsDelete)

app.add_url_rule('/tasks', view_func=views.viewTasksList)
app.add_url_rule('/tasks/delete', view_func=views.viewTasksDelete)

app.add_url_rule('/settings/view', view_func=views.viewSettingsView)
app.add_url_rule('/settings/modify', methods=["POST"], view_func=views.viewSettingsModify)

if __name__ == "__main__":
    app.run()