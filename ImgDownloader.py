import requests
import json
import os

imageToDownload = input("search what image to download: ")
numberOfImage = input("select the number of image between 3-200 to download: ")

imagesLink = []

while int(numberOfImage) < 3 or int(numberOfImage) > 200:
    print("the number must be more than 3 and less than 200")
    numberOfImage = input("select the number of image between 3-200 to download: ")

response = requests.get(f"https://pixabay.com/api/?key=9602505-f76ea265b3e81cda17324512f&per_page={numberOfImage}&q={imageToDownload}")

#Create the folder if it does not exist
if not os.path.exists(f"{imageToDownload}"):
    os.makedirs(f"{imageToDownload}")

# filter the json to url of image and assign it to an array
for imageURL in json.loads(response.content)["hits"]:
    imagesLink.append(imageURL["largeImageURL"])

for count, imageLink in enumerate(imagesLink):
    img_data = requests.get(f"{imageLink}")
    f = open(f"{imageToDownload}/img{count}.jpg", "wb+")
    f.write(img_data.content)
