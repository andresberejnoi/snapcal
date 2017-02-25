import sys
from tools import *

image_path = sys.argv[1]
label = classify(image_path)
print(label) #for debugging
