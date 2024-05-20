from flask import Flask, render_template, jsonify # type: ignore
app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Nairobi',
        'salary': '$ 10000'
    },
    {
        'id': 2,
        'title': 'Software Engineer',
        'location': 'Mombasa',
        'salary': 'Ksh 100002'
    },
    {
        'id': 3,
        'title': 'Devops',
        'location': 'Nyeri',
        'salary': '$ 1050'
    },
    {
        'id': 4,
        'title': 'Networks Engineer',
        'location': 'Kitui',
        'salary': 'Ksh 56667'
    }
]

@app.route("/")
def hello():
    return render_template("home.html", jobs=JOBS)

@app.route('/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=True)
    