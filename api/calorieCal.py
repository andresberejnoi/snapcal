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

	def build_url(self, endpoint):
		return self.baseurl + "/" + self.version + "/" + endpoint
	
	def auth_headers(self):
		self.headers['x-app-id'] = self.appId
		self.headers['x-app-key'] = self.appKey
		self.headers['x-remote-user-id'] = "0"

	def get_cal(self, query):
                """ given a query returns an array of food dictionaries
                return: [
                               {
                                                                "food_name":
								"food_cal":
							}
						]
                """
                endpoint = "natural/nutrients"
                url = self.build_url(endpoint)
                self.auth_headers()
                body = {"query": query, "timezone": "US/Eastern"}
                result_query = requests.post(url, data=json.dumps(body), headers=self.headers).text
                print (result_query)
                return result_query


if __name__ == "__main__":
	cfg = load_config()
	CC = CalorieCal(cfg)
	CC.get_cal("1 Veggie Burger")
