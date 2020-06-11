from django.shortcuts import render, redirect

from django.urls import reverse
from .forms import ListForm
from .forms import UpdateForm


from cars.models import Brand
from cars.models import Car
from django.core.paginator import Paginator

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import login_required

from django.views import generic






class ProfileListView(generic.ListView):
	model = Car
	template_name = "myprofile/list_author.html"
	paginate_by = 4


	def get_context_data(self, **kwargs):
		context = super(ProfileListView, self).get_context_data(**kwargs) 
		car_posts = Car.objects.filter(profile=self.request.user).order_by('-id')

		paginator = Paginator(car_posts, self.paginate_by)
		page = self.request.GET.get('page')
		posts = paginator.get_page(page)

		context['posts'] = posts
		return context



class ProfileUpdateView(generic.UpdateView):
	model = Car
	template_name = "myprofile/update.html"
	paginate_by = 10
	form_class = UpdateForm
	brand_car = Brand.objects.all()
	success_message = "Post was created successfully"
	def get_success_url(self):
		return reverse('profiles:list')


class ProfileDeleteView(generic.DeleteView):
	model = Car
	template_name = "myprofile/delete.html"
	paginate_by = 10
	form_class = UpdateForm
	brand_car = Brand.objects.all()
	success_message = "Post was created successfully"
	def get_success_url(self):
		return reverse('profiles:list')




def list_author(request):
	user = request.user
	form = ListForm(request.POST)
	posts = Car.objects.filter(profile=user).order_by('-id')
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

	return render(request, 'myprofile/list_author.html', context_posts)

	


def delete_post(request, pk):
	post = get_object_or_404(Car,pk=pk)
	if request.method == 'POST':
		post.delete()
		return redirect('profiles:list')
	context = {
		"object": post
	}
	return render(request, 'myprofile/delete.html', context)


def update_post(request, pk):
	question = Car.objects.get(pk=pk)

	form = UpdateForm(request.POST, instance=question)
	brand_car = Brand.objects.all()
	if request.user.has_perm("account.can_add"):
		if request.method == 'POST':
			print(form.errors)
			if form.is_valid():
				form.save()
		return render(request, 'myprofile/update.html', {'form': form, 'brand_car': brand_car, 'question': question})