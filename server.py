#!/usr/bin/env python

from bottle import run
import main

if __name__ == "__main__":
  run(reloader=True, debug=True)
