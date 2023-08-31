import boto3
import json

def lambda_handler(event, context):
    filepath = event['Records'][0]['s3']['object']['key']
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    data_str = json.dumps(event, indent=4)

    client = boto3.client('sns')

    message = f"New file uploaded ({filepath}) to bucket {bucket_name}.\n\n" \
              f"Please find more details below:\n\n" \
              f"JSON data:\n\n{data_str}"

    client.publish(
        TargetArn='<<sns_topic_arn>>',
        Message= message,
        Subject='File uploaded to Paragon SFTP'
    )
    