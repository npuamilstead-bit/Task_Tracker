#importing flask/using jinja
from flask import Flask, render_template, request

app = Flask(__name__)



#nested dictionary for users/tasks/logins
users = {
"alex": {
    "user ID": "01",
    "username": "alex",
    "email": "alexander.milstead@hashmith.com",
    "password": "12345",
    "task list": ["make a task list", "start school", "ask boran stupid questions"]
},
"boran": {
    "user ID": "02",
    "username": "boran",
    "email": "borancar@hashsmith.com",
    "password": " ",
    "task list": []
}
}
@app.route("/", methods=["GET","POST"])
def home():
    current_user = "alex"
    user_tasks = []

    if request.method == "POST":
        current_user = request.form.get("username")

        if current_user in users:
            user_tasks = users[current_user]["task list"]

    return render_template("index.html", username=current_user, tasks=user_tasks, all_users=users.keys())
if __name__ == "__main__":
    app.run(debug=True, port=5001)
