import tensorflow as tf, sys
from util import load_config

class FoodRecognition():
	
        def __init__(self, cfg):
                self.image_path = None
                self.retrained_labels = cfg["FoodRec"]["labels"]
                self.retrained_graph = cfg["FoodRec"]["graph"]
                self.label_lines = self.read_labels()

        def read_image(self,image_path):
                # Read in the image_data
                image_data = tf.gfile.FastGFile(image_path, 'rb').read()
                self.image_data = image_data
        
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
                        
                        predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': self.image_data})
                
                        # Sort to show labels of first prediction in order of confidence
                        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
                print(type(top_k),top_k)   #DEBUGGING LINE       
                label = self.label_lines[top_k[0]]
                #certainty = predictions[0][top_k[0]]
                
                return label
        
        def predict_multilabel(self):
                '''Placeholder. It should find several types of objects present in one image'''
                with tf.gfile.FastGFile(self.retrained_graph, 'rb') as f:
                        graph_def = tf.GraphDef()
                        graph_def.ParseFromString(f.read())
                        _ = tf.import_graph_def(graph_def, name = '')
                with tf.Session() as sess:
                        sigmoid_tensor = sess.graph.get_tensor_by_name('final_result:0')
                        predictions = sess.run(sigmoid_tensor, {'DecodeJpeg/contents:0': self.image_data})

                        #Sort labels
                        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
                print(type(top_k),'is ', top_k)  #REMOVE AFTER DEBUGGING
                labels = [self.label_lines[ID] for ID in top_k]  #a list of sorted labels
                scores = [predictions[0][node_id] for node_id in top_k]

                #tf.nn.sigmoid_cross_entropy_with_logits(logits,targets,name=None)
                #labels = None
                return labels,scores 

if __name__ == "__main__":
        cfg = load_config()
        imgRec=FoodRecognition(cfg)
        #imgRec.set_image_path("brocolli.jpg")
        #imgRec.read_image('brocolli.jpg')
        img_path = sys.argv[1]
        imgRec.read_image(img_path)
        #print(imgRec.predict())
        labels,scores = imgRec.predict_multilabel()
        added_scores = sum(scores)
        print("Total sum of scores is:",added_scores)
        print(list(zip(labels,scores)))
