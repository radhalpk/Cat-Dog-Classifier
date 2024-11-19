from django.shortcuts import render
from django.core.files.storage import default_storage
from django.conf import settings

import tensorflow as tf
from tensorflow import keras
from PIL import Image
import os
from app1 import forms

def index(request):
    content = " "
    im_url = None
    
    if request.method == "POST":
        Form = forms.UserForm(request.POST, request.FILES)
        if Form.is_valid():
            script_directory = os.path.dirname(os.path.abspath(__file__))  
            model_path = os.path.join(script_directory, 'Cat-vs-DOg.h5')
            model = tf.keras.models.load_model(model_path) ##loading DL model
            
            image = Form.cleaned_data['UloadImage']
            img = Image.open(image)
            img = img.resize((256, 256))
            img_array = keras.preprocessing.image.img_to_array(img)
            img_array = img_array.reshape((1, 256, 256, 3))
            
            pred = model.predict(img_array)
            print("--------------",pred)
            
            if pred <= 0.5:
                content = "CAT"
            else:
                content = "DOG"
                
            Form.save(commit=True)
            con = {'Form': Form, 'content': content}
            return render(request, 'app1/index.html', context=con)
    else:
        Form = forms.UserForm()
        con = {'Form': Form, 'content': content}
        return render(request, 'app1/index.html', context=con)
