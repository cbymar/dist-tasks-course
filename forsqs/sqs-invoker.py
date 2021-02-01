import boto3
import os
import yaml
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# define path to creds
HOME = os.path.expanduser('~')
CREDS_FILE = os.path.join(HOME + '/credconf.yaml')
with open(CREDS_FILE, 'r') as f:
    creds = yaml.load(f, Loader=yaml.FullLoader)

# creds
KEY = creds['SQS']['KEY']
SECRET = creds['SQS']['SECRET']
SQS_URL = creds['SQS']['URL']

sqs = boto3.client("sqs",
                   region_name="us-west-2",
                   aws_access_key_id=KEY,
                   aws_secret_access_key=SECRET
                   )


def send_report_results():
    """"""
    payload = json.dumps(
        {'jobId': 'test01',
         'data': {
             'topping': [
        {'id': '5001', 'type': 'Chery'},
        {'id': '5002', 'type': 'Glazed'},
        {'id': '5005', 'type': 'Sugar'},
        {'id': '5007', 'type': 'Powdered Sugar'},
        {'id': '5006', 'type': 'Chocolate with Sprinkles'},
        {'id': '5003', 'type': 'Chocolate'},
        {'id': '5004', 'type': 'Maple'}
             ]
         }
         }
    )

    response = sqs.send_message(
        QueueUrl=SQS_URL,
        MessageBody=payload
    )

    print(response)
    print("SUCCESS")

send_report_results()
