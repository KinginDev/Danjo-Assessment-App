from django import template

register = template.Library()

@register.filter
def get_choice_submission(submissions, choice_id):
    return submissions.get(choice_id)


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def get_choice_status(choice_status, choice_id):
    return choice_status[choice_id]