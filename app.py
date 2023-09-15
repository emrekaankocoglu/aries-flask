from flask import Flask, request,render_template
from tinydb import TinyDB, Query
db = TinyDB('db.json')


app = Flask(__name__,
            static_url_path='',
            static_folder='static/pure-hc',
            template_folder='templates')

@app.route('/contact.html', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        print(request.form)
        db.insert(request.form)
        return render_template("contact.html", message="Thank you for your message", message_type="success")
    else:
        return render_template("contact.html")
@app.route('/index.html', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/', methods=['GET'])
def ins():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)