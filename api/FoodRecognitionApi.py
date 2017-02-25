import tensorflow as tf, sys

class FoodRecognition:
	
	def __init__(self):
		self.image_path = None
		self.label_lines = self.read_labels()
	
	def set_image_path(self, image_path):
		self.image_path = image_path

	def read_image(self):
		# Read in the image_data
		image_data = tf.gfile.FastGFile(self.image_path, 'rb').read()
		return image_data
	
	def read_labels(self):
		# Loads label file, strips off carriage return
		label_lines = [line.rstrip() for line in tf.gfile.GFile("retrained_labels.txt")]
		return label_lines
	
	def print_rank(prediction):
		for node_id in prediction:
			human_string = self.label_lines[node_id]
			score = predictions[0][node_id]
			print('%s (score = %.5f)' % (human_string, score))

	def predict(self):
		# Unpersists graph from file
		with tf.gfile.FastGFile("retrained_graph.pb", 'rb') as f:
			graph_def = tf.GraphDef()
			graph_def.ParseFromString(f.read())
			_ = tf.import_graph_def(graph_def, name='')
		with tf.Session() as sess:
			# Feed the image_data as input to the graph and get first prediction
			softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

			predictions = sess.run(softmax_tensor, \
      	{'DecodeJpeg/contents:0': self.read_image()})
			
			# Sort to show labels of first prediction in order of confidence
			top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
		
		label = self.label_lines[top_k[0]]
		#certainty = predictions[0][top_k[0]]
		
		return label
    

if __name__ == "__main__":
	imgRec=FoodRecognition()
	imgRec.set_image_path("brocolli.jpg")
	print	imgRec.predict()
	
