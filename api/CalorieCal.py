import requests
import json
from util import load_config

class CalorieCal:
	def __init__(self, cfg):
		self.appId = cfg["nutritionix"]["appId"]
		self.appKey = cfg["nutritionix"]["appKey"]
		self.baseurl = cfg["nutritionix"]["url"] 
		self.version = cfg["nutritionix"]["version"]
		self.headers = {'content-type': "application/json"}

	def buildUrl(self, endpoint):
		return self.baseurl + "/" + self.version + "/" + endpoint
	
	def authHeaders(self):
		self.headers['x-app-id'] = self.appId
		self.headers['x-app-key'] = self.appKey
		self.headers['x-remote-user-id'] = "0"

	def getCal(self, query):
		""" given a query returns an array of food dictionaries
		return: [
							{
								"food_name":
								"food_cal":
							}
						]
		"""
		endpoint = "natural/nutrients"
		url = self.buildUrl(endpoint)
		self.authHeaders()
		body = {"query": query, "timezone": "US/Eastern"}
		print requests.post(url, data=json.dumps(body), headers=self.headers).text


if __name__ == "__main__":
	cfg = load_config()
	CC = CalorieCal(cfg)
	CC.getCal("1 Veggie Burger")
