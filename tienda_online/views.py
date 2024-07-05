from telnetlib import STATUS
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
from rest_framework.parsers import JSONParser
from tienda_online.models import Usuario,Producto,Categoria, Rol,Compra,Comentario,Puntuacion,Pregunta,Respuesta
from tienda_online.serializers import ProductoSerializer,UsuarioSerializer, CategoriaSerializer, RolSerializer, CompraSerializer
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
def compra(request):
    if request.method == 'POST':
        basket = request.data.get('basket', [])
        for item in basket:
            try:
                product_id = item['id']
                selected_size = item['selectedSize']
                product = Producto.objects.get(id=product_id)
                if selected_size == 'S':
                    product.stock_s = max(0, product.stock_s - 1)
                    print("\nPRODUCTO COMPRADO TALLA S",product.stock_s)
                elif selected_size == 'M':
                    product.stock_m = max(0, product.stock_m - 1)
                    print("\nPRODUCTO COMPRADO TALLA M",product.stock_m)
                elif selected_size == 'L':
                    product.stock_l = max(0, product.stock_l - 1)
                    print("\nPRODUCTO COMPRADO TALLA L",product.stock_l)
                elif selected_size == 'XL':
                    product.stock_xl = max(0, product.stock_xl - 1)
                    print("\nPRODUCTO COMPRADO TALLA XL",product.stock_xl)
                else:
                    return JsonResponse({'error': f'Invalid size {selected_size}'}, status=400)
                product.save()
            except Producto.DoesNotExist:
                return JsonResponse({'error': f'Product with id {product_id} does not exist'}, status=404)
            except KeyError:
                return JsonResponse({'error': 'Invalid basket format, missing "id" or "selectedSize" key'}, status=400)
        
        return JsonResponse('GAMER', safe=False)
    return HttpResponse("Solicitud incorrecta")


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

@csrf_exempt 
@api_view(['POST'])
def send_email(request):
    email = 'danielmorales@gmail.com'

    # Assuming 'user_id' and 'some_data' are required for the register
    user_id = request.data.get('usuario')
    some_data = request.data.get('basket')
    subtotal = request.data.get('subtotal')
    payment = request.data.get('payment')
    shipping = request.data.get('shipping')



    if user_id is not None and some_data is not None:
        try:
            user = Usuario.objects.get(id=user_id)
            registro = Compra.objects.create(user=user_id, producto=some_data, cantidad=subtotal, estado='Procesando')
            registro_serializer = CompraSerializer(registro)
        except Usuario.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'User ID or data not provided'}, status=400)

    # Send email
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

    return HttpResponse("Email sent and register added successfully")