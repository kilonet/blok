from werkzeug.debug import DebuggedApplication
from werkzeug import run_simple
from blok.application import Blok
import os
from werkzeug.wsgi import SharedDataMiddleware

application = Blok()
#application = DebuggedApplication(application, evalex=True)
application = SharedDataMiddleware(application, {
    '/static':     os.path.join(os.getcwd(), 'blok/static')
})
run_simple('localhost', 4000, application, use_reloader=True)



