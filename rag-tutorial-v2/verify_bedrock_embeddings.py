from langchain_aws import BedrockEmbeddings

def verify_bedrock_embeddings():
    try:
        # Initialize BedrockEmbeddings with the credentials profile and region
        embeddings = BedrockEmbeddings(
            credentials_profile_name="default",
            region_name="us-east-1"
        )

        # Example text to test embedding
        test_text = ["Hello, this is a test to verify BedrockEmbeddings!"]

        # Try to create embeddings
        result = embeddings.embed_documents(test_text)

        # Print the result
        print("Embedding successful! Here is the result:")
        print(result)

    except Exception as e:
        print("An error occurred while verifying BedrockEmbeddings:")
        print(str(e))

        # Additional debugging output
        import os
        print("AWS_PROFILE:", os.environ.get("AWS_PROFILE", "Not set"))
        print("AWS_REGION:", os.environ.get("AWS_REGION", "Not set"))

if __name__ == "__main__":
    verify_bedrock_embeddings()
