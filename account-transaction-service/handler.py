import json
import boto3

dynamodb = boto3.resource('dynamodb')
table_name = 'AccountTransaction'
table = dynamodb.Table(table_name)

def save_account_transaction(event, context):
    body = json.loads(event['body'])
    
    if 'id' not in body or 'accountNumber' not in body or 'accountType' not in body or 'openingDate' not in body or 'status' not in body or 'identificationNumber' not in body:
        response = {
            'statusCode': 400,
            'body': json.dumps({'message': 'Campos de AccountTransaction faltantes'})
        }
        return response

    account_transaction = {
        'id': body['id'],
        'accountNumber': body['accountNumber'],
        'accountType': body['accountType'],
        'openingDate': body['openingDate'],
        'status': body['status'],
        'identificationNumber': body['identificationNumber']
    }

    table.put_item(Item=account_transaction)

    response = {
        'statusCode': 200,
        'body': json.dumps({'message': 'AccountTransaction guardado exitosamente'})
    }
    return response
