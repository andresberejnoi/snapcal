import yaml

def load_config():
	with open("../config.yml", 'r') as ymlfile:
		cfg = yaml.load(ymlfile)
	return cfg


if __name__ == "__main__":
	print load_config()
