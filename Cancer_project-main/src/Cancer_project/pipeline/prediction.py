import numpy as np
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing import image



import os



class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename


    
    def predict(self):
        # load model
        model = load_model(os.path.join("model","model.h5"))

        imagename = self.filename
        test_image = image.image_utils.load_img(imagename, target_size = (224,224))
        test_image = image.image_utils.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'Adenocarcinoma Cancer'
            return [{"image":prediction}]
        else:
            prediction = 'Normal'
            return [{"image":prediction}]