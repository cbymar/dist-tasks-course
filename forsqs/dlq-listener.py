import json
import time
import os
import yaml
import boto3

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# define path to creds
HOME = os.path.expanduser('~')
CREDS_FILE = os.path.join(HOME + '/credconf.yaml')
with open(CREDS_FILE, 'r') as f:
    creds = yaml.load(f, Loader=yaml.FullLoader)

# creds
KEY = creds['SQS']['KEY']
SECRET = creds['SQS']['SECRET']
SQS_URL = creds['SQS']['DLQURL']

sqs = boto3.client("sqs",
                   region_name="us-west-2",
                   aws_access_key_id=KEY,
                   aws_secret_access_key=SECRET
                   )

if __name__ == "__main__":
    print("Starting DLQ worker listening on {}".format(SQS_URL))
    while True:
        response = sqs.receive_message(
            QueueUrl=SQS_URL,
            AttributeNames=["All"],
            MessageAttributeNames=["string"],
            MaxNumberOfMessages=1,
            WaitTimeSeconds=10,
        )

        messages = response.get("Messages", []) # array type
        for message in messages:
                print("Message Body > ", message.get("Body"))
                sqs.delete_message(QueueUrl=SQS_URL, ReceiptHandle=message.get("ReceiptHandle"))

        time.sleep(5)


print("Worker stopped")


"""
For each message, get the body
Then, act on it, and delete it from the queue.  Deletion is critical. 
We delete using the QueueUrl + ReceiptHandle tuple
"""

