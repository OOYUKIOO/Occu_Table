import csv, random
from flask import Flask, render_template
hw03 = Flask(__name__)

jobs = dict()
joblist = list()
num = 0.0
percentile = 0.0

with open('occupations.csv','r') as csvfile:
    f = csv.reader(csvfile)
    for row in f:
        if row[0] != 'Job Class' and row[0] != 'Total':
            start = percentile
            percentile += float(row[1])
            val = [float(row[1]),start,percentile]
            jobs[row[0]] = val
            joblist.append(row)
            
def jobPicker():
    num = float(random.random()*percentile)
    for job in jobs:
        if num >= jobs[job][1] and num < jobs[job][2]:
            return job

@hw03.route("/")
def welcome():
    return "Welcome to random job picker"

@hw03.route("/occupations")
def generate():
    j = jobPicker()
    return render_template("table.html", l=joblist, job=j, per=num)


if __name__ == "__main__":
    hw03.debug = True
    hw03.run()
    
    
