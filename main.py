#!/usr/bin/env python3

import json
import sys
from pprint import pprint as pp
from os import getenv
from time import time

from bottle import Bottle, abort, request, route, run

app = Bottle()


@app.route('/', method='GET')
def index():
    return "ok"


@app.route('/delayedHealthy', method='GET')
def delayedHealthy():
    global boottime
    print("boottime: {}".format(boottime))
    timeTilHealthy = getenv("DELAY_SECONDS")
    if timeTilHealthy is None:
        timeTilHealthy = 10
    else:
        timeTilHealthy = int(timeTilHealthy)

    if boottime + timeTilHealthy < int(time()):
        return "ok"
    abort(500, "not healthy yet")


@app.route('/delayedUnhealthy', method='GET')
def delayedUnhealthy():
    global boottime
    print("boottime: {}".format(boottime))
    timeTilHealthy = getenv("DELAY_SECONDS")
    if timeTilHealthy is None:
        timeTilHealthy = 10
    else:
        timeTilHealthy = int(timeTilHealthy)

    if boottime + timeTilHealthy > int(time()):
        return "ok"
    abort(500, "not unhealthy yet")


def main():
    global boottime
    boottime = int(time())
    print("storing boottime: {}".format(boottime))

    app.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":
    main()
