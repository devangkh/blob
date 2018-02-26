from django import forms

class BlobTextForm(forms.Form):
	blobtext = forms.CharField()
	
class DualTextForm(forms.Form):
	base = forms.CharField()
	ref = forms.CharField()