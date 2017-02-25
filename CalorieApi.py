import requests
import json
from util import load_config

def getCal(query, cfg):
	""" given a query returns an array of food dictionaries
	return: [
						{
							"food_name":
							"food_cal":
						}
					]
	"""
	endpoint = "natural/nutrients"
	url = cfg["nutritionix"]["url"] + "/" + cfg["nutritionix"]["version"] + "/" + endpoint
	headers = {'content-type': "application/json",
					'x-app-id': cfg["nutritionix"]["appId"],
					'x-app-key': cfg["nutritionix"]["appKey"],
					'x-remote-user-id': "0" }
	body = {"query": query, "timezone": "US/Eastern"}

	url = "https://trackapi.nutritionix.com/v2/natural/nutrients"

	print requests.post(url, data=json.dumps(body), headers=headers).text


if __name__ == "__main__":
	cfg = load_config()
	getCal("1 Veggie Burger", cfg)
