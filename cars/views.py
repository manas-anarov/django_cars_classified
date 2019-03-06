from django.shortcuts import render




from .forms import AddForm



from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, DeleteView
from django.shortcuts import render, redirect

from django.shortcuts import render, get_object_or_404

import datetime
from django.urls import reverse_lazy



from django.core.paginator import Paginator

from django.contrib.auth.forms import UserCreationForm


from django.urls import reverse

from django.http import HttpResponseRedirect







def add(request):

	form = AddForm(request.POST)

	if request.method == 'POST':
		print(form.errors)
		if form.is_valid():
			form.save()
	return render(request, 'add.html', {'form': form})