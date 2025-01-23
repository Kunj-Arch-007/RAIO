from django import template

register = template.Library()

@register.filter(name='addclass')
def addclass(field, args):
    """Add multiple attributes (like class and id) to a Django form field in templates."""
    attrs = {}
    for arg in args.split(','):
        key, value = arg.split('=')
        attrs[key.strip()] = value.strip()
    return field.as_widget(attrs=attrs)
