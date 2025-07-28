import requests
import io
from PIL import Image
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scroll_to_bottom(wd, delay=2, max_attempts=30):
    """Scroll to the bottom repeatedly to load more content, up to max_attempts."""
    print("Scrolling to the bottom of the page...")
    last_height = wd.execute_script("return document.body.scrollHeight")
    last_image_count = 0
    attempts = 0

    while attempts < max_attempts:
        # Scroll down
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay)

        # Check scroll height and number of image containers
        new_height = wd.execute_script("return document.body.scrollHeight")
        image_elements = wd.find_elements(By.CSS_SELECTOR, 'div.CoverImage')

        if new_height == last_height and len(image_elements) == last_image_count:
            print("No new content loaded. Ending scroll.")
            break

        last_height = new_height
        last_image_count = len(image_elements)
        attempts += 1

    print(f"Scrolling finished after {attempts} attempts.")


def get_images_from_site(wd, url, dir, species, max_images=5, delay=2):
    wd.get(url)
    
    # Wait for the page to load and for the image containers to appear
    try:
        # Wait for the first image container to appear
        WebDriverWait(wd, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.CoverImage'))
        )
        print("First image is visible.")
    except Exception as e:
        print(f"Error waiting for the first image: {e}")
        return

    # Scroll to the bottom of the page to load all images
    scroll_to_bottom(wd, delay)

    images_downloaded = 0
    while images_downloaded < max_images:
        try:
            # Find all image divs with the class 'CoverImage'
            photo_containers = wd.find_elements(By.CSS_SELECTOR, 'div.CoverImage')
            print(f"Found {len(photo_containers)} photo containers.")
            if len(photo_containers) == 0:
                print("No images found.")
                break

            # Loop through the photo containers and download images
            for i, container in enumerate(photo_containers):
                if images_downloaded >= max_images:
                    break

                # Extract the image URL from the background-image style
                image_url = container.value_of_css_property('background-image').replace('url("', '').replace('")', '')
                print(f"Image URL: {image_url}")

                # Download and save the image
                download_image(dir, image_url, f"{species}_{images_downloaded + 1}.jpg")
                images_downloaded += 1
                print(f"Downloaded image {images_downloaded}/{max_images}")

        except Exception as e:
            print(f"Error: {e}")
            break

    print("Finished downloading images.")

def download_image(download_path, url, file_name):
    try:
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        
        # Convert the image to "RGB" mode if it's in "RGBA" mode
        if image.mode == "RGBA":
            image = image.convert("RGB")

        file_path = download_path + file_name

        with open(file_path, "wb") as f:
            image.save(f, "JPEG")

        print("Success")
    except Exception as e:
        print('FAILED -', e)