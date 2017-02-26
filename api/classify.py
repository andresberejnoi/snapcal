from foodRecognition import FoodRecognition
from util import load_config
from calorieCal import CalorieCal
import sys

def run(image_path, cfg):
    foodRec = FoodRecognition(cfg)
    foodRec.read_image(image_path)  #reads the image as stores it as an internal parameter
    #image_labels = foodRec.read_labels()
    #Predict the items in the picture:
    labels,_ = foodRec.predict_multilabel()
    cal_query = CalorieCal(cfg) 


    #get calorie information
    calories = [cal_query.get_cal(item) for item in labels]
    tot_cal = sum(calories)

    cal_dict = {label:str(cal) for label,cal in zip(labels,calories)}
    cal_dict['total'] = str(tot_cal)    #adding the total calories as another key:value pair

    return cal_dict
    
if __name__ == "__main__":
    run()
