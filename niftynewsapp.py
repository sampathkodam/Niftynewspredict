# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 22:23:21 2020

@author: SAMPATH
"""


from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np

app = Flask(__name__,template_folder='template')
model = pickle.load(open('final_scores.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/Niftypredict", methods=['GET'])
def Niftypredict():
    if request.method == 'GET':
        sentence=request.args.get('sentence')
        data=model(str(sentence))
        return render_template('index.html',positive_value=data['pos'],neutral_value=data['neu'],negative_value=data['neg'],compound_value=data['compound'])

    else:
        return render_template('index.html')

  
    
if __name__=="__main__":
    app.run()