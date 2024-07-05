from django.db import models



class Rol(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre




class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, null=False, blank=False)
    def __str__(self):
        return self.nombre



class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    precio = models.FloatField()
    stock_s = models.IntegerField()
    stock_m = models.IntegerField()
    stock_l = models.IntegerField()
    stock_xl =models.IntegerField()
    talla = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='productos', null=True, blank=True)
    def __str__(self):
        return self.nombre


class Compra(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    def __str__(self):
        return "Compra de " + str(self.cantidad) + " " + self.producto.nombre + " por " + self.usuario.nombre

class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=50)
    def __str__(self):
        return self.usuario

class Puntuacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()
    def __str__(self):
        return self.usuario

class Pregunta(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pregunta = models.CharField(max_length=50)
    def __str__(self):
        return self.usuario


class Respuesta(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=50)
    def __str__(self):
        return self.usuario
