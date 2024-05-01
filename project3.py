from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import json

driver = webdriver.Chrome()
URL = "https://bringatrailer.com/porsche/991-gt2/?exclude=parts+wheels"

resp = driver.get(URL)

sleep(3)

auctionLinks = []
auctionDataComplete = {}

auction = driver.find_elements(By.XPATH, '//a[@class="listing-card bg-white-transparent"]')

print(f"Scraping complete, {len(auction)} GT2 RS's processed")

for link in auction:
	href = link.get_attribute("href")
	auctionLinks.append(href)

for auction in auctionLinks:
	auctionData = {}
	driver.get(auction)

	sleep(2)

	VIN_elements = driver.find_elements(By.XPATH, '//a[contains(@href, "search?q=")]')
	for vin in VIN_elements:
		VINtext = vin.text.strip()
		VIN = VINtext
		

	modelName = driver.find_elements(By.XPATH, '//h1[@class="post-title listing-post-title"]')
	for title in modelName:
		textTitle = title.text

		auctionData['modelName'] = textTitle

	auctionDetails = driver.find_elements(By.XPATH, '//span[@class="info-value noborder-tiny"]')
	for elem in auctionDetails:
		elemText	= elem.text.split()
		price		= elemText[2].strip('$').replace(',', '')
		date		= elemText[4]
		result		= elemText[0]

		auctionData['price']	= price
		auctionData['date']		= date
		auctionData['result']	= result

	auctionTag = driver.find_elements(By.XPATH, '//div[@class = "item-tags"]')
	auctionData['tags'] = ["No Tags"]  
	if auctionTag:
		auctionData['tags'] = []  
		for tag in auctionTag:
			textTag = tag.text.strip()
			if textTag:
				auctionData['tags'].append(textTag)  

	sellerName = driver.find_elements(By.XPATH, '//div[@class="item item-seller"]')
	for name in sellerName:
		cleanedName = name.text.split()
		auctionData['seller name'] = cleanedName[1]
		

	sellerLoc = driver.find_elements(By.XPATH, '//a[contains(@href, "maps/place")]')
	for location in sellerLoc:
		loc = location.text.strip()
		auctionData['location'] = loc
		

	listingDetails = driver.find_elements(By.XPATH, '//div[@class = "item"]//ul//li')
	details = []
	for detail in listingDetails:
		detailInfo = detail.text
		details.append(detailInfo)

		auctionData['listing details'] = details


	auctionDataComplete[VIN] = auctionData

results = {"911 GT2 RS's": auctionDataComplete}

with open("products.json", "w+") as f:
	json.dump(results, f, indent = 4)
f.close()

