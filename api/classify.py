from foodRecognition import FoodRecognition
from util import load_config
from calorieCal import CalorieCal
import sys

def run():
    cfg = load_config()
    image_path = sys.argv[1]
    foodRec = FoodRecognition(cfg)
    image_data = foodRec.read_image(image_path)
    image_labels = foodRec.read_labels()

    #Predict the items in the picture:
    label = foodRec.predict()

    cal_query = CalorieCal(cfg) 


    #get calorie information
    cal = cal_query.get_cal(label)
