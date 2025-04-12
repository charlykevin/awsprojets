from flask import Flask, request, render_template
import boto3
import os

app = Flask(__name__)

dynamodb = boto3.resource('dynamodb', region_name='ca-central-1')  # Change region as needed
table = dynamodb.Table('UserForm')  # Replace with your actual table name
app.run(host="0.0.0.0", port=5000)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        table.put_item(
            Item={
                'email': email,
                'name': name
            }
        )
        return "Submitted!"
    return render_template('form.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
