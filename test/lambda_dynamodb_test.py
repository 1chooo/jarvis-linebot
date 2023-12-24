import boto3
import os

aws_access_key_id = 'YOUR_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'
region_name = 'YOUR_REGION'

# 創建 DynamoDB client
dynamodb = boto3.resource(
    'dynamodb', 
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

def lambda_handler(event: any, context: any):

    user: str = event["user"]
    visit_count: int = 0

    # Prepare the DynamoDB client
    dynamodb = boto3.resource("dynamodb")
    table_name = "lambda-dynamodb-test"
    # table_name = os.environ["TABLE_NAME"]
    table = dynamodb.Table(table_name)

    # Get the visit count from the DynamoDB table
    response = table.get_item(Key={"user": user})
    if "Item" in response:
        visit_count = response["Item"]["visit_count"]

    # Increment the visit count and put the item into DynamoDB table.
    visit_count += 1
    table.put_item(Item={"user": user, "visit_count": visit_count})

    message: str = f"Hello {user}! You have visited us {visit_count} times."
    return {"message": message}


if __name__ == "__main__":
    # os.environ["TABLE_NAME"] = "lambda-dynamodb-test"
    test_event = {"user": "1chooo"}
    result = lambda_handler(test_event, None)
    print(result)