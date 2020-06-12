{"filter":false,"title":"views.py","tooltip":"/products/views.py","undoManager":{"mark":3,"position":3,"stack":[[{"start":{"row":6,"column":0},"end":{"row":16,"column":0},"action":"remove","lines":["def all_products(request):","    \"\"\" A view to show all products, including sorting and search queries \"\"\"","","    products = Product.objects.all()","","    context = {","        'products': products,","    }","","    return render(request, 'products/products.html', context)",""],"id":60},{"start":{"row":6,"column":0},"end":{"row":29,"column":0},"action":"insert","lines":["def all_products(request):","    \"\"\" A view to show all products, including sorting and search queries \"\"\"","","    products = Product.objects.all()","    query = None","","    if request.GET:","        if 'q' in request.GET:","            query = request.GET['q']","            if not query:","                messages.error(request, \"You didn't enter any search criteria!\")","                return redirect(reverse('products'))","            ","            queries = Q(name__icontains=query) | Q(description__icontains=query)","            products = products.filter(queries)","","    context = {","        'products': products,","        'search_term': query,","    }","","    return render(request, 'products/products.html', context)","",""]}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":61}],[{"start":{"row":0,"column":0},"end":{"row":2,"column":0},"action":"remove","lines":["from django.shortcuts import render, get_object_or_404","from .models import Product",""],"id":62},{"start":{"row":0,"column":0},"end":{"row":3,"column":27},"action":"insert","lines":["from django.shortcuts import render, redirect, reverse, get_object_or_404","from django.contrib import messages","from django.db.models import Q","from .models import Product"]}],[{"start":{"row":0,"column":0},"end":{"row":27,"column":61},"action":"remove","lines":["from django.shortcuts import render, redirect, reverse, get_object_or_404","from django.contrib import messages","from django.db.models import Q","from .models import Product","# Create your views here.","","def all_products(request):","    \"\"\" A view to show all products, including sorting and search queries \"\"\"","","    products = Product.objects.all()","    query = None","","    if request.GET:","        if 'q' in request.GET:","            query = request.GET['q']","            if not query:","                messages.error(request, \"You didn't enter any search criteria!\")","                return redirect(reverse('products'))","            ","            queries = Q(name__icontains=query) | Q(description__icontains=query)","            products = products.filter(queries)","","    context = {","        'products': products,","        'search_term': query,","    }","","    return render(request, 'products/products.html', context)"],"id":63},{"start":{"row":0,"column":0},"end":{"row":36,"column":0},"action":"insert","lines":["from django.shortcuts import render, redirect, reverse, get_object_or_404","from django.contrib import messages","from django.db.models import Q","from .models import Product, Category","","# Create your views here.","","def all_products(request):","    \"\"\" A view to show all products, including sorting and search queries \"\"\"","","    products = Product.objects.all()","    query = None","    categories = None","","    if request.GET:","        if 'category' in request.GET:","            categories = request.GET['category'].split(',')","            products = products.filter(category__name__in=categories)","            categories = Category.objects.filter(name__in=categories)","","        if 'q' in request.GET:","            query = request.GET['q']","            if not query:","                messages.error(request, \"You didn't enter any search criteria!\")","                return redirect(reverse('products'))","            ","            queries = Q(name__icontains=query) | Q(description__icontains=query)","            products = products.filter(queries)","","    context = {","        'products': products,","        'search_term': query,","        'current_categories': categories,","    }","","    return render(request, 'products/products.html', context)",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":5,"column":23},"end":{"row":5,"column":23},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1591984163804,"hash":"448c8586a78d4e38df9e7dc0678212de1972bdd1"}