import web

urls = (
    '/index', 'index',
    '/demo',  'demo',
    '/name/(.*)', 'name',
    '/input', 'input',
    '/chart', 'chart',

    '/',  'error',
    '/.*', 'error'
)
app = web.application(urls, globals())

render = web.template.render('templates')

class index:
    def GET(self): 
        return render.index()

class input:
    def GET(self):
        #http://0.0.0.0:1234/input?id=8,age=2
        i = web.input(id=None, age=None)
        return render.input(i.id, i.age)

class demo:    
    def GET(self):
        return render.demo()

class name:
    def GET(self, name):
        if not name:
            name = 'world'
        return "hello, " + name

class chart:
    def GET(self):
        return render.chart()

class error:
    def GET(self):
        return render.e404()

if __name__ == "__main__":
    app.run()
