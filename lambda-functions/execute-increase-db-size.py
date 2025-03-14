import json
import boto3

def lambda_handler(event, context):
    sfn_client = boto3.client('stepfunctions')

    # Execute the Step Function
    try:
        response = sfn_client.start_execution(
            stateMachineArn='arn-your-step-function',
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