from django import forms
from models import Book, Dvd


# Book edit Form
class BookEditForm(forms.ModelForm):
    price = forms.DecimalField(
        label="Price",
        prefix="$",
        max_digits=6,
        decimal_places=2
    )

    class Meta:
        model = Book
        exclude = ()
        fields = ['title', 'author', 'publisher', 'copyright_date',
                  'isbn', 'publiction_date', 'series', 'pages', 'description']
        widgets = {}


# DVD edit Form
class DVDEditForm(forms.ModelForm):
    price = forms.DecimalField(
        label="Price",
        prefix="$",
        max_digits=6,
        decimal_places=2
    )

    class Meta:
        model = Dvd
        exclude = ()
        fields = ['title', 'actors', 'run_time', 'raiting',
                  'release_date', 'description']
        widgets = {}
