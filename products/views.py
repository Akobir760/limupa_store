from django.shortcuts import render

from django.views.generic import ListView, DetailView

from products.models import ProductModel, ProductCategory, ProductBrand, ProductSize, ProductColor, BlogModel


class ProductListView(ListView):
    template_name = 'htmls/shop-4-column.html'
    context_object_name = "products"
    paginate_by = 5

    def get_queryset(self):
        qs = ProductModel.objects.all().order_by('-id')
        q = self.request.GET.get('q')
        cat = self.request.GET.get('cat')
        size = self.request.GET.get('size')
        color = self.request.GET.get('color')
        brand = self.request.GET.get('brand')
        price = self.request.GET.get('price')

        if q:
            qs = qs.filter(title__icontains=q)
        if cat:
            qs = qs.filter(categories=cat)
        if size:
            qs = qs.filter(products_quantity__sizes=size)
        if color:
            qs = qs.filter(products_quantity__colors=color)
        if brand:
            qs = qs.filter(brand=brand)
        if price:
            if price == "price":
                qs = qs.order_by('price')
            elif price == "-price":
                qs = qs.order_by('-price')

        qs = qs.distinct()
        print(qs)
        return qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = ProductCategory.objects.all().order_by('-id')
        context["colors"] = ProductColor.objects.all().order_by('-id')
        context["sizes"] = ProductSize.objects.all().order_by('-id')
        context["brands"] = ProductBrand.objects.all().order_by('-id')
        return context
    
class ProductDetailView(DetailView):
    template_name = 'shop/product.html'
    queryset = ProductModel.objects.all()
    context_object_name = "product"


class BlogListView(ListView):
    model = BlogModel
    template_name = 'htmls/blog.html'
    context_object_name = 'blogs'
    paginate_by = 6 
    ordering = ['-id']  
    
    def get_queryset(self):
        qs = super().get_queryset()
        for blog in qs:
            print(blog.title, blog.short_description)
        return qs


class BlogDetailView(DetailView):
    model = BlogModel
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'




