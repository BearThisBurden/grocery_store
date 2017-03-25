import web
import model
        
urls = (
    '/index', 'Index',
    '/view/(.+)', 'View',
    '/insert', 'Insert',
)

app = web.application(urls, globals())

render = web.template.render('templates', base='base')

web.config.debug = False

class Index:        
    def GET(self):
        products = model.get_products()
        return render.index(products)

class View:
    def GET(self, id):
        id_product = int(id)
        product = model.get_product(id_product)
        return render.view(product)

class Insert(self):
    def GET(self):
        return render.insert()
    def POST(self):
        form = web.input()

        image = web.input(product_image = {})

        filedir = 'static/img'
        filepath = image.product_image.filename.replace('\\','/')
        filename = filepath.split('/')[-1]

        fout = open(filedir +'/'+ filename, 'w')
        fout.write(image.product_image.file.read())
        fout.close()
        product_image = filename

        model.insert(
            form['product'],
            form['description'],
            form['stock'],
            form['purchase_cost'],
            form['sale_cost'],
            product_image
            )
        raise web.seeother('/')     
             		        
if __name__ == "__main__":
    app.run()