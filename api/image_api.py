import requests
import schedule
import time
from supabase import Client, create_client

image_urls = ["https://kamere.dars.si/kamere/Sentvid_Jug/cam6.jpg",
              "https://kamere.dars.si/kamere/Sentvid_Jug/cam6.jpg",
              "https://kamere.dars.si/kamere/Golovec/Portal_Nove_Jarse1.jpg",
              "https://kamere.dars.si/kamere/Golovec/Strmec_Bizovik.jpg",
              "https://kamere.dars.si/kamere/Golovec/K24_Rudnik_SD_1.jpg",
              "https://kamere.dars.si/kamere/ljubljana/Kam20_pociva_Barje.jpg",
              "https://kamere.dars.si/kamere/Sentvid_Jug/cam11.jpg",
              "https://www.drsc.si/kamere/KamSlike/BrezovicaAC2/slike/Bac2_0001.jpg",
              "https://www.drsc.si/kamere/KamSlike/Dragomer/slike/Dra1_0001.jpg",
              "https://kamere.dars.si/kamere/msc2pics/Cam21_SPEED_VHOD.jpg",
              "https://kamere.dars.si/kamere/Vrhnika/Sinja_gorica_LJ.JPG",
              "https://kamere.dars.si/kamere/Vrhnika/CP_Vrhnika_Panorama_izhod.JPG"]

image_url = "https://kamere.dars.si/kamere/Golovec/Portal_Nove_Jarse2.jpg"

# Replace with your Supabase URL and key
url = "https://hqzppnbdbfpalptrrzas.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhxenBwbmJkYmZwYWxwdHJyemFz" \
      "Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDI2NzI4NTcsImV4cCI6MjAxODI0ODg1N30.mx5rnff6qF9P6qMF7CejkL4IxijBH3dJfojrZYi2S7w"
client: Client = create_client(url, key)


def fetch_and_save_image():
    # Fetch the image from the URL
    response = requests.get(image_url, stream=True)

    # Check if the request was successful
    if response.status_code == 200:
        # Get the image data
        image_data = response.content

        # Save the image locally in the folder images in the format image.jpg
        filepath = "../images/image.jpg"
        with open(filepath, 'wb') as f:
            f.write(image_data)

        with open(filepath, 'rb') as f:
            # delete image from storage
            client.storage.from_("kamere").remove("image.jpg")
            client.storage.from_("kamere").upload(file=f, path="image.jpg", file_options={"content-type": "image/jpeg"})


# Schedule the image fetching and uploading task to run every minute
# schedule.every(1).minutes.do(lambda: fetch_and_save_image())

# while True:
# schedule.run_pending()
# time.sleep(1)

fetch_and_save_image()
