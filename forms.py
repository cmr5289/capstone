from django import forms
from models import Book, Dvd, PersonEntry


# Book edit Form
class BookEditForm(forms.ModelForm):
    price = forms.DecimalField(
        label="Price $",
        max_digits=6,
        decimal_places=2
    )

    class Meta:
        model = Book
        exclude = ()
        fields = ['title', 'author', 'publisher', 'copyright_date',
                  'isbn', 'publication_date', 'series', 'pages', 'description']
        widgets = {}


# DVD edit Form
class DVDEditForm(forms.ModelForm):
    price = forms.DecimalField(
        label="Price $",
        max_digits=6,
        decimal_places=2
    )

    class Meta:
        model = Dvd
        exclude = ()
        fields = ['title', 'actors', 'run_time', 'raiting',
                  'release_date', 'description']
        widgets = {}


class EmployeeEditForm(forms.ModelForm):
    raw_phone_number = forms.CharField(label="Phone Number", max_length="14")

    class Meta:
        model = PersonEntry
        exclude = ()
        fields = ['name', 'employee_number',
                  'role', 'email', 'department']
        widget = {}
