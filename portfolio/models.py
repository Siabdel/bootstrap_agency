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
from streamfieldblocks.models import TimelineBlock, CarouselBlock, ResponsiveImageBlock, CardBlock
#from commonblocks.blocks import SimpleRichTextBlock
from wagtail.core import blocks
from wagtail.embeds  import blocks as embedBlock



class PortfolioPage(Page):
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
        blank=True, help_text='Blog listing page header text.'
    )
    
    experience = StreamField([
        ("Timeline_Block", TimelineBlock()),
    ], null=True, blank=True)

    content_panels=Page.content_panels + [
            ImageChooserPanel("background_image"),
            FieldPanel("headline_text"),
            StreamFieldPanel('experience'),
        ]
 
 

class ProjectPage(Page):
    intro = models.TextField()
    image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        help_text='Project Image',
        on_delete=models.SET_NULL,
    )
 
    content = StreamField([
        ('richtext', blocks.RichTextBlock()),
        ('carousel', CarouselBlock()),
        #('flush_list', FlushListBlock()),
        ('responsive_image', ResponsiveImageBlock()),
        ('card', CardBlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel("image"),
        FieldPanel("intro"), 
        StreamFieldPanel("content"),
    ]
