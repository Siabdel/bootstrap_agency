from django.db import models
# Create your models here.
# portfolio/models.py

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Orderable, Page, Collection
from wagtail.core.fields import RichTextField
from wagtail.core.fields import RichTextField, StreamField
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from streamfieldblocks.models import TimelineBlock, CarouselBlock, ResponsiveImageBlock
from wagtail.core import blocks
from wagtail.embeds  import blocks as embedBlock
from streamfieldblocks.models import ResponsiveImageBlock, CardBlock, SimpleRichTextBlock, CarouselBlock
from blog.blocks import BaseStreamBlock


class StandardPage(Page):
    """
    A generic content page. On this demo site we use it for an about page but
    it could be used for any type of page content that only needs a title,
    image, introduction and body field
    """

    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and 3000px.'
    )
    # body = StreamField( BaseStreamBlock(verbose_name="Page body", blank=True))
    body = StreamField( BaseStreamBlock(), verbose_name="Page body", blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
        StreamFieldPanel('body'),
        ImageChooserPanel('image'),
    ]

