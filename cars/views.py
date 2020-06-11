from django.shortcuts import render
from .forms import AddForm
from .forms import ListForm
from django.shortcuts import render

from cars.models import Brand
from cars.models import Car
from django.core.paginator import Paginator

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import login_required

from django.views import generic


from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.urls import reverse

from django.contrib.messages.views import SuccessMessageMixin



def add(request):
	form = AddForm(request.POST)
	brand_car = Brand.objects.all()
	if request.user.has_perm("account.can_add"):
		if request.method == 'POST':
			print(form.errors)
			if form.is_valid():
				form.save()
		return render(request, 'add.html', {'form': form, 'brand_car': brand_car})


def all_posts1(request):

	form = ListForm(request.POST)
	posts = Car.objects.all().order_by('-id')
	brand_search = Brand.objects.all()


	if request.method == 'POST':
		brand = request.POST.get('brand_id_f')
		posts = Car.objects.filter(brand=brand).order_by('-id')
	
	paginator = Paginator(posts, 10)
	page = request.GET.get('page')
    
	posts = paginator.get_page(page)



	context_posts = {
		'posts': posts,
		'brand_search': brand_search,
	}

	return render(request, 'all_posts.html', context_posts)


def all_posts(request):
	posts = Car.objects.all().order_by('-id')
	
	paginator = Paginator(posts, 10)
	page = request.GET.get('page')
	posts = paginator.get_page(page)

	context_posts = {
		'posts': posts,
	}

	return render(request, 'all_posts.html', context_posts)







# https://stackoverflow.com/questions/5907575/how-do-i-use-pagination-with-django-class-based-generic-listviews

class CarListView(generic.ListView):
	model = Car
	template_name = "all_posts.html"
	paginate_by = 4


	def get_context_data(self, **kwargs):
		context = super(CarListView, self).get_context_data(**kwargs) 
		car_posts = Car.objects.all()

		paginator = Paginator(car_posts, self.paginate_by)
		page = self.request.GET.get('page')
		posts = paginator.get_page(page)

		context['posts'] = posts
		return context




class CarDetailView(generic.DetailView):
	model = Car
	template_name = "post.html"
	queryset = Car.objects.all()
	context_object_name = 'post'






# class ComplicatedCreate(SuccessMessageMixin, CreateView):
#     model = ComplicatedModel
#     success_url = '/success/'
#     success_message = "%(calculated_field)s was created successfully"


class CarCreateView(SuccessMessageMixin, generic.CreateView):
	model = Car
	template_name = "add.html"
	paginate_by = 4
	form_class = AddForm
	brand_car = Brand.objects.all()
	success_message = "Post was created successfully"
	def get_success_url(self):
		return reverse('car:add')

def show_post(request, pk):
	post = get_object_or_404(Car,pk=pk)
	brand = Brand.objects.get(id=post.brand)
	return render(request, 'post.html', {'post':post, 'brand':brand})

@login_required
def show_post2(request, pk):
	post = get_object_or_404(Car,pk=pk)
	

	item = Car.objects.get(pk=pk)
	if request.user == item.profile:
		Car.objects.filter(id=pk).delete()
		return HttpResponse("asdasd")




def list_category(request, pk:None):

	form = ListForm(request.POST)
	posts = Car.objects.filter(brand=pk).order_by('-id')
	brand_search = Brand.objects.all()


	if request.method == 'POST':
		brand = request.POST.get('brand_id_f')
		posts = Car.objects.filter(brand=brand).order_by('-id')
	
	paginator = Paginator(posts, 10)
	page = request.GET.get('page')
    
	posts = paginator.get_page(page)



	context_posts = {
		'posts': posts,
		'brand_search': brand_search,
	}

	return render(request, 'all_posts.html', context_posts)

