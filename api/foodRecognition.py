import tensorflow as tf, sys
from util import load_config

class FoodRecognition:
	
	def __init__(self, cfg):
		self.image_path = None
		self.retrained_labels = cfg["FoodRec"]["labels"]
		self.retrained_graph = cfg["FoodRec"]["graph"]
		self.label_lines = self.read_labels()
	"""
	def set_image_path(self, image_path):
		self.image_path = image_path
        """
	def read_image(self,image_path):
		# Read in the image_data
		image_data = tf.gfile.FastGFile(image_path, 'rb').read()
		return image_data
	
	def read_labels(self):
		# Loads label file, strips off carriage return
		label_lines = [line.rstrip() for line in tf.gfile.GFile(self.retrained_labels)]
		return label_lines
	
	def print_rank(predictions):
		for node_id in predictions:
			human_string = self.label_lines[node_id]
			score = predictions[0][node_id]
			print('%s (score = %.5f)' % (human_string, score))

	def predict(self):
		# Unpersists graph from file
		with tf.gfile.FastGFile(self.retrained_graph, 'rb') as f:
			graph_def = tf.GraphDef()
			graph_def.ParseFromString(f.read())
			_ = tf.import_graph_def(graph_def, name='')
		with tf.Session() as sess:
			# Feed the image_data as input to the graph and get first prediction
			softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

			predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': self.read_image()})
			
			# Sort to show labels of first prediction in order of confidence
			top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
		
		label = self.label_lines[top_k[0]]
		#certainty = predictions[0][top_k[0]]
		
		return label
        def predict_multilabel(self):
                '''Placeholder. It should find several types of objects present in one image'''
                with tf.gfile.FastGFile(self.retrained_graph, 'rb') as f:
                        graph_def = tf.GraphDef()
                        graph_def.ParserFromString(f.read())
                        _ = tf.import_graph_def(graph_def, name = '')
                
                pass
                pass
                labels = None
                return labels 

if __name__ == "__main__":
	cfg = load_config()
	imgRec=FoodRecognition(cfg)
	imgRec.set_image_path("brocolli.jpg")
	print	imgRec.predict()
	
