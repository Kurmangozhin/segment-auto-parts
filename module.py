import numpy as np
import os, cv2
from config import *
from PIL import Image



def load_img(path:str):
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)	
    img_input = cv2.resize(img,(img_height,img_width))
    img_input = np.expand_dims(img_input, axis=0)
    return img_input, img


def load_models():
    from tensorflow.keras.models import load_model
    model = load_model(model_path, compile = False)
    return model

def processing(pred):
    dt = list()
    pr = pred[0]
    pr = pr.reshape(-1, num_classes)
    for k in range(len(pr)):
        index = np.argmax(pr[k])
        dt.append(colors_cls[index])
    dt = np.array(dt)
    dt = dt.reshape(img_width, img_height,3)
    return dt


def prediction_save(img_path:str, out_path:str):
    img_input, img = load_img(img_path)
    model   = load_models()
    predict = model.predict(img_input)
    result  = processing(predict)
    images  = Image.fromarray(result.astype('uint8')).convert('RGB')
    images = images.resize(size = (img.shape[1], img.shape[0]))
    result_image = cv2.addWeighted(img, 0.75, np.array(images), 0.65, 0)
    cv2.imwrite(out_path, cv2.cvtColor(result_image,cv2.COLOR_BGR2RGB))




    

