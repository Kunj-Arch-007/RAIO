from django import template

register = template.Library()

@register.filter(name='addclass')
def addclass(value, arg):
    if hasattr(value, 'as_widget'):
        return value.as_widget(attrs={'class': arg})
    return value
