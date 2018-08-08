import os
import json
from datetime import datetime
from time_range import TimeRange, TimeRangeList
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def format_range(h1, m1, h2, m2):
  start = '{}:{}'.format(h1,m1)
  end = '{}:{}'.format(h2,m2)
  return TimeRange(datetime.strptime(start, "%H:%M") , datetime.strptime(end, "%H:%M"))

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/subtract', methods=['POST'])
def subtract():
  ranges = request.json
  #Instantiate lists of time ranges
  a = TimeRangeList()
  b = TimeRangeList()
  #Load the a ranges
  for value in ranges['a']:
    a.insert(format_range(value['h1'],value['m1'], value['h2'], value['m2']))
  for value in ranges['b']:
    b.insert(format_range(value['h1'],value['m1'], value['h2'], value['m2']))
  #Sort the lists (a log a + b log b)
  a.sort()
  b.sort()
  #Subtract the arrays (a + b)
  a.subtract(b)
  return json.dumps(a.to_array())

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
