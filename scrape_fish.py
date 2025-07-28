from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import scraping
import os

# Create a Service object with ChromeDriverManager
service = Service(ChromeDriverManager().install())
wd = webdriver.Chrome(service=service)

# Banded directory path
banded_dir = '/Users/averyfield/Desktop/Sunfish_ID/data/banded/'

# Make sure the directory exists before downloading
if not os.path.exists(banded_dir):
    os.makedirs(banded_dir)

banded_url = "https://www.inaturalist.org/taxa/99993-Enneacanthus-obesus/browse_photos"
species = 'banded'
scraping.get_images_from_site(wd, banded_url, banded_dir, "banded", max_images=250)

# Black Crappie directory path
blackcrappie_dir = '/Users/averyfield/Desktop/Sunfish_ID/data/blackcrappie/'

# Make sure the directory exists before downloading
if not os.path.exists(blackcrappie_dir):
    os.makedirs(blackcrappie_dir)

blackcrappie_url = "https://www.inaturalist.org/taxa/49594-Pomoxis-nigromaculatus/browse_photos"
species = 'blackcrappie'
scraping.get_images_from_site(wd, blackcrappie_url, blackcrappie_dir, "blackcrappie", max_images=250)

# Blackbanded directory path
blackbanded_dir = '/Users/averyfield/Desktop/Sunfish_ID/data/blackbanded/'

# Make sure the directory exists before downloading
if not os.path.exists(blackbanded_dir):
    os.makedirs(blackbanded_dir)

blackbanded_url = "https://www.inaturalist.org/taxa/99991-Enneacanthus-chaetodon/browse_photos"
species = 'blackbanded'
scraping.get_images_from_site(wd, blackbanded_url, blackbanded_dir, "blackbanded", max_images=250)

# Bluegill directory path
bluegill_dir = '/Users/averyfield/Desktop/Sunfish_ID/data/bluegill/'

# Make sure the directory exists before downloading
if not os.path.exists(bluegill_dir):
    os.makedirs(bluegill_dir)

bluegill_url = "https://www.inaturalist.org/taxa/49591-Lepomis-macrochirus/browse_photos"
species = 'bluegill'
scraping.get_images_from_site(wd, bluegill_url, bluegill_dir, "bluegill", max_images=250)

# Bluespotted directory path
bluespotted_dir = '/Users/averyfield/Desktop/Sunfish_ID/data/bluespotted/'

# Make sure the directory exists before downloading
if not os.path.exists(bluespotted_dir):
    os.makedirs(bluespotted_dir)

bluespotted_url = "https://www.inaturalist.org/taxa/99992-Enneacanthus-gloriosus/browse_photos"
species = 'bluespotted'
scraping.get_images_from_site(wd, bluespotted_url, bluespotted_dir, "bluespotted", max_images=250)

# Green directory path
green_dir = '/Users/averyfield/Desktop/Sunfish_ID/data/green/'

# Make sure the directory exists before downloading
if not os.path.exists(green_dir):
    os.makedirs(green_dir)

green_url = "https://www.inaturalist.org/taxa/58636-Lepomis-cyanellus/browse_photos"
species = 'green'
scraping.get_images_from_site(wd, green_url, green_dir, "green", max_images=250)

# Largemouth Bass directory path
largemouth_dir = '/Users/averyfield/Desktop/Sunfish_ID/data/largemouth/'

# Make sure the directory exists before downloading
if not os.path.exists(largemouth_dir):
    os.makedirs(largemouth_dir)

largemouth_url = "https://www.inaturalist.org/taxa/1439808-Micropterus-nigricans/browse_photos"
species = 'largemouth'
scraping.get_images_from_site(wd, largemouth_url, largemouth_dir, "largemouth", max_images=250)

# Mud directory path
mud_dir = '/Users/averyfield/Desktop/Sunfish_ID/data/mud/'

# Make sure the directory exists before downloading
if not os.path.exists(mud_dir):
    os.makedirs(mud_dir)

mud_url = "https://www.inaturalist.org/taxa/93011-Acantharchus-pomotis/browse_photos"
species = 'mud'
scraping.get_images_from_site(wd, mud_url, mud_dir, "mud", max_images=250)

# Pumpkinseed directory path
pumpkinseed_dir = '/Users/averyfield/Desktop/Sunfish_ID/data/pumpkinseed/'

# Make sure the directory exists before downloading
if not os.path.exists(pumpkinseed_dir):
    os.makedirs(pumpkinseed_dir)

pumpkinseed_url = "https://www.inaturalist.org/taxa/49614-Lepomis-gibbosus/browse_photos"
species = 'pumpkinseed'
scraping.get_images_from_site(wd, pumpkinseed_url, pumpkinseed_dir, "pumpkinseed", max_images=250)

# Redbreast directory path
redbreast_dir = '/Users/averyfield/Desktop/Sunfish_ID/data/redbreast/'

# Make sure the directory exists before downloading
if not os.path.exists(redbreast_dir):
    os.makedirs(redbreast_dir)

redbreast_url = "https://www.inaturalist.org/taxa/85365-Lepomis-auritus/browse_photos"
species = 'redbreast'
scraping.get_images_from_site(wd, redbreast_url, redbreast_dir, "redbreast", max_images=250)

# Rock Bass directory path
rockbass_dir = '/Users/averyfield/Desktop/Sunfish_ID/data/rockbass/'

# Make sure the directory exists before downloading
if not os.path.exists(rockbass_dir):
    os.makedirs(rockbass_dir)

rockbass_url = "https://www.inaturalist.org/taxa/58637-Ambloplites-rupestris/browse_photos"
species = 'rockbass'
scraping.get_images_from_site(wd, rockbass_url, rockbass_dir, "rockbass", max_images=250)

# Smallmouth Bass directory path
smallmouth_dir = '/Users/averyfield/Desktop/Sunfish_ID/data/smallmouth/'

# Make sure the directory exists before downloading
if not os.path.exists(smallmouth_dir):
    os.makedirs(smallmouth_dir)

smallmouth_url = "https://www.inaturalist.org/taxa/49590-Micropterus-dolomieu/browse_photos"
species = 'smallmouth'
scraping.get_images_from_site(wd, smallmouth_url, smallmouth_dir, "smallmouth", max_images=250)

# Warmouth directory path
warmouth_dir = '/Users/averyfield/Desktop/Sunfish_ID/data/warmouth/'

# Make sure the directory exists before downloading
if not os.path.exists(warmouth_dir):
    os.makedirs(warmouth_dir)

warmouth_url = "https://www.inaturalist.org/taxa/104252-Lepomis-gulosus/browse_photos"
species = 'warmouth'
scraping.get_images_from_site(wd, warmouth_url, warmouth_dir, "warmouth", max_images=250)

# White Crappie directory path
whitecrappie_dir = '/Users/averyfield/Desktop/Sunfish_ID/data/whitecrappie/'

# Make sure the directory exists before downloading
if not os.path.exists(whitecrappie_dir):
    os.makedirs(whitecrappie_dir)

whitecrappie_url = "https://www.inaturalist.org/taxa/49593-Pomoxis-annularis/browse_photos"
species = 'whitecrappie'
scraping.get_images_from_site(wd, whitecrappie_url, whitecrappie_dir, "whitecrappie", max_images=250)

