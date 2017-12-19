#!flask/bin/python
from flask import request, abort, Flask, jsonify
import subprocess

submit_post = Flask(__name__)

tasks = [{
        'id': 0,
        'title': u'',
        'done': False
    }
]

def runjob(job_name):
    cmd = "python runjob.py " + job_name
    subprocess.call(cmd.split())

@submit_post.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'done': False
    }
    runjob(request.json['title'])
    tasks.append(task)
    return jsonify({'tasks': task}), 201

if __name__ == '__main__':
    submit_post.run(host='172.22.132.19', port=5000, debug=True)

