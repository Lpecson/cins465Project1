from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from tasks.models import JournalEntry
from tasks.forms import JournalEntryForm
from django.contrib.auth.models import User
from django.shortcuts import render

@login_required(login_url='/core/login/')
def TasksMain(request):
    return render(request, 'tasks/home.html')


@login_required(login_url='/core/login/')
def add(request):
	if (request.method == "POST"):
		if ("add" in request.POST):
			add_form = JournalEntryForm(request.POST)
			if (add_form.is_valid()):
				Description = add_form.cleaned_data["Description"]
				Category = add_form.cleaned_data["Category"]
				Completed = add_form.cleaned_data["Completed"]
				JournalEntry(user=request.user, Description=Description, Category=Category, Completed=Completed).save()
				return redirect("/TasksMain/")
			else:
				context = {
                    "form_data": add_form
				}
				return render(request, 'tasks/add.html', context)
		else:
			# Cancel
			return redirect("TasksMain/")
	else:
		context = {
            "form_data": JournalEntryForm()
		}
		return render(request, 'tasks/add.html', context)


@login_required(login_url='/core/login/')
def edit(request, id):
	if (request.method == "GET"):
		# Load Journal Entry Form with current model data.
		journalEntry = JournalEntry.objects.get(id=id)
		form = JournalEntryForm(instance=journalEntry)
		context = {"form_data": form}
		return render(request, 'edit.html', context)
	elif (request.method == "POST"):
		# Process form submission
		if ("edit" in request.POST):
			form = JournalEntryForm(request.POST)
			if (form.is_valid()):
				journalEntry = form.save(commit=False)
				journalEntry.user = request.user
				journalEntry.id = id
				journalEntry.save()
				return redirect("TasksMain/")
			else:
				context = {
                    "form_data": form
				}
				return render(request, 'add.html', context)
		else:
			#Cancel
			return redirect("/TasksMain/")
