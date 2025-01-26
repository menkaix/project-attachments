from google.cloud import storage

# ...existing code...

def upload_file_to_gcs(bucket_name, file_stream, destination_blob_name):
    """Uploads a file stream to Google Cloud Storage."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_file(file_stream)

    print(f"File uploaded to {destination_blob_name}.")

# ...existing code...
