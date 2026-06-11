import json


def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
        name = body.get('name', 'Unknown')
        email = body.get('email', 'No email')
        message = body.get('message', 'No message')

        print(f"Contact Form Submission - Name: {name}, Email: {email}")

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'success': True,
                'message': f'Thank you {name}! Your message has been received.'
            })
        }

    except Exception as e:
        print(f"Error processing request: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'success': False,
                'message': 'Internal server error'
            })
        }
