from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Python Developer",
        "location": "New York",
        "salary": "$" + str(5000)
    },
    {
        "id": 2,
        "title": "Web Developer",
        "location": "San Francisco",
        "salary": "$" + str(4000)
    },
    {
        "id": 3,
        "title": "Data Scientist",
        "location": "Chicago",
        "salary": "$" + str(6000)
    },
]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name="Job Finder")


@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
