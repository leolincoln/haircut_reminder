# -*- coding: utf-8 -*-
"""
Created on Thu Aug 06 12:20:59 2015

@author: liuliu
"""
from flask import Flask,render_template,request
from os import environ
import json
import traceback
from send_txt import sms

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    '''
    Returns:
        render home.html.
    Requests:
    e.g.
    [('carrier', u'tmobile'), ('name', u'liu'), ('submitbutton', u'Submit'),
    ('phone#', u'2243100552'), ('reccurence', u'2'), ('location', u'alkej')]
    '''

    #sms(content='hair_cut_reminder: online')
    if len(request.form.keys())!=0:
        #get name
        name = request.form['name']
        try:
            carrier = request.form['carrier']
        except:
            return render_template('home.html')

        phone = request.form['phone#']
        #defaults reccurence to 2
        try:
            reccurence = int(request.form['reccurence'])
        except:
            reccurence = 2

        location = request.form['location']

        #send sms
        #format: sms(phone = '2243100552',content=None,subject=None,carrier='sprint'):
        sms(phone = phone,content="reminder to cut your hair",carrier = carrier)
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
    import sys
    app.run(host='0.0.0.0',debug=True,port=int(environ.get("PORT", 5000)))
