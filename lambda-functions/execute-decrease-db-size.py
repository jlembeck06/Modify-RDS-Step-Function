import boto3
import json

def lambda_handler(event, context):
    sfn_client = boto3.client('stepfunctions')

    
    try:
        # Execute the Step Function
        response = sfn_client.start_execution(
            # Inform the Step Function ARN
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