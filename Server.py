from flask import Flask, render_template, url_for, request
import csv
app = Flask(__name__)
print(__name__)

@app.route('/index.html')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open('Database.csv', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject])

def write_to_file(data):
    with open('Database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        file = database.write(f'\n{email},{subject}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return 'form submitted'
    else:
        return 'something is not right'

