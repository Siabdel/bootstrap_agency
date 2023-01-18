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


class BlogListingPage(Page):
    background_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        help_text='Header background image',
        on_delete=models.SET_NULL,
    )

    headline_text = models.CharField(
        max_length=70,
        blank=True, 
        help_text='Blog listing page header text.'
    )
    # INSIDE THE BLOG LISTING CLASS
    content_panels = Page.content_panels + [
        ImageChooserPanel("background_image"), 
        FieldPanel("headline_text"),
    ]
    
# Create your models here.content

class BlogPage(Page):
    created = models.DateField("Article Date")
    intro = models.TextField("Introduction")
    content = StreamField([
        ('richtext', SimpleRichTextBlock()),
        ('carousel', CarouselBlock()),
        ('responsive_image', ResponsiveImageBlock()),
        ('card', CardBlock()),
    ], blank=True)
    featured = models.BooleanField(default=False)
    content_panels = Page.content_panels + [
        FieldPanel('created'),
        FieldPanel('featured'),
        FieldPanel('intro'),
        StreamFieldPanel('content'),

    ]
