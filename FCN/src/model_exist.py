# -*- coding: utf-8 -*-

import os
import urllib
import logging
import sys

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
    level=logging.INFO,
    stream=sys.stdout)

model_path = os.path.join(os.getcwd(),'model/vgg16.npy')

if not os.path.isfile(model_path):
    logging.info("Model file doesn't exist.")
    url = 'ftp://mi.eng.cam.ac.uk/pub/mttt2/models/vgg16.npy'

    # if dir 'model/' doesn't exist
    model_dir = model_path[:-9]
    if not os.path.exists(model_dir):
        logging.info("Mkdir 'model/'.")
        os.mkdir(model_dir)

    def down(_save_path, _url):
        try:
            urllib.urlretrieve(_url, _save_path)
        except:
            print '\nError when retrieving the URL:', _save_path

    logging.info("Downloading model file.")
    down(model_path, url)
else:
    logging.info("Model file exists.")
