import json

def lambda_handler(event, context):

    textEmail = event['queryStringParameters']['textEmail']
    textTitle = event['queryStringParameters']['textTitle']
    textFirst_name = event['queryStringParameters']['textFirst_name']
    textLast_name = event['queryStringParameters']['textLast_name']
    textAddress_line1 = event['queryStringParameters']['textAddress_line1']
    textAddress_line2 = event['queryStringParameters']['textAddress_line2']
    textCity = event['queryStringParameters']['textCity']
    textPostcode = event['queryStringParameters']['textPostcode']
    textTelephone = event['queryStringParameters']['textTelephone']
    textSite = event['queryStringParameters']['textSite']

    app_response = {}
    app_response['message'] = "Welcome " + textFirst_name + textLast_name + " thank you for register in this app"
    app_response['access_log'] = "Your access login is " + textEmail

    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(app_response)


    return responseObject