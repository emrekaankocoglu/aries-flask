from flask import Flask, request,render_template
from tinydb import TinyDB, Query
db = TinyDB('db.json')
db_feedback = db.table('feedback')
db_contact = db.table('contact')


app = Flask(__name__,
            static_url_path='',
            static_folder='static/pure-hc',
            template_folder='templates')

@app.route('/contact.html', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        formdata = dict(request.form)
        formdata.update({"read":False})
        db_contact.insert(formdata)
        return render_template("success.html", message="Thank you for your message", message_type="success")
    else:
        return render_template("contact.html")
@app.route('/index.html', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/', methods=['GET'])
def ins():
    return render_template("index.html")

@app.route('/fb', methods=['GET','POST'])
def feedback():
    if request.method == 'POST':
        formdata = dict(request.form)
        formdata.update({"read":False, "token" : request.args.get('t')})
        db_feedback.insert(formdata)
        return render_template("success.html", message="Thank you for your message", message_type="success")
    else:
        return render_template("feedback.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)