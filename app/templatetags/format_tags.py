from django import template


register = template.Library()


@register.filter(name='format_tags')
def format_tags(tags_string):
    tags_list = tags_string.split(',')
    formatted_tags = ','.join([f'#{tag.strip()}' for tag in tags_list])
    return formatted_tags.split(',')