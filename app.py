from flask import Flask
from flask_dynamo import Dynamo
import redis
from time import strftime, localtime

# def create_app():
#     app = Flask(__name__)
#     app.config['DYNAMO_TABLES'] = [
#         dict(
#             TableName='visitor_counter',
#             KeySchema=[dict(AttributeName='counter', KeyType='HASH')],
#             AttributeDefinitions=[dict(AttributeName='counter', AttributeType='S')],
#             ProvisionedThroughput=dict(ReadCapacityUnits=5, WriteCapacityUnits=5)
#         ) 
#     ]

#     dynamo = Dynamo()
#     dynamo.init_app(app)
#     with app.app_context():
#         dynamo.create_all()
#     return app

# app = create_app()




r = redis.Redis(host='visitor-counter.gjtcg3.0001.use1.cache.amazonaws.com', port=6379, db=0,
            ssl=True,
            ssl_cert_reqs=None)


strftime("key:%Y%m%d%H", localtime())
r.incr(strftime("key:%Y%m%d%H", localtime()))