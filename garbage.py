from flask import Flask
import bcolz
from fastai.imports import *
from fastai.transforms import *
from fastai.conv_learner import *
from fastai.model import *
from fastai.dataset import *
from fastai.sgdr import *
from fastai.plots import *
from flask import request
import os
app = Flask(__name__)
 
@app.route("/", methods = ['GET', 'POST'])
def hello():
    latestfile = request.files['media']
    latestfile.save(os.path.join(app.root_path, 'img/cam/1.jpg'))
    PATH = "./img/"
    sz=224
    tfms = tfms_from_model(resnet50, sz, aug_tfms=transforms_side_on, max_zoom=1.1)
    arch = resnet50
    data = ImageClassifierData.from_paths(PATH, tfms=tfms_from_model(arch, sz), test_name = 'cam')
    learn = ConvLearner.pretrained(arch, data, precompute=True)
    
    learn.load('garbage')
    im_path = 'img/cam/1.jpg'
    trn_tfms, val_tfms = tfms_from_model(arch,sz) # get transformations
    learn.precompute=False # We'll pass in a raw image, not activationstrn_tfms, val_tfms   tfms_from_model(resnet34,sz)
    
    im = val_tfms(open_image(im_path))
    log_preds,y = learn.TTA(is_test=True)
    probs = np.mean(np.exp(log_preds), axis=0)
    f=data.test_ds.fnames
    if f[0]=='cam/1.jpg':
        r=probs[0]
    else:
        r=probs[1]
    return str(np.argmax(r))

@app.route('/d')
def hello1():
	return "dewde" 

if __name__ == "__main__":
    app.run()
