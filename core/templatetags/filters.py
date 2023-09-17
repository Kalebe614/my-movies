from django import template
register = template.Library()

@register.filter
def get_year(data):
  
    try:
        year= data.split('-')[0]
        return year
    
    except ValueError:
        print(f'Was not possible to parse year, error:{ValueError}')
        return data