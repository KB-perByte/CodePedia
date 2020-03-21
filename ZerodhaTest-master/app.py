import os, json, cherrypy
from bseHandler import stockTopTen, stockByName, getOperationDetails , saveToRedis

class MainPage(object):
    @cherrypy.expose
    def index(self):
        return open("index.html")

@cherrypy.expose
class StockList(object):
    @cherrypy.tools.accept(media='text/plain')
    @cherrypy.tools.json_out()
    def GET(self):
        return stockTopTen()

@cherrypy.expose
class StockListUpdate(object):
    @cherrypy.tools.accept(media='text/plain')
    @cherrypy.tools.json_out()
    def GET(self):
        saveToRedis()
        return {'Response' : True}

@cherrypy.expose
class OperationDetails(object):
    @cherrypy.tools.accept(media='text/plain')
    @cherrypy.tools.json_out()
    def GET(self):
        _fechDate = getOperationDetails()
        if _fechDate:
            return _fechDate[0] ,_fechDate[1]
        else:
            return None

@cherrypy.expose
class StockSearch(object):
    @cherrypy.tools.accept(media='text/plain')
    @cherrypy.tools.json_out()
    def GET(self, name):
        return stockByName(name)

if __name__ == "__main__":

    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/update':{
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/operation':{
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/stocks': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/stocks/search': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'public'
        }
    }
    cherrypy.config.update('app.ini')
    bseApp = MainPage()
    bseApp.update = StockListUpdate()
    bseApp.stocks = StockList()
    bseApp.operation = OperationDetails()
    bseApp.stocks.search = StockSearch()
    cherrypy.quickstart(bseApp, '/', conf)
