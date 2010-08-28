from django import forms
from django.forms.fields import DEFAULT_DATE_INPUT_FORMATS
import datetime

DEFAULT_DATE_OUTPUT_FORMATS = DEFAULT_DATE_INPUT_FORMATS[0]

## Sibio form fields

# @start: DateField. Built in order to render output format based on input format
class FormattedTextInput(forms.widgets.TextInput):
    "Overrides TextInput to render formatted value."
    def render(self, name, value, attrs=None):
        formatted_value = None
        if value:
            formatted_value = self.format_value(value)
        return super(FormattedTextInput, self).render(name, formatted_value, attrs)

class DateFormattedTextInput(FormattedTextInput):
    "Renders formatted date."
    def __init__(self, format=None, attrs=None):
        super(DateFormattedTextInput, self).__init__(attrs)
        self.format = format or DEFAULT_DATE_OUTPUT_FORMATS

    def format_value(self, value):
        if isinstance(value, datetime.date) or isinstance(value, datetime.datetime):
            return value.strftime(self.format)
        else:
            return value

class DateField(forms.DateField):
    widget = DateFormattedTextInput

    def __init__(self, attrs=None,  *args, **kwargs):
        super(DateField, self).__init__(*args, **kwargs)
        self.widget.format = self.input_formats[0]
        self.widget.attrs.update({'class':'date-field'})
        if attrs:
            self.widget.attrs.update(attrs)
# @end: DateField