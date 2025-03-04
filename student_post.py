import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Students')

def lambda_handler(event, context):
    try:
        print("Incoming event:", event)  # Debugging

        # Check if the request body exists (API Gateway case)
        if "body" in event:
            if isinstance(event["body"], str):  # If it's a string, parse it
                event = json.loads(event["body"])
            else:
                event = event["body"]  # If already a dictionary, use it directly

        # Extract values safely
        student_id = event.get('StudentID')
        name = event.get('name')
        student_class = event.get('class')
        age = event.get('age')

        # Validate required fields
        if not all([student_id, name, student_class, age]):
            return {
                'statusCode': 400,
                'body': json.dumps('Error: Missing required student data fields')
            }

        # Prepare item for DynamoDB
        item = {
            'StudentID': str(student_id),
            'name': str(name),
            'class': str(student_class),
            'age': int(age)
        }
        print("Item to be inserted:", item)

        # Insert data into DynamoDB
        response = table.put_item(Item=item)

        return {
            'statusCode': 200,
            'body': json.dumps('Student data saved successfully!')
        }

    except Exception as e:
        print("Error:", str(e))  # Debugging
        return {
            'statusCode': 500,
            'body': json.dumps(f'Internal Server Error: {str(e)}')
        }
