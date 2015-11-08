# -*- coding: utf-8 -*-
"""
Created on Thu Aug 06 12:20:59 2015

@author: liuliu
"""
from flask import Flask,render_template

import json
import traceback

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    '''
    Returns: 
        render home.html. 
    '''
    sms(content='hair_cut_reminder: online')
    return render_template('home.html')

@app.route('/houseclean')
def confidence():
    '''
    returns:
        render houseclean.html
    '''
    return render_template('houseclean.html')


@app.route('/anniversary')
def cleaner():
    return render_template('anniversary.html')

if __name__=='__main__':
    from send_txt import sms
    app.run(debug=True)
