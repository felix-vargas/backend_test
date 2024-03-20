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
    Producto.objects.create(nombre='Product 1', descripcion='Description 1', precio=10.0, talla='Large')
    Producto.objects.create(nombre='Product 2', descripcion='Description 2', precio=20.0, talla='Small')

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
