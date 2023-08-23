from django import template

register = template.Library()

@register.filter()
def censor(value):
    bad_words = ['сука', 'клоун']
    for word in bad_words:
        value = value.replace(word, '*' * len(word))
    return value

#в news/4 используется censor


