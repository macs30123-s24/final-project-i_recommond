import psycopg2
import json
import boto3
import csv
from io import StringIO

s3 = boto3.client('s3')

def lambda_handler(event, context):
    db_host = event['db_host']
    db_name = event['db_name']
    db_user = event['db_user']
    db_password = event['db_password']
    db_port = event['db_port']
    s3_bucket = event['s3_bucket']
    s3_key = event.get('s3_key', 'results/query_results.json')  # Default to 'results/query_results.json' if 's3_key' is not provided
    
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password,
            port=db_port
        )

        # Create a cursor object
        cursor = connection.cursor()
        
        sql_query = """
        SELECT
            b."userId" AS uid,
            u."userName",
            cg."title" AS category,
            scg."title" AS sub_category,
            l."title" AS product,
            l."price" AS listing_amount,
            COUNT(*) AS counts,
            SUM(b."amount") AS total_bid_amount
        FROM
            public.users u
        RIGHT JOIN public.bids b ON u."id" = b."userId"
        JOIN public.listing l ON b."listingId" = l."id"
        JOIN public.category cg ON l."categoryId" = cg."id"
        JOIN public.sub_category scg ON l."subCategoryId" = scg."id"
        GROUP BY
            cg."title",
            scg."title",
            l."title",
            l."price",
            b."userId",
            u."userName"
        ORDER BY
            cg."title",
            scg."title",
            counts DESC;
        """
        
        # Execute the query
        cursor.execute(sql_query)

        # Fetch all rows from the executed query
        rows = cursor.fetchall()
        
        # Get column names from cursor
        column_names = [desc[0] for desc in cursor.description]

        # Create a CSV file in memory
        csv_buffer = StringIO()
        csv_writer = csv.writer(csv_buffer)
        
        # Write the column headers to the CSV file
        csv_writer.writerow(column_names)
        
        # Write the rows to the CSV file
        csv_writer.writerows(rows)

        # Upload the CSV file to S3
        s3.put_object(Bucket=s3_bucket, Key=s3_key, Body=csv_buffer.getvalue())

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return {
            'statusCode': 200,
            'body': f"uploaded to s3://{s3_bucket}/{s3_key}"
        }

    except (Exception, psycopg2.Error) as error:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(error)})
        }
