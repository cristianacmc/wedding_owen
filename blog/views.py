from django.shortcuts import render
from .forms import ContactForm

def index(request):
  return render(request, 'index.html')

def contact(request):
	template = "index.html"

	if request.method == 'POST':
		form = 	ContactForm(request.POST)

		if form.is_valid():
			form.save()
	else:
		form = ContactForm()

	context = {
		'form': form,
	}
	return render(request, index.html, context)

