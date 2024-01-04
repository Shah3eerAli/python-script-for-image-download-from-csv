import csv
import os
import requests

def download_image(image_url):
    file_name = image_url.split("/")[-1]
    try:
        # Check if the file already exists in the 'downloaded' directory
        if os.path.exists(f"downloaded/{file_name}"):
            print(f"Skipping {file_name}. Image already downloaded.")
            return  # Skip downloading if the file exists

        # Send a GET request to the image URL
        response = requests.get(image_url, stream=True)
        
        if response.status_code == 200:
            # Create a directory if it doesn't exist
            if not os.path.exists('downloaded'):
                os.makedirs('downloaded')

            # Save the image to a local file
            with open(f"downloaded/{file_name}", 'wb') as img_file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        img_file.write(chunk)
            
            print("Image downloaded successfully!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def process_csv(file_path):                    
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                download_image(row['url'])
            except Exception as e:
                print(f"Error processing row: {str(e)}")

# Replace 'files.csv' with your CSV file name or path
file_path = 'files.csv'
process_csv(file_path)
