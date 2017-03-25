import web

db_host = 'localhost'
db_name = 'grocery_store'
db_user = 'root'
db_pw = ''

db = web.database(
	dbn = 'mysql',
	host = db_host,
	db = db_name,
	user = db_user,
	pw = db_pw
	)

def get_products():
	try:
		return db.select('products')
	except:
		return None

def get_product(id_product):
	try:
		return db.select('products', where = 'id_product = $id_product', vars = locals())
	except:
		return None

def insert(product, description, purchase_cost, sale_cost, product_image):
	db.insert('products', product = product, description = description, stock = stock, purchase_cost = purchase_cost, sale_cost = sale_cost, product_image = product_image)	 