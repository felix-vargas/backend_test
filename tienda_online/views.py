from telnetlib import STATUS
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
from rest_framework.parsers import JSONParser
from tienda_online.models import Usuario,Producto,Categoria, Rol,Compra,Comentario,Puntuacion,Pregunta,Respuesta
from tienda_online.serializers import ProductoSerializer,UsuarioSerializer, CategoriaSerializer, RolSerializer
from django.core import serializers
# from django.contrib.auth.forms import UserCreationForm
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.decorators import api_view
from rest_framework.response import Response

def get_users(request):
    if request.method == 'GET':
        users = Usuario.objects.all()
        serializer = UsuarioSerializer(users, many=True)
        # users = serializers.serialize("json", Usuario.objects.all())
        # data = {"SomeModel_json": users}
        return JsonResponse(serializer.data, safe=False)
    return HttpResponse("No hay productos")



@csrf_exempt 
@api_view(['POST'])
def create_product(request):
    if request.method == 'POST':
        data = request.data
        serializer = ProductoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response("No hay productos", status=status.HTTP_400_BAD_REQUEST)


#funcionando
def create_category(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategoriaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    return HttpResponse("No se pudo crear la categoria")

def get_categories(request):
    if request.method == 'GET':
        categories = Categoria.objects.all()
        serializer = CategoriaSerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False)
    return HttpResponse("No hay productos")

def create_rol(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RolSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    return HttpResponse("No se pudo crear el rol")

def get_roles(request):
    if request.method == 'GET':
        roles = Rol.objects.all()
        serializer = RolSerializer(roles, many=True)
        #crear json
        return JsonResponse(serializer.data, safe=False)
    return HttpResponse("No hay productos")


def create_user(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    return HttpResponse("No se pudo crear el nuevo usuario")


#FUNCIONA
@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        email = data.get('email', '')
        password = data.get('password', '')

        try:
            user = Usuario.objects.get(email=email)
            if user.password == password:  # Use check_password method to verify password
                # Generate JWT token
                token = AccessToken.for_user(user)

                # Generate CSRF token
                csrf_token = get_token(request)

                # Return token and CSRF token in response
                return JsonResponse({'token': str(token), 'csrf_token': csrf_token}, status=200)
            else:
                return JsonResponse({'error': 'Invalid email or password'}, status=400)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=400)
    return HttpResponse("No se pudo iniciar sesion")

#FUNCIONA
@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        if 'rol' not in data:
            data['rol'] = 2
        serializer = UsuarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

#FUNCIONA
@csrf_exempt 
@api_view(['GET'])
def list_products(request):
    if request.method == 'GET':
        products = Producto.objects.all()
        print('\nProductos : ',products)
        serializer = ProductoSerializer(products, many=True)
        print('\nResponse after parsing : ',serializer.data)
        return JsonResponse(serializer.data, safe=False)
    return HttpResponse("No hay productos")


@csrf_exempt 
@api_view(['POST'])
def product_by_id(request):
    if request.method == 'POST':
        product_id = request.data.get('id', None)  # Assuming 'id' is the attribute containing the product ID
        if product_id is not None:
            try:
                product = Producto.objects.get(id=product_id)
                serializer = ProductoSerializer(product)
                return JsonResponse(serializer.data)
            except Producto.DoesNotExist:
                return JsonResponse({'error': 'Product not found'}, status=404)
        else:
            return JsonResponse({'error': 'ID attribute not provided in the request'}, status=400)
    return HttpResponse("Incorrect request method")


def send_email(request):
    email = 'miguel.rovlich@sansano.usm.cl'

    template = get_template('email-order.html')
    content = template.render({'email': email})

    email = EmailMultiAlternatives(
        'Asunto',
        "content",
        settings.EMAIL_HOST_USER,
        [email]
    )
    email.attach_alternative(content, 'text/html')
    email.send()
    return HttpResponse("Email enviado")