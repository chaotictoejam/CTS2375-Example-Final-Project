import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Orgin" : "*"
        },
        'body': {
            'fact':'This is a random dog fact',
            'image':'images/leela.jpg'
        }
    }
