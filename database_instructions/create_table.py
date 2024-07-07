import boto3

def create_score_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb',region_name='eu-west-2')

    table = dynamodb.create_table(
        TableName='Scores',
        KeySchema=[
            {
                'AttributeName': 'song',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'user',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'song',
                'AttributeType': 'S'  # String attribute type
            },
            {
                'AttributeName': 'user',
                'AttributeType': 'S'  # String attribute type
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table


if __name__ == '__main__':
    score_table = create_score_table()
    print("Table status:", score_table.table_status)