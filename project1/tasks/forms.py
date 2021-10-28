from django import forms
from tasks.models import JournalEntry
cat = ['Home', 'School', 'Work', 'Self Improvement', 'Other']
class JournalEntryForm(forms.ModelForm):
	Description = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}));
	Category=forms.CharField(widget=forms.Select(choices=cat))

	class Meta():
		model = JournalEntry
		fields = ['Description', 'Category', 'Completed']
