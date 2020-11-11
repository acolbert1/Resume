from flask import Flask, render_template
from flask_cors import CORS
from pprint import pprint
import json
import boto3 
import os


app = Flask(__name__)
CORS(app)
app._static_folder = os.path.abspath("templates/static/")
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorCounter')

response = table.get_item(
    Key={
        'Site': 0
    }
)



@app.route('/')
def index():
    item = response['Item']
    print(item)
    count = item['Visits']
    print(count)
    return render_template('index.html', count=count)

@app.route('/my-link/')
def my_link():
  print ('I got clicked!')
  print(table.creation_date_time)
  item = response['Item']
  print(item)
  count = item['Visits']
  print(count)

 
#   table.update_item(
#       Key={
#           'Site': 0,

#       },
#       UpdateExpression='SET Visits = :val1',
#       ExpressionAttributeValues={
#           ':val1': item['Visits'] + 1
#       }
#   )
  return render_template('index.html', count=count)
#   return {
    #   "statusCode": 200,
    #   "body": json.dumps({"Visit_Count": str(item['Visits'] + 1)})
    # }
  
  

  

if __name__ == '__main__':
    app.run(debug=True)


























# app = Flask(__name__)
# # Initialize dynamodb access
# dynamodb = boto3.resource('dynamodb')
# db = dynamodb.Table('visitor-counter')

# @app.route('/counter', methods=['GET'])
# def counter_get():
#     res = db.get_item(Key={'id': 'counter'})
#     return jsonify({'counter': res['Item']['counter_value']})


# @app.route('/counter/increase', methods=['POST'])
# def counter_increase():
#     res = db.get_item(Key={'id': 'counter'})
#     value = res['Item']['counter_value'] + 1  
#     res = db.update_item(
#     Key={'id': 'counter'},
#     UpdateExpression='set counter_value=:value',
#     ExpressionAttributeValues={':value': value},
#     )  
#     return jsonify({'counter': value})
