from home.models import FooterText, ExtraText
from wagtail.core.models import Page, Site
from django import template
from home.models import ExtraText


register = template.Library()
# https://docs.djangoproject.com/en/1.9/howto/custom-template-tags/


@register.inclusion_tag('includes/extra_text.html', takes_context=True)
def get_extra_text(context, icon_name='icon-fa-laptop'):
    Extra_text = "Icon Vide"
    try:
        Extra_text = ExtraText.objects.get(slug=icon_name).body
    except Exception :
        return Extra_text

    return {
        'Extra_text': Extra_text,
    }
