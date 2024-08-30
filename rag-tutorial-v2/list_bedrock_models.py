import boto3
import json
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Create a client for Bedrock
try:
    client = boto3.client('bedrock', region_name='us-east-1')  # Use the correct region

    # Attempt to call the service (e.g., list foundation models)
    response = client.list_foundation_models()
    print("Credentials are set correctly. Bedrock response:", json.dumps(response, indent=4))

except NoCredentialsError:
    print("No credentials found. Please configure your AWS credentials.")
except PartialCredentialsError:
    print("Incomplete credentials found. Please check your AWS credentials.")
except Exception as e:
    print("An error occurred:", str(e))
