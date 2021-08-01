from flask import Flask, render_template, request, redirect, url_for  # For flask implementation
from bson import ObjectId  # For ObjectId to work
from pymongo import MongoClient
import os
import logging
import orderInsert

app = Flask(__name__)

@app.route('/')
def getFun():
    name    = request.args.get('a_name')
    address = request.args.get('a_address')
    item    = request.args.get('a_item')
    dt      = request.args.get('a_date')
    orderInsert.orderInsRecord(name,address,item,dt)
    return render_template('index.html')

@app.route('/listorder')
def listFun():
    listval = orderInsert.orderlistRecords()
    return render_template('listOrder.html', arg1= listval)

if __name__ == "__main__":
    app.run(debug=True)