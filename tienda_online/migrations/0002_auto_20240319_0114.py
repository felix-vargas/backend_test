from django.db import migrations

def create_initial_data(apps, schema_editor):
    Categoria = apps.get_model('tienda_online', 'Categoria')
    Producto = apps.get_model('tienda_online', 'Producto')
    Rol = apps.get_model('tienda_online', 'Rol')
    Usuario = apps.get_model('tienda_online', 'Usuario')

    # Create initial Categoria objects
    Categoria.objects.create(nombre='mujer')
    Categoria.objects.create(nombre='hombre')
    Categoria.objects.create(nombre='unisex')
    Categoria.objects.create(nombre='poleron')
    Categoria.objects.create(nombre='body')
    Categoria.objects.create(nombre='pantalones')
    Categoria.objects.create(nombre='lenceria')

    # Create initial Categoria objects
    mujer = Categoria.objects.create(nombre='mujer')
    hombre = Categoria.objects.create(nombre='hombre')
    unisex = Categoria.objects.create(nombre='unisex')
    poleron = Categoria.objects.create(nombre='poleron')
    body = Categoria.objects.create(nombre='body')
    pantalones = Categoria.objects.create(nombre='pantalones')
    lenceria = Categoria.objects.create(nombre='lenceria')

    # Create initial Producto objects
    body_azul = Producto.objects.create(
        nombre='Body Azul',
        descripcion='Body hecho a mano 100% algodon de color Azul',
        stock_s=20,
        stock_m=12,
        stock_l=1,
        stock_xl=6,
        precio=15000,
        talla='S,M,L,XL',
        imagen='polera_azul_14.jpg'
    )
    body_azul.categorias.add(mujer, body)

    body_azul_marino = Producto.objects.create(
        nombre='Body Azul Marino',
        descripcion='Body hecho a mano 100% algodon de color Azul Marino',
        stock_s=20,
        stock_m=12,
        stock_l=1,
        stock_xl=6,
        precio=15000,
        talla='S,M,L,XL',
        imagen='body_azulmarino_14.jpg'
    )
    body_azul_marino.categorias.add(mujer, body)

    body_blanco = Producto.objects.create(
        nombre='Body Blanco',
        descripcion='Body hecho a mano 100% algodon de color Blanco',
        stock_s=20,
        stock_m=12,
        stock_l=1,
        stock_xl=6,
        precio=15000,
        talla='S,M,L,XL',
        imagen='body_blanco_M-L.jpg'
    )
    body_blanco.categorias.add(mujer, body)

    body_amarillo_fuego = Producto.objects.create(
        nombre='Body Amarillo Fuego',
        descripcion='Body hecho a mano 100% algodon de color Amarillo Fuego',
        stock_s=20,
        stock_m=12,
        stock_l=1,
        stock_xl=6,
        precio=15000,
        talla='S,M,L,XL',
        imagen='body_fuegoconamarillo_S-M.jpg'
    )
    body_amarillo_fuego.categorias.add(mujer, body)

    body_negro = Producto.objects.create(
        nombre='Body Negro',
        descripcion='Body hecho a mano 100% algodon de color Negro',
        stock_s=20,
        stock_m=12,
        stock_l=1,
        stock_xl=6,
        precio=15000,
        talla='L',
        imagen='body_negro_M-L.jpg'
    )
    body_negro.categorias.add(mujer, body)

    body_rojo = Producto.objects.create(
        nombre='Body Rojo',
        descripcion='Body hecho a mano 100% algodon de color Rojo',
        stock_s=20,
        stock_m=12,
        stock_l=1,
        stock_xl=6,
        precio=15000,
        talla='S,M,L,XL',
        imagen='body_rojo_14.jpg'
    )
    body_rojo.categorias.add(mujer, body)

    body_rosado = Producto.objects.create(
        nombre='Body Rosado',
        descripcion='Body hecho a mano 100% algodon de color Rosado',
        stock_s=20,
        stock_m=12,
        stock_l=1,
        stock_xl=6,
        precio=15000,
        talla='S,M,L,XL',
        imagen='body_rosado_M-L.jpg'
    )
    body_rosado.categorias.add(mujer, body)

    calzas = Producto.objects.create(
        nombre='Calzas 38-44',
        descripcion='Calzas hechas a mano 100% algodon.',
        stock_s=20,
        stock_m=12,
        stock_l=1,
        stock_xl=6,
        precio=10000,
        talla='38,39,40,41,42,43,44',
        imagen='calzas_38-44.jpg'
    )
    calzas.categorias.add(mujer, pantalones)

    lenceria_sm = Producto.objects.create(
        nombre='Lenceria S-M',
        descripcion='Lenceria hecha a mano, 100% algodon, comoda y elasticada.',
        stock_s=20,
        stock_m=12,
        stock_l=1,
        stock_xl=6,
        precio=5000,
        talla='S,M',
        imagen='lenceria_S-M.jpg'
    )
    lenceria_sm.categorias.add(mujer, lenceria)

    lenceria_lxl = Producto.objects.create(
        nombre='Lenceria L-XL',
        descripcion='Lenceria hecha a mano, 100% algodon, comoda y elasticada.',
        stock_s=20,
        stock_m=12,
        stock_l=1,
        stock_xl=6,
        precio=5000,
        talla='L,XL',
        imagen='lenceria_L-XL.jpg'
    )
    lenceria_lxl.categorias.add(mujer, lenceria)

    # Repeat similar structure for other products
    # Example for another product with multiple categories

    polera_azul = Producto.objects.create(
        nombre='Polera Azul',
        descripcion='Polera de algodon de color, hecha a mano, pre encogida',
        stock_s=20,
        stock_m=12,
        stock_l=1,
        stock_xl=6,
        precio=8000,
        talla='S,M,L,XL',
        imagen='polera_azul_14.jpg'
    )
    polera_azul.categorias.add(unisex, hombre, mujer, poleron)
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