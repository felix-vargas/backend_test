from django.db import migrations

def create_initial_data(apps, schema_editor):
    Categoria = apps.get_model('tienda_online', 'Categoria')
    Producto = apps.get_model('tienda_online', 'Producto')
    Rol = apps.get_model('tienda_online', 'Rol')
    Usuario = apps.get_model('tienda_online', 'Usuario')

    # Create initial Categoria objects
    Categoria.objects.create(nombre='Category 1')
    Categoria.objects.create(nombre='Category 2')

    # Create initial Producto objects
    Producto.objects.create(nombre='Body Azul', categorias=f'mujer,body',descripcion=f'Body hecho a mano 100% algodon de color Azul', stock_s=20, stock_m=12, stock_l=1, stock_xl=6,precio=15000, talla='S,M,L,XL', imagen='polera_azul_14.jpg')
    Producto.objects.create(nombre='Body Azul Marino', categorias=f'mujer,body',descripcion=f'Body hecho a mano 100% algodon de color Azul Marino', stock_s=20, stock_m=12, stock_l=1, stock_xl=6,precio=15000, talla='S,M,L,XL',imagen='body_azulmarino_14.jpg')
    Producto.objects.create(nombre='Body Blanco', categorias=f'mujer,body',descripcion=f'Body hecho a mano 100% algodon de color Blanco', stock_s=20, stock_m=12, stock_l=1, stock_xl=6,precio=15000, talla='S,M,L,XL',imagen='body_blanco_M-L.jpg')
    Producto.objects.create(nombre='Body Amarillo Fuego', categorias=f'mujer,body',descripcion=f'Body hecho a mano 100% algodon de color Amarillo Fuego', stock_s=20, stock_m=12, stock_l=1, stock_xl=6,precio=15000, talla='S,M,L,XL',imagen='body_fuegoconamarillo_S-M.jpg')
    Producto.objects.create(nombre='Body Negro', categorias=f'mujer,body',descripcion=f'Body hecho a mano 100% algodon de color Negro', stock_s=20, stock_m=12, stock_l=1, stock_xl=6,precio=15000, talla='L',imagen='body_negro_M-L.jpg')
    Producto.objects.create(nombre='Body Rojo', categorias=f'mujer,body',descripcion=f'Body hecho a mano 100% algodon de color Rojo', stock_s=20, stock_m=12, stock_l=1, stock_xl=6,precio=15000, talla='S,M,L,XL',imagen='body_rojo_14.jpg')
    Producto.objects.create(nombre='Body Rosado', categorias=f'mujer,body',descripcion=f'Body hecho a mano 100% algodon de color Rosado', stock_s=20, stock_m=12, stock_l=1, stock_xl=6,precio=15000, talla='S,M,L,XL',imagen='body_rosado_M-L.jpg')
    Producto.objects.create(nombre='Calzas 38-44', categorias=f'mujer,pantalones',descripcion=f'Calzas hechas a mano 100% algodon.', stock_s=20, stock_m=12, stock_l=1, stock_xl=6,precio=10000, talla='38,39,40,41,42,43,44',imagen='calzas_38-44.jpg')
    Producto.objects.create(nombre='Lenceria S-M', categorias=f'mujer,lenceria',descripcion=f'Lenceria hecha a mano, 100% algodon, comoda y elasticada.', stock_s=20, stock_m=12, stock_l=1, stock_xl=6,precio=5000, talla='S,M',imagen='lenceria_S-M.jpg')
    Producto.objects.create(nombre='Lenceria L-XL', categorias=f'mujer,lenceria',descripcion=f'Lenceria hecha a mano, 100% algodon, comoda y elasticada.', stock_s=20, stock_m=12, stock_l=1, stock_xl=6,precio=5000, talla='L,XL',imagen='lenceria_L-XL.jpg')
    Producto.objects.create(nombre='Polera Azul', categorias=f'unisex,hombre,mujer,polera',descripcion='Polera de algodon de color, hecha a mano, pre encogida', stock_s=20, stock_m=12, stock_l=1, stock_xl=6,precio=8000, talla='S,M,L,XL',imagen='polera_azul_14.jpg')
    Producto.objects.create(nombre='Polera Blanca', categorias=f'unisex,hombre,mujer,polera',descripcion='Polera de algodon de color, hecha a mano, pre encogida', stock_s=20, stock_m=12, stock_l=1, stock_xl=6,precio=8000, talla='S,M,L,XL',imagen='polera_blanca_14.jpg')
    Producto.objects.create(nombre='Polera Celeste', categorias=f'unisex,hombre,mujer,polera',descripcion='Polera de algodon de color, hecha a mano, pre encogida', stock_s=20, stock_m=12, stock_l=1, stock_xl=6,precio=8000, talla='S,M,L,XL',imagen='polera_celeste_14.jpg')
    Producto.objects.create(nombre='Polera Morada', categorias=f'unisex,hombre,mujer,polera',descripcion='Polera de algodon de color, hecha a mano, pre encogida', stock_s=20, stock_m=12, stock_l=1, stock_xl=6,precio=8000, talla='S,M,L,XL',imagen='polera_morada_14.jpg')
    Producto.objects.create(nombre='Polera Naranja', categorias=f'unisex,hombre,mujer,polera',descripcion='Polera de algodon de color, hecha a mano, pre encogida', stock_s=20, stock_m=12, stock_l=1, stock_xl=6,precio=8000, talla='S,M,L,XL',imagen='polera_naranja_14.jpg')
    Producto.objects.create(nombre='Polera Negra con Naranjo', categorias=f'unisex,hombre,mujer,polera',descripcion='Polera de algodon de color, hecha a mano, pre encogida', stock_s=20, stock_m=12, stock_l=1, stock_xl=6,precio=8000, talla='S,M,L,XL',imagen='polera_negra_con_naranjo_14.jpg')
    Producto.objects.create(nombre='Polera Roja', categorias=f'unisex,hombre,mujer,polera',descripcion='Polera de algodon de color, hecha a mano, pre encogida', stock_s=20, stock_m=12, stock_l=1, stock_xl=6,precio=8000, talla='S,M,L,XL',imagen='polera_roja_14.jpg')
    Producto.objects.create(nombre='Polera Verde', categorias=f'unisex,hombre,mujer,polera',descripcion='Polera de algodon de color, hecha a mano, pre encogida', stock_s=20, stock_m=12, stock_l=1, stock_xl=6,precio=8000, talla='S,M,L,XL',imagen='polera_verde_14.jpg')
    Producto.objects.create(nombre='Poleron Negro Caleidoscopio', categorias=f'unisex,hombre,mujer,poleron',descripcion='Poleron de algodon de color, hecha a mano, pre encogida', stock_s=20, stock_m=12, stock_l=1, stock_xl=6,precio=25000, talla='S,M,L,XL',imagen='poleron_negro_xl.jpg')
    Producto.objects.create(nombre='Poleron Azul y Blanco', categorias=f'unisex,hombre,mujer,poleron',descripcion='Poleron de algodon de color, hecha a mano, pre encogida', stock_s=20, stock_m=12, stock_l=1, stock_xl=6,precio=25000, talla='S,M,L,XL',imagen='poleron_azul_y_blanco_L.jpg')
    Producto.objects.create(nombre='Poleron Blanco Celeste', categorias=f'unisex,hombre,mujer,poleron',descripcion='Poleron de algodon de color, hecha a mano, pre encogida', stock_s=20, stock_m=12, stock_l=1, stock_xl=6,precio=25000, talla='S,M,L,XL',imagen='poleron_blanco_S.jpg')
    Producto.objects.create(nombre='Poleron Blanco Negro', categorias=f'unisex,hombre,mujer,poleron',descripcion='Poleron de algodon de color, hecha a mano, pre encogida', stock_s=20, stock_m=12, stock_l=1, stock_xl=6,precio=25000, talla='S,M,L,XL',imagen='poleron_blanco_xl.jpg')
    Producto.objects.create(nombre='Poleron Negro Blanco', categorias=f'unisex,hombre,mujer,poleron',descripcion='Poleron de algodon de color, hecha a mano, pre encogida', stock_s=20, stock_m=12, stock_l=1, stock_xl=6,precio=25000, talla='S,M,L,XL',imagen='poleron_blanco_y_negro_L.jpg')
    Producto.objects.create(nombre='Poleron Gris', categorias=f'unisex,hombre,mujer,poleron',descripcion='Poleron de algodon de color, hecha a mano, pre encogida', stock_s=20, stock_m=12, stock_l=1, stock_xl=6,precio=25000, talla='S,M,L,XL',imagen='poleron_gris_S.jpg')
    Producto.objects.create(nombre='Poleron Morado', categorias=f'unisex,hombre,mujer,poleron',descripcion='Poleron de algodon de color, hecha a mano, pre encogida', stock_s=20, stock_m=12, stock_l=1, stock_xl=6,precio=25000, talla='S,M,L,XL',imagen='poleron_morado_L.jpg')
    Producto.objects.create(nombre='Poleron Naranjo', categorias=f'unisex,hombre,mujer,poleron',descripcion='Poleron de algodon de color, hecha a mano, pre encogida', stock_s=20, stock_m=12, stock_l=1, stock_xl=6,precio=25000, talla='S,M,L,XL',imagen='poleron_naranjo_xl.jpg')
    Producto.objects.create(nombre='Poleron Negro Splatter', categorias=f'unisex,hombre,mujer,poleron',descripcion='Poleron de algodon de color, hecha a mano, pre encogida', stock_s=20, stock_m=12, stock_l=1, stock_xl=6,precio=25000, talla='S,M,L,XL',imagen='poleron_negro_L.jpg')

    # Create initial Rol objects
    Rol.objects.create(nombre='Admin')
    Rol.objects.create(nombre='User')

    # Create initial Usuario objects
    Usuario.objects.create(nombre='admin', apellido='admin', email='admin@admin.com', password='admin', rol_id=1)
    Usuario.objects.create(nombre='test', apellido='test', email='test@test.com', password='test', rol_id=2)

class Migration(migrations.Migration):

    dependencies = [
        ('tienda_online', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_data),
    ]