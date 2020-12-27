import os
from flask import Flask, redirect, url_for, request, render_template, session, jsonify
from pymongo import MongoClient
import acp_times
import logging
import arrow
import config

app = Flask(__name__)

client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
#client = MongoClient('172.18.0.2', 27017)
db = client.tododb
db.tododb.delete_many({})

#
###
# Globals
###
#app = flask.Flask(__name__)
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY

###
# Pages
###


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return render_template('calc.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    session['linkback'] = url_for("index")
    return render_template('404.html'), 404


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    #app.logger.debug("Got a JSON request")
    km = request.args.get('km', 999, type=float)
    #app.logger.debug("km={}".format(km))
    #app.logger.debug("request.args: {}".format(request.args))
    # FIXME: These probably aren't the right open and close times
    # and brevets may be longer than 200km
    brevet_dist_km = request.args.get('brevet_dist_km', 0, type = int)

    begin_time = request.args.get('begin_time', "", type = str)
    begin_date = request.args.get('begin_date', "", type = str)

    start_time = arrow.get(begin_date + " " + begin_time).isoformat()
    open_time = acp_times.open_time(km, brevet_dist_km, start_time)
    close_time = acp_times.close_time(km, brevet_dist_km, start_time)

    result = {"open": open_time, "close": close_time}
    return jsonify(result=result)


#############

@app.route('/display', methods=[ 'POST'])
def display():
    _items = db.tododb.find()
    items = [item for item in _items]
    #if not items:
    if(len(items) == 0):
        return render_template('error_none.html')

    return render_template('display.html', items=items)

@app.route('/new', methods=['POST'])
def new():
    #item_doc = {
    #    'name': request.form['name'],
    #    'description': request.form['description']
    #}
    #db.tododb.insert_one(item_doc)
    open_data = request.form.getlist("open")
    close_data = request.form.getlist("close")
    km_data = request.form.getlist("km")
    open_time = []
    close_time = []
    km = []

    #app.logger.debug("km={}".format(km_data))
    #app.logger.debug("open={}".format(open_data))
    #app.logger.debug("close={}".format(close_data))
    
    for data in km_data:
        if str(data):
            #app.logger.debug("data={}".format(data))
            km.append(str(data))
        else:
            break
    for data in open_data:
        if str(data):
            #app.logger.debug("open")
            open_time.append(str(data))
        else:
            break
    for data in close_data:
        if str(data):
            #app.logger.debug("close")
            close_time.append(str(data))
        else:
            break

    #app.logger.debug("km={}".format(km))
    #app.logger.debug("open={}".format(open_time))
    #app.logger.debug("close={}".format(close_time))

    if (len(open_time) == 0) or (len(close_time) == 0) or (len(km) == 0):
        return render_template('error_none.html')

    for idx in range(len(open_time)):
        data = {
            'open_data': open_time[idx],
            'close_data': close_time[idx],
            'km_data': km[idx],
        }
        db.tododb.insert_one(data)

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
