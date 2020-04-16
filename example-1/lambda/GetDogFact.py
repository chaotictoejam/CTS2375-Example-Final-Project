import json
import random

def lambda_handler(event, context):
    factlist = [["Dogs like to play in water!", "images/leela_water.jpg"], 
        ["Dogs don't understand beds are for sleeping.", "images/leela_bed.jpg"],  
        ["Dogs destroy there toys", "images/leela_toys.jpg"],  
        ["Wear sweaters. Seriously? You have fur.", "images/leela_sewaters.jpg"],  
        ["Attack the broom.", "images/leela_broom.gif"],  
        ["Like to play in dirt.", "images/leela_dirt.jpg"]
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
