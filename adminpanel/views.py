from functools import total_ordering
from django.db.models.fields import DecimalField
from django.shortcuts import get_object_or_404, render, redirect
from restaurant.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Sum, Avg
from django.contrib import messages
from .models import Contact
import csv

import json


def login_for_admin(request):
    # shop_id = get_object_or_404(Shop, pk=shop_id)
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_authenticated:
            # print(user.id)
                print(user)
                shop_id = get_object_or_404(Shop, user=user)
                print(shop_id)
                login(request, user)
                return redirect(f"/adminpanel/home/{shop_id.id}/")
            else:
                return HttpResponse("Something Went Wrong")
    args = {}
    return render(request, "account/admin_login.html", args)


def logoutView(request):
    # shop_id = get_object_or_404(Shop, pk=shop_id)
    logout(request)
    return redirect("login_for_admin")



@login_required(login_url="login_for_admin")
def adminpanelHome(request, shop_id):
    shop_id = get_object_or_404(Shop, pk=shop_id)
    if shop_id.user == request.user:
        customer_amount = Customer.objects.filter(
            added_by = request.user
        ).count()
        # Gross Sales
        gs = RestCheckout.objects.filter(
            shop=shop_id
        ).aggregate(Avg("grand_total"))
        gs_sale = gs.pop("grand_total__avg")
        # Total Transaction
        total_transaction = RestCheckout.objects.filter(
            shop=shop_id
        ).aggregate(Sum("grand_total"))
        # delete_key = "grand_total"
        pipi = total_transaction.pop("grand_total__sum")
        print(pipi)
        # del total_transaction["grand_total__sum"]
        print(type(total_transaction))

        # json.dumps(str(total_transaction))
        
        print(str(total_transaction))
        print(customer_amount)
        args = {
            "shop_id": shop_id,
            "customer_amount": customer_amount,
            "total_transaction": total_transaction,
            "gs": gs,
            "pipi": pipi,
            "gs_sale": gs_sale
        }
        return render(request, "adminpanel/admin-panel.html", args)
    else:
        return HttpResponse("You are not the owner of this shop")


@login_required(login_url="login_for_admin")
def adminpanelOrder(request, shop_id):
    shop_id = get_object_or_404(Shop, pk=shop_id)
    if shop_id.user == request.user:
        orders = RestCheckout.objects.filter(
            shop=shop_id
        )

        args = {
            "orders": orders,
            "shop_id": shop_id,
        }
        return render(request, "adminpanel/orders.html", args)
    else:
        return HttpResponse("You are not the owner of this shop")

# Department
def departmentHomeView(request, shop_id):
    shop_id = get_object_or_404(Shop, pk=shop_id)
    if shop_id.user == request.user:
        args = {
            "shop_id": shop_id
        }
        return render(request, "department/department.html", args)
    else:
        return HttpResponse("You are not the owner of this shop")

def createDepartmentCategory(request):
    args = {

    }
    return render(request, "department/new-category.html", args)
   

def editDepartmentView(request):
    args = {

    }
    return render(request, "department/edit-department.html", args)

def createDepartmentView(request):
    args = {

    }
    return render(request, "department/new-department.html", args)

def createItemDepartmentView(request):
    args = {

    }
    return render(request, "department/new-item.html", args)

# Category
def categoryHomeView(request, shop_id):
    shop_id = get_object_or_404(Shop, pk=shop_id)
    if shop_id.user == request.user:
        category = Category.objects.filter(
            shop=shop_id,
        )
        args = {
            "shop_id": shop_id,
            "category": category,
        }
        return render(request, "category/category.html", args)
    else:
        return HttpResponse("You are not the owner of this shop")


def editCategoryView(request, shop_id, cat_id):
    shop_id = get_object_or_404(Shop, id=shop_id)

    if shop_id.user == request.user:
        user_shops = Shop.objects.filter(user=request.user, is_active=True)
        category_obj = get_object_or_404(Category, pk=cat_id)
    else:
        return HttpResponse("Sorry! You are not the owner of this shop")

    args = {
        "shop_id": shop_id,
        "user_shops": user_shops,
        "category_obj": category_obj
    }
    return render(request, "category/edit-category.html", args)

def adminEditCategoryView(request, shop_id, cat_id):
    cat_obj = get_object_or_404(Category, id=cat_id)
    shop_obj = get_object_or_404(Shop, id=shop_id)

    # print("SHOP Name:", shop_obj.shop_name)

    if request.method == "POST":
        cat_name = request.POST.get("category_name")

        if cat_name:
            cat_obj.category_name = cat_name
            cat_obj.shop = shop_obj

            cat_obj.save()

            return redirect(f"/adminpanel/category/{shop_id}/")
        else:
            return redirect(f"/adminpanel/edit-category/{shop_id}/{cat_id}/")

        



def createCategoryView(request, shop_id):
    shop_id = get_object_or_404(Shop, pk=shop_id)
    if shop_id.user == request.user:

        shops = Shop.objects.filter(
            user=request.user
        )

        if request.method == "POST":
            category_name = request.POST.get("category_name")
            shop = request.POST.get("shop")

            category = Category(
                category_name=category_name,
                shop=Shop.objects.get(id=shop_id.id)
            )

            category.save()

            return redirect(f"/adminpanel/category/{shop_id.id}/")
        # else:
        #     return HttpResponse("Failed! Please Contact With The Support!")

        args = {
            "shop_id": shop_id,
            "shops": shops
        }
        return render(request, "category/new-category.html", args)
    else:
        return HttpResponse("Sorry You are not the owner of this shop")

# brand
def brandHomeView(request, shop_id):
    shop_id = get_object_or_404(Shop, id=shop_id)

    if shop_id.user == request.user:
        brands = Brand.objects.filter(shop=shop_id)
    else:
        return HttpResponse("Sorry! You are not the owner of this shop")

    args = {
        "shop_id": shop_id,
        "brands": brands,
    }
    return render(request, "brand/brand.html", args)

def createBrand(request, shop_id):
    shop_id = get_object_or_404(Shop, id=shop_id)

    if shop_id.user != request.user:
        return HttpResponse("Sorry! You are not the owner of this shop")

    args = {
        "shop_id": shop_id,
    }
    return render(request, "brand/new-brand.html", args)  

def adminCreateBrand(request, shop_id):
    shop_obj = get_object_or_404(Shop, id=shop_id)

    if request.method == "POST":
        brand_name = request.POST.get("brand_name")
        
        if brand_name:
            Brand.objects.create(
                brand_name=brand_name,
                shop=shop_obj
            )
            return redirect(f"/adminpanel/brand/{shop_obj.id}/")
        else:
            return redirect(f"/adminpanel/create-brand/{shop_obj.id}/")
    else:
        return redirect(f"/adminpanel/create-brand/{shop_obj.id}/") 
    
def editBrandView(request, shop_id, brand_id):
    shop_id = get_object_or_404(Shop, id=shop_id)

    if shop_id.user == request.user:
        brand_obj = get_object_or_404(Brand, id=brand_id)
    else:
        return HttpResponse("Sorry! You are not the owner of this shop")

    args = {
        "shop_id": shop_id,
        "brand_obj": brand_obj,
    }
    return render(request, "brand/edit-brand.html", args)

def adminEditBrand(request, shop_id, brand_id):
    brand_obj = get_object_or_404(Brand, id=brand_id)
    shop = get_object_or_404(Shop, id=shop_id)

    if request.method == "POST":
        brand_name = request.POST.get("brand_name")

        if brand_name:
            brand_obj.brand_name = brand_name
            brand_obj.shop = shop

            brand_obj.save()
        else:
            return redirect(f"/adminpanel/edit-brand/{shop_id}/{brand_id}/")

        return redirect(f"/adminpanel/brand/{shop_id}/")


def adminDeleteBrand(request, shop_id, brand_id):
    brand_obj = get_object_or_404(Brand, id=brand_id)
    brand_obj.delete()

    return redirect(f"/adminpanel/brand/{shop_id}/")

def newBrandItem(request, shop_id):
    shop_id = get_object_or_404(Shop, id=shop_id)

    args = {
        "shop_id": shop_id,
    }
    return render(request, "brand/new-brand-item.html", args)                 

def adminDeleteCategoryiew(request, shop_id, cat_id):
    category_obj = get_object_or_404(Category, id=cat_id)

    # print(category_obj)
    
    category_obj.delete()
    return redirect(f"/adminpanel/category/{shop_id}/")
        

def createCategoryItemView(request):
    args = {

    }
    return render(request, "category/new-category-item.html", args)

# Product
def productHomeView(request, shop_id):
    shop_id = get_object_or_404(Shop, pk=shop_id)
    if shop_id.user == request.user:

        products = Item.objects.filter(
            shop=shop_id
        )

        args = {
            "shop_id": shop_id,
            "products": products,
        }
        return render(request, "product/product.html", args)

    else:
        return HttpResponse("You are not the owner of this shop")

def editProducteView(request, shop_id, prod_id):
    shop_id = get_object_or_404(Shop, id=shop_id)

    if shop_id.user == request.user:
        prod_obj = get_object_or_404(Item, id=prod_id)
        categories = Category.objects.filter(shop=shop_id)
        vendors = Vendor.objects.filter(shop=shop_id)
        brands = Brand.objects.filter(shop=shop_id)
    else:
        return HttpResponse("Sorry! You are not the owner of this shop")

    args = {
        "shop_id": shop_id,
        "prod_obj": prod_obj,
        "categories": categories,
        "vendors": vendors,
        "brands": brands,
    }
    return render(request, "product/edit-product.html", args)

def adminEditProductView(request, shop_id, prod_id):
    shop_id = get_object_or_404(Shop, id=shop_id)
    prod_obj = get_object_or_404(Item, id=prod_id)
    prod_image, selected_brand, upc = None, None, None
    out_of_stock = False

    if request.method == "POST":
        product_name = request.POST.get("product_name")
        product_description = request.POST.get("product_description")
        get_category = request.POST.get("category")
        get_upc = request.POST.get("upc")
        sku = request.POST.get("sku")
        product_img = request.FILES.get("uploadImg")
        buying_price = request.POST.get("buying_price")
        selling_price = request.POST.get("selling_price")
        get_vendor = request.POST.get("get_vendor")
        get_brand = request.POST.get("brand")
        product_stock = request.POST.get("product_stock")
        get_out_of_stock = request.POST.get("out_of_stock")
        
        category = get_object_or_404(Category, id=get_category)
        vendor = get_object_or_404(Vendor, id=get_vendor)

        if get_brand == "":
            selected_brand = None
        else:
            selected_brand = get_object_or_404(Brand, id=get_brand)

        if get_out_of_stock == "yes":
            out_of_stock = True

        if len(get_upc) > 0:
            upc = get_upc
        
        print(product_img is None)
        print(product_img)
        if product_name and product_description and sku and buying_price and selling_price and category and vendor and product_stock:
            if product_img is None:
                prod_obj.item_name = product_name
                prod_obj.item_price = selling_price
                prod_obj.buying_price = buying_price
                prod_obj.brand = selected_brand
                prod_obj.category = category
                prod_obj.vendor = vendor
                prod_obj.shop = shop_id
                prod_obj.stock_amount = product_stock
                prod_obj.out_of_stock = out_of_stock
                prod_obj.upc = upc
                prod_obj.sku = sku
                prod_obj.product_descriptions = product_description
            else:
                prod_obj.item_name = product_name
                prod_obj.item_price = selling_price
                prod_obj.buying_price = buying_price
                prod_obj.brand = selected_brand
                prod_obj.category = category
                prod_obj.vendor = vendor
                prod_obj.shop = shop_id
                prod_obj.item_img = product_img
                prod_obj.stock_amount = product_stock
                prod_obj.out_of_stock = out_of_stock
                prod_obj.upc = upc
                prod_obj.sku = sku
                prod_obj.product_descriptions = product_description

            prod_obj.save()
        else:
            return redirect(f"/adminpanel/edit-product/{shop_id.id}/{prod_obj.id}/")
    return redirect(f"/adminpanel/product/{shop_id.id}/")

def createProducteView(request, shop_id):
    shop_id = get_object_or_404(Shop, pk=shop_id)

    if shop_id.user != request.user:
        return HttpResponse("Sorry! You are not the owner of this shop")

    vendors = Vendor.objects.filter(shop=shop_id)

    get_upc, get_brand, vendor = None, None, None
    out_of_stock = False

    categories = Category.objects.filter(shop=shop_id)
    brands = Brand.objects.filter(shop=shop_id)

    if request.method == "POST":
        item_name = request.POST.get("item_name")
        product_description = request.POST.get("product_descriptions")
        brand = request.POST.get("brand")
        get_category = request.POST.get("category")
        upc = request.POST.get("upc")
        sku = request.POST.get("sku")
        product_stock = request.POST.get("product_stock")
        get_out_of_stock = request.POST.get("out_of_stock")
        uploadImg = request.FILES.get("uploadImg")
        buying_price = request.POST.get("buying_price")
        selling_price = request.POST.get("item_price")
        get_vendor = request.POST.get("vendor")

        if len(upc) > 0:
            get_upc = upc
        
        if get_out_of_stock == "yes":
            out_of_stock = True

        category = get_object_or_404(Category, id=get_category)
        
        if brand == "":
            get_brand = None
        else:
            get_brand = get_object_or_404(Brand, id=brand)

        if get_vendor != "" or get_vendor is not None:
            vendor = get_object_or_404(Vendor, id=get_vendor)
            print(vendor)
            if item_name and product_description and sku and category and product_stock and uploadImg and buying_price and selling_price:
                Item.objects.create(
                    item_name=item_name,
                    item_price=selling_price,
                    buying_price=buying_price,
                    brand=get_brand,
                    category=category,
                    vendor=vendor,
                    shop=shop_id,
                    stock_amount=product_stock,
                    out_of_stock=out_of_stock,
                    item_img=uploadImg,
                    upc=get_upc,
                    sku=sku,
                    product_descriptions=product_description,
                )
                return redirect(f"/adminpanel/product/{shop_id.id}/")
            else:
                return redirect(f"/adminpanel/create-product/{shop_id.id}/")
        else:
            return redirect(f"/adminpanel/create-product/{shop_id.id}/")


    args = {
        "shop_id": shop_id,
        "categories": categories,
        "brands": brands,
        "vendors": vendors,
    }
    return render(request, "product/new-product.html", args)




# customer
def customerHomeView(request, shop_id):
    shop_id = get_object_or_404(Shop, pk=shop_id)
    if shop_id.user == request.user:
        customers = Customer.objects.filter(added_by=request.user)
        args = {
            "shop_id": shop_id,
            "customers": customers,
        }
        return render(request, "customers/customer.html", args)
    else:
        return HttpResponse("You are not the owner of this shop")



def editCustomerView(request, shop_id, cust_id):
    shop_id = get_object_or_404(Shop, id=shop_id)

    if shop_id.user == request.user:
        customer_obj = get_object_or_404(Customer, id=cust_id)
        customer_obj = get_object_or_404(Customer, added_by=shop_id.user, id=customer_obj.id)
    else:
        return HttpResponse("Sorry! You are not the owner of this shop")
    

    args = {
        "shop_id": shop_id,
        "customer_obj": customer_obj,
    }
    return render(request, "customers/edit-customer.html", args)    

def adminEditCustomerView(request, shop_id, cust_id):
    shop_obj = get_object_or_404(Shop, id=shop_id)
    customer_obj = get_object_or_404(Customer, id=cust_id)

    if request.method == "POST":
        cust_name = request.POST.get("cust_name")
        cust_contact = request.POST.get("cust_contact")
        cust_email = request.POST.get("cust_email")
        cust_address = request.POST.get("cust_address")

        if cust_name and cust_contact and cust_email and cust_address:
            customer_obj.customer_name = cust_name
            customer_obj.customer_contact = cust_contact
            customer_obj.customer_email = cust_email
            customer_obj.customer_add = cust_address

            customer_obj.save()
            return redirect(f"/adminpanel/customer/{shop_id}/")
        else:
            return redirect(f"/adminpanel/edit-customer/{shop_id}/{cust_id}/")


def personalCustomerView(request):
    args = {

    }
    return render(request, "customers/personal-customer.html", args)     

def businessCustomerView(request):
    args = {

    }
    return render(request, "customers/business-customer.html", args)     


# vendor
def vendorView(request, shop_id):
    shop_id = get_object_or_404(Shop, pk=shop_id)
    if shop_id.user == request.user:

        vendors = Vendor.objects.filter(
            shop=shop_id
        )
        args = {    
            "shop_id": shop_id,
            "vendors": vendors,
        }
        return render(request, "vendor/vendor.html", args)  
    else:
        return HttpResponse("You are not the owner of this shop")


def editVendorView(request, shop_id, vendor_id):
    vendorId = get_object_or_404(Vendor, id=vendor_id)
    shop_id = get_object_or_404(Shop, id=shop_id)
    countrys = CountryModel.objects.all()
    citys = CityModel.objects.all()

    if shop_id.user != request.user:
        return HttpResponse("Sorry! You are not the owner of this shop")

    if request.method == "POST":
        vendor_name = request.POST.get("vendor_name")
        tax_id = request.POST.get("tax_id")
        shop = shop_id
        address = request.POST.get("address")
        country = request.POST.get("country")
        city = request.POST.get("city")
        zip_code = request.POST.get("zip_code")
        phone_number = request.POST.get("phone_number")
        contact_name = request.POST.get("contact_name")
        email = request.POST.get("email")
        website = request.POST.get("website")
        trade_license = request.POST.get("trade_license")

        if vendor_name and tax_id and address and country and city and zip_code and phone_number and contact_name and email and website and trade_license:
            vendorId.vendor_name = vendor_name
            vendorId.tax_id = tax_id
            vendorId.shop = shop
            vendorId.address = address
            vendorId.country = CountryModel.objects.get(country_name=country)
            vendorId.city = CityModel.objects.get(city_name=city)
            vendorId.zip_code = zip_code
            vendorId.phone_number = phone_number
            vendorId.contact_name = contact_name
            vendorId.email = email
            vendorId.website = website
            vendorId.trade_license = trade_license

            vendorId.save()

            return redirect(f"/adminpanel/vendor/{shop_id.id}/")


    args = {
        "shop_id": shop_id,
        "vendorId": vendorId,
        "countrys": countrys,
        "citys": citys,
    }
    return render(request, "vendor/edit-vendor.html", args)

def createVendorView(request, shop_id):
    shop_id = get_object_or_404(Shop, pk=shop_id)
    countrys = CountryModel.objects.all()
    citys = CityModel.objects.all()
    if shop_id.user == request.user:
        if request.method == "POST":
            vendor_name = request.POST.get("vendor_name")
            tax_id = request.POST.get("tax_id")
            shop = shop_id
            address = request.POST.get("address")
            country = request.POST.get("country")
            city = request.POST.get("city")
            zip_code = request.POST.get("zip_code")
            phone_number = request.POST.get("phone_number")
            contact_name = request.POST.get("contact_name")
            email = request.POST.get("email")
            website = request.POST.get("website")
            trade_license = request.POST.get("trade_license")

            vendor_exist = Vendor.objects.filter(vendor_name=vendor_name)

            if vendor_exist.exists():
                messages.error(request, "Vendor already exists!")
                return redirect(f"/adminpanel/create-vendor/{shop_id.id}")

            if vendor_name and tax_id and address and country and city and zip_code and phone_number and contact_name and email and website and trade_license:
                vendor = Vendor(
                    vendor_name=vendor_name,
                    tax_id=tax_id,
                    shop=shop,
                    address=address,
                    country=CountryModel.objects.get(country_name=country),
                    city=CityModel.objects.get(city_name=city),
                    zip_code=zip_code,
                    phone_number=phone_number,
                    contact_name=contact_name,
                    email=email,
                    website=website,
                    trade_license=trade_license
                )
                vendor.save()
                print(str(vendor))
                return HttpResponse("Success with website")
            else:
                vendor = Vendor(
                    vendor_name=vendor_name,
                    tax_id=tax_id,
                    shop=shop,
                    address=address,
                    country=country,
                    city=city,
                    zip_code=zip_code,
                    phone_number=phone_number,
                    contact_name=contact_name,
                    email=email,
                    trade_license=trade_license
                )
                vendor.save()
                print(str(vendor))
                return HttpResponse("Success without website")
        args = {
            "shop_id": shop_id,
            "countrys": countrys,
            "citys": citys,
        }   
        return render(request, "vendor/create-vendor.html", args)     
    else:
        return HttpResponse("You are not the owner of this shop!")


def deleteVendorView(request, shop_id, vendor_id):
    shop_obj = get_object_or_404(Shop, id=shop_id)

    if request.method == "POST":
        vendor_obj = get_object_or_404(Vendor, id=vendor_id)
        vendor_obj.delete()

        return redirect(f"/adminpanel/vendor/{shop_obj.id}/")


# employee    
def employeeView(request):
    args = {

    }   
    return render(request, "employee/employee.html", args)

def editEmployeeView(request):
    args = {

    }   
    return render(request, "employee/edit-employee.html", args)  

def createEmployeeView(request):
    args = {

    }   
    return render(request, "employee/create-employee.html", args)       


# contact    

def contactView(request, shop_id):
    shop_id = get_object_or_404(Shop, id=shop_id)
    countries = CountryModel.objects.all()

    args = {
        "shop_id": shop_id,
        "countries": countries,
    }
    return render(request, "adminpanel/contact.html", args)    

def submitContact(request, shop_id):
    shop_obj = get_object_or_404(Shop, id=shop_id)
    get_address2 = None

    if request.method == "POST":
        shop_name = request.POST.get("shop_name")
        address1 = request.POST.get("address1")
        address2 = request.POST.get("address2")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zip = request.POST.get("zip")
        country = request.POST.get("country")
        website = request.POST.get("website")
        email = request.POST.get("email")
        message = request.POST.get("message")

        shop = get_object_or_404(Shop, shop_name=shop_name)

        if len(address2) > 0:
            get_address2 = address2

        country = get_object_or_404(CountryModel, country_name=country)

        if shop_name and address1 and city and state and zip and country and website and email and message:
            Contact.objects.create(
                shop=shop,
                address1=address1,
                address2=get_address2,
                city=city,
                state=state,
                zip=zip,
                country=country,
                website=website,
                email=email,
                message=message
            )
            messages.success(request, "Your message is sent successfully!")
            return redirect(f"/adminpanel/contact/{shop_id}/")
        else:
            return redirect(f"/adminpanel/home/{shop_id}/")




# exceptions
# success
def successView(request):
    args = {

    }
    return render(request, "exceptions/success.html", args)  

# failed
def failedView(request):
    args = {

    }
    return render(request, "exceptions/failed.html", args)   
    
# not found
def notFoundView(request):
    args = {

    }
    return render(request, "exceptions/notFound.html", args)      

 # warning
def warningView(request):
    args = {

    }
    return render(request, "exceptions/warning.html", args)

# Export
def exportCustomerData(request, shop_id):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="filename.csv"'
    writer = csv.writer(response)
    writer.writerow(["added_by", "customer_name", "customer_contact", "customer_email", "customer_add", "created_at"])
    data = Customer.objects.filter(added_by=request.user)
    for row in data:
        rowobj = [row.customer_name, row.customer_contact, row.customer_email, row.customer_add, row.created_at]
        writer.writerow(rowobj)
    return response

def exportProductData(request, shop_id):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="filename.csv"'
    writer = csv.writer(response)
    writer.writerow(["item_name", "item_price", "buying_price", "brand", "category", "vendor", "shop", "stock_amount", "out_of_stock", "item_img", "product_descriptions", "upc", "sku", "created_at"])
    data = Item.objects.filter(shop=shop_id)
    for row in data:
        rowobj = [row.item_name, row.item_price, row.buying_price, row.brand, row.category, row.vendor, row.shop, row.stock_amount, row.out_of_stock, row.item_img, row.product_descriptions, row.upc, row.sku, row.created_at]
        writer.writerow(rowobj)
    return response