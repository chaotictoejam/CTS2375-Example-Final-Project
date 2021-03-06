const AWS = require('aws-sdk');
const ddb = new AWS.DynamoDB.DocumentClient({region: 'us-east-1'});

exports.handler = async (event, context, callback) => {
    const requestId = context.awsRequestId;
    await agree(requestId).then(() => {
        callback(null, {
            statusCode: 201,
            body: '',
            headers: {
                'Access-Control-Allow-Origin': '*',
            },
        });
    }).catch((err) => {
        console.error(err);
    });
};

function agree(requestId) {
    const params = {
      TableName: 'Agree',
      Item: {
        'AgreeId': requestId
      }
    }
    return ddb.put(params).promise();
}