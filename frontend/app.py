from flask import Flask
import dateutil.parser
import views

app = Flask(__name__)
app.secret_key = "5#y2LF4Q8z\n\xec]/"

app.add_url_rule('/', view_func=views.viewIndex)
app.add_url_rule('/stats', view_func=views.viewStats)

app.add_url_rule('/hosts', view_func=views.viewHostsList)
app.add_url_rule('/hosts/create', view_func=views.viewHostsCreate)
app.add_url_rule('/hosts/create', methods=["POST"], view_func=views.viewHostsCreatePost)
app.add_url_rule('/hosts/view', view_func=views.viewHostsView)
app.add_url_rule('/hosts/delete', view_func=views.viewHostsDelete)

app.add_url_rule('/tasks', view_func=views.viewTasksList)
app.add_url_rule('/tasks/view', view_func=views.viewTasksView)
app.add_url_rule('/tasks/delete', view_func=views.viewTasksDelete)

app.add_url_rule('/settings/view', view_func=views.viewSettingsView)
app.add_url_rule('/settings/modify', methods=["POST"], view_func=views.viewSettingsModify)
app.add_url_rule('/settings/check', view_func=views.viewSettingsCheck)

@app.template_filter('strftime')
def _jinja2_filter_datetime(date, fmt=None):
    date = dateutil.parser.parse(date)
    native = date.replace(tzinfo=None)
    format='%d/%m/%Y'
    return native.strftime(format)

if __name__ == "__main__":
    app.run()