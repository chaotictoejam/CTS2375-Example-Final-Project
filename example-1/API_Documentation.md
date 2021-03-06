# Cats Website API Documentation

The Cats Website API is a simple API organized around REST. 

## Core Resources

### Agree

This is an object represents how many people have agreed to cats being awesome. There are two methods.

#### GET
This retrieves the total count of how many people have agreed to cats being awesome. This calls AWS Gateway API which then calls the lambda function ReadAgreeCats. The lambda function then accesses the DynamoDb Agree table, and returns the count.

**Sample Call**

This is a simple GET call, and requires no body.

**Sample Response**

```json
{
    "statusCode":200,
    "body":21,
    "headers":{
    	"Access-Control-Allow-Origin":"*"
    }
}
```

#### POST

This post an agreement to count towards how many people have agreed to cats being awesome. This calls AWS Gateway API which then calls the lambda function AgreeCats. The lambda function then accesses the DynamoDb Agree table, and writes the new agreement to the table.

**Sample Call**

This POST call requires no body.

**Sample Response**

```json
{
    "statusCode":201,
    "body":"",
    "headers":{
    	"Access-Control-Allow-Origin":"*"
    }
}
```

### Cat Facts

#### GET

This retrieves the a random fact about cats and an image. This calls AWS Gateway API which then calls the lambda function GetCatFact. The lambda function choses a random fact from a list of facts.

**Sample Call**

This is a simple GET call, and requires no body.

**Sample Response**

```json
{
    "statusCode": 200, 
    "headers": {
        "Access-Control-Allow-Orgin": "*"
    }, 
    "body": {
        "fact": "Cats can make themselves compact.", 
        "image": "images/chell_ball.jpg"
    }
}
```

### Dog Facts

#### GET

This retrieves a random fact about dogs and an image. This calls AWS Gateway API which then calls the lambda function GetDogFact. The lambda function choses a random fact from a list of facts.

**Sample Call**

This is a simple GET call, and requires no body.

**Sample Response**

```json
{
    "statusCode": 200, 
    "headers": {
        "Access-Control-Allow-Orgin": "*"
    }, 
    "body": {
        "fact": "Dogs destroy there toys", 
        "image": "images/leela_toys.jpg"
    }
}
```
