from django.shortcuts import render
from .forms import AddForm
from django.shortcuts import render



from cars.models import Brand



def add(request):

	form = AddForm(request.POST)
	brand_car = Brand.objects.all()
	if request.user.has_perm("account.can_add"):
		if request.method == 'POST':
			print(form.errors)
			if form.is_valid():
				form.save()
		return render(request, 'add.html', {'form': form, 'brand_car': brand_car})