import boto3
import json

def lambda_handler(event, context):
    snf_client = boto3.client('stepfunctions')

    try:
        # Execute the Step Function
        response = snf_client.start_execution(
            stateMachineArn='arn:aws:states:sa-east-1:620200558027:stateMachine:Decrease-Database-Size',
        )

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Step Function execution started successfully',
                'executionArn': response['executionArn']
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Failed to start Step Function execution',
                'error': str(e)
            })
        }