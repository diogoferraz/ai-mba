from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
import time
import json
import os

def main():
    from dotenv import load_dotenv
    global training_client
    global custom_vision_project

    try:
        # Get Configuration Settings
        load_dotenv()
        training_endpoint = os.getenv('VISION_TRAINING_ENDPOINT')
        training_key = os.getenv('VISION_TRAINING_KEY')
        project_id = os.getenv('VISION_PROJECT_ID')

        # Authenticate a client for the training API
        credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
        training_client = CustomVisionTrainingClient(training_endpoint, credentials)


        # Get the Custom Vision project
        custom_vision_project = training_client.get_project(project_id)

        # Upload and tag images
        Upload_Images()

        Train_Model()

    except Exception as ex:
        print(ex)


def Train_Model():
    project_id = os.getenv('VISION_PROJECT_ID')
    prediction_resource_id = os.getenv('VISION_PREDICTION_RESOURCE_ID')
    # create new custom vision project
    publish_iteration_name = "objectDetectionModel"

    # training the project
    print ("Training...")
    iteration = training_client.train_project(project_id)
    while (iteration.status != "Completed"):
        iteration = training_client.get_iteration(project_id, iteration.id)
        print ("Training status: " + iteration.status)
        print ("Waiting 10 seconds...")
        time.sleep(10)

    # the iteration is now trained. Publish it to the project endpoint
    training_client.publish_iteration(project_id, iteration.id, publish_iteration_name, prediction_resource_id)
    print ("Done!")

def Upload_Images():
    print("Uploading images...")

    # Get the tags defined in the project
    tags = training_client.get_tags(custom_vision_project.id)

    # Create a list of images with tagged regions
    tagged_images_with_regions = []

    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the JSON file
    json_file_path = os.path.join(current_dir, 'tagged-images.json')

    # Construct the full path to the JSON file
    images_folder_path = os.path.join(current_dir, 'images')

    # Get the images and tagged regions from the JSON file
    with open(json_file_path, 'r') as json_file:
        tagged_images = json.load(json_file)
        for image in tagged_images['files']:
            # Get the filename
            file = image['filename']
            # Get the tagged regions
            regions = []
            for tag in image['tags']:
                tag_name = tag['tag']
                # Look up the tag ID for this tag name
                tag_id = next(t for t in tags if t.name == tag_name).id
                # Add a region for this tag using the coordinates and dimensions in the JSON
                regions.append(Region(tag_id=tag_id, left=tag['left'],top=tag['top'],width=tag['width'],height=tag['height']))
            # Add the image and its regions to the list
            with open(os.path.join(images_folder_path,file), mode="rb") as image_data:
                tagged_images_with_regions.append(ImageFileCreateEntry(name=file, contents=image_data.read(), regions=regions))

    # Upload the list of images as a batch
    upload_result = training_client.create_images_from_files(custom_vision_project.id, ImageFileCreateBatch(images=tagged_images_with_regions))
    # Check for failure
    if not upload_result.is_batch_successful:
        print("Image batch upload failed.")
        for image in upload_result.images:
            print("Image status: ", image.status)
    else:
        print("Images uploaded.")

if __name__ == "__main__":
    main()