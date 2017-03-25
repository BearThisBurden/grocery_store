import web

db_host = 'edo4plet5mhv93s3.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'tf71g665v2egz9ft'
db_user = 'psveutvxir3d6sja'
db_pw = 'qg2trvbysgtdxj5w'

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
