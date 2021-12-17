import pickle
from flask import Flask, render_template, jsonify, request
from datetime import datetime
from processor import mail_process
import copy
import os

app = Flask(__name__)
counter_account = 0
mail_dict = {}


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html", n_account=counter_account)


@app.route("/api/add-mail", methods=['POST'])
def predict():
    global counter_account
    if request.json:
        # predict image
        result = mail_process.save_mail(
            request.json, mail_dict, counter_account)
        counter_account += 1
        print('Success!')
        return jsonify({'result': 'success'})
    print('Fail!')
    return jsonify({'result': 'fail'})


@app.route("/reset-counter", methods=['GET'])
def reset_counter():
    global counter_account
    counter_account = 0


@app.route("/get-account", methods=['GET'])
def get_account():
    store_acc = copy.deepcopy(mail_dict)
    for _, _, filenames in os.walk('./store'):
        break
    for name in filenames:
        with open('./store/'+name, 'rb') as f:
            accs = pickle.load(f)
            store_acc.update(accs)
    return jsonify(store_acc)


@app.route("/delete-account", methods=['GET'])
def delete_account():
    global mail_dict, counter_account
    for _, _, filenames in os.walk('./store'):
        break
    for name in filenames:
        os.remove('./store/'+name)
    mail_dict = dict()
    counter_account = 0
    return jsonify({'delete': 'success'})


@app.route("/shutdown", methods=['GET'])
def shutdown():
    '''Shutdown the server'''
    shutdown_func = request.environ.get('werkzeug.server.shutdown')
    if shutdown_func is None:
        raise RuntimeError('Not running werkzeug')
    shutdown_func()
    return "Shutting down..."


if __name__ == "__main__":
    app.run(debug=False)
