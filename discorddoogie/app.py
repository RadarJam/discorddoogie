"""
Write code here which need access to the app during runtime. 
You can decorate functions using '@pyttman.app.hooks.run("before_start")' and have 
them executed before the app goes online - useful for database connections and alike.
"""

import mongoengine
from pyttman import app

@app.hooks.run("before_start")
def _():
    mongoengine.connect(**app.settings.DATABASE)