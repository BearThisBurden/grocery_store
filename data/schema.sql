create table products (
	id_product tinyint(3) not null auto_increment primary key,
	product varchar(20) not null unique,
	description varchar(35) not null,
	stock tinyint(3) not null,
	purchase_cost tinyint(3) not null,
	sale_cost tinyint(3) not null,
	product_image varchar(200)
)
engine InnoDB default charset utf8;

insert into products(product, description, stock, purchase_cost, sale_cost) values('Chocolate', 'Cacao en polvo para bebidas', 55, 11, 22),
('Cereal', 'Hojuelas de maíz azucaradas', 32, 16, 33),	('Galletas', 'Galletas de mesa surtidas', 28, 18, 35),
('Pasta', 'Pasta de trigo para sopa', 50, 3, 8), ('Atún', 'Atún de aleta azul en aceite', 44, 5, 11);
