import json
import random

def lambda_handler(event, context):
    factlist = [["Use sustainable energy to stay warm.", "images/algebra_sunbeam.jpg"], 
        ["Cats are resourceful, we can make anything a bed", "images/algebra_backpack.jpg"],  
        ["Cats can make themselves compact.", "images/chell_ball.jpg"],  
        ["Can climb up high", "images/brr_high.jpg"],  
        ["Cats know how to use a bed.", "images/algebra_bed.jpg"],  
        ["Cats are perfect.", "images/chell2.jpg"]
    ]
    
    randomFact = random.choice(factlist);
    
    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Orgin" : "*"
        },
        'body': {
            'fact':randomFact[0],
            'image':randomFact[1]
        }
    }
