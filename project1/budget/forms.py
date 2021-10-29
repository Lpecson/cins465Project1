from django import forms
from tasks.models import JournalEntry
cat = [('Food', 'food'), ('Clothing', 'clothing'), ('Housing', 'housing'), ('Education', 'education'),('Entertainment', 'entertainment') ('Other', 'other')]
class BudgetItemForm(forms.ModelForm):
	Description = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}));
	Category = forms.CharField(widget=forms.Select(choices=cat))
    Projected = forms.CharField(min_length = 1, max_length = 1000)
    Actual = forms.CharField(min_length = 1, max_length = 1000)

	class Meta():
		model = JournalEntry
		fields = ['Description', 'Category', 'Completed']
