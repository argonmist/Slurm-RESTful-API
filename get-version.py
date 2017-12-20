#!flask/bin/python
import subprocess
import os
from flask import Flask, jsonify
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('tls/self-signed.crt', 'tls/private.key')

app = Flask(__name__)

cmd = "python ./version.py"
subprocess.call(cmd.split())
fo = open('/home/slurm/todo-api/logs/tmp', 'r')
version = fo.readlines()
fo.close()

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'version': version})

if __name__ == '__main__':
    app.run(host='172.22.132.19', port=5001 , ssl_context=context, debug=True)

