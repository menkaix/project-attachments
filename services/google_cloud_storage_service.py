from google.cloud import storage
import re

def upload_file_to_gcs(bucket_name, file_stream, destination_blob_name):
    """Uploads a file stream to Google Cloud Storage."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_file(file_stream)

    print(f"File uploaded to {destination_blob_name}.")

def list_blobs_with_prefix(bucket_name, prefix, regex_pattern):
    """Lists all the blobs in the bucket that match the regex pattern."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=prefix)

    pattern = re.compile(regex_pattern)
    matching_blobs = [blob.name for blob in blobs if pattern.match(blob.name)]

    return matching_blobs


