from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Product, Supplier


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def add_product(request):
    # Check if the form submitted has a method post
    if request.method == "POST":
        # Start receiving data from the form
        p_name = request.POST.get('jina')
        p_quantity = request.POST.get('kiasi')
        p_price = request.POST.get('bei')

        # Finally save the data in our table called products
        product = Product(prod_name=p_name, prod_quantity=p_quantity, prod_price=p_price)
        product.save()
        # Redirect back with a success message
        messages.success(request, 'Product saved successfully')
        return redirect('add_product')
    return render(request, 'add_product.html')


@login_required
def view_products(request):
    # Select all the products to be displayed
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


@login_required()
def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    messages.success(request, 'Product deleted successfully')
    return redirect('products')


@login_required
def add_supplier(request):
    # Check if the form submitted has a method post
    if request.method == "POST":
        # Start receiving data from the form
        s_name = request.POST.get('jina')
        s_email = request.POST.get('pepe')
        s_goods = request.POST.get('bidhaa')

        # Finally save the data in our table called products
        supplier = Supplier(supp_name=s_name, supp_email=s_email, supp_goods=s_goods)
        supplier.save()
        # Redirect back with a success message
        messages.success(request, 'Supplier saved successfully')
        return redirect('add_supplier')
    return render(request, 'add_supplier.html')


@login_required
def update_product(request, id):
    # fetch the product to be updated
    product = Product.objects.get(id=id)
    # check if the form submitted has a method post
    if request.method == "POST":
        # Receive data from the form
        upd_name = request.POST.get('jina')
        upd_quantity = request.POST.get('kiasi')
        upd_price = request.POST.get('bei')
        # update the product with the received updated data
        product.prod_name = upd_name
        product.prod_quantity = upd_quantity
        product.prod_price = upd_price

        # return the dat back to the database and redirect
        product.save()
        messages.success(request, 'product updated successfully')
        return redirect('products')
    return render(request, 'update_product.html', {'product': product})


@login_required
def payment(request, id):
    # select the product to be paid
    product = Product.objects.get(id=id)
    return render(request, 'payment.html', {'product': product})
