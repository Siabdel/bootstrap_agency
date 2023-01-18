from django.db import models
from django import forms
from django.db.models.deletion import SET_NULL
from modelcluster.models import ClusterableModel
from django_extensions.db.fields import AutoSlugField


from wagtail.core.models import Orderable, Page, Collection
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import  BaseChooserPanel, FieldPanel, InlinePanel, MultiFieldPanel, RichTextField, RichTextFieldPanel
from wagtail.admin.edit_handlers import  PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.core.fields import RichTextField, StreamField
from modelcluster.models import  ClusterableModel
from modelcluster.fields import ParentalKey, ParentalManyToManyField

from wagtail.snippets.models import register_snippet
from streamfieldblocks.models import (
    ServiceBlock,
    ResponsiveImageBlock,
    SimpleRichTextBlock,) 

 
class HomePage(Page):
    
    """ Page home Model """
    template_name = "/templates/home/home_page.html"
    max_count = 1
    
    banner_title = models.CharField(max_length=100, blank=True, null=True)
    banner_subtitle = RichTextField()
    banner_body = RichTextField(null=True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False, null=True,
        on_delete=models.SET_NULL,
        related_name = "+",
        )
    banner_cta = models.ForeignKey("wagtailcore.Page",
        blank=True, null=True,
        on_delete=models.SET_NULL,related_name="+")


    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        FieldPanel('banner_body', classname="full"),
        ImageChooserPanel("banner_image"),
        PageChooserPanel("banner_cta"),
    ]
    class Meta :
        verbose_name="Home page Atlas RDV"
        verbose_name_plural = "Accueil Page AtlasRDV" 

    
@register_snippet
class CategorieService(models.Model):
    """
    A Django model to define the Service Catégorie of service web
    """
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', editable=True, 
                         help_text="Unique identifier" )
                         
    image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False, null=True,
        on_delete=models.SET_NULL,
        related_name = "+",
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
        ImageChooserPanel('image')
    ]

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = "Categorie de Service"
        verbose_name_plural = "Categorieis de Service"


class ServicePage(Page):
    """ Deatil for a Services web """
     
    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)
    
    body = RichTextField(blank=True)
    categorie_service = ParentalManyToManyField(CategorieService, blank=True)

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and '
        '3000px.'
    )
    
    icon_slug = models.ForeignKey("ExtraText", 
                                  on_delete=models.SET_NULL,
                                  related_name="mes_service", 
                                  null=True, blank=False)

   
    @property
    def thumb_image(self):
        # Returns an empty string if there is no profile pic or the rendition
        # file can't be found.
        try:
            return self.image.get_rendition('fill-50x50').img_tag()
        except:  # noqa: E722 FIXME: remove bare 'except:'
            return ''
    
    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
        ImageChooserPanel('image'),
        FieldPanel('categorie_service', widget=forms.CheckboxSelectMultiple),
        BaseChooserPanel('icon_slug'),
        FieldPanel('body')
    ]
    
    def __str__(self):
        return self.title
    
    # Can only be placed under a ServicesIndexPage object
    parent_page_types = ['ServicesIndexPage']

    class Meta:
        verbose_name_plural = "Service Page Web"

class ServicesIndexPage(Page):
    """
    A Page model that creates an index page (a listview)
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

    # Only ServicePage objects can be added underneath this index page
    subpage_types = ['ServicePage']

    # Allows children of this indexpage to be accessible via the indexpage
    # object on templates. We use this on the homepage to show featured
    # sections of the site and their child pages
    def children(self):
        return self.get_children().specific().live()

    # Overrides the context to list all child
    # items, that are live, by the date that they were published
    # http://docs.wagtail.io/en/latest/getting_started/tutorial.html#overriding-context
    def get_context(self, request):
        context = super(ServicesIndexPage, self).get_context(request)
        context['Services'] = ServicePage.objects.live().order_by('title')
        return context

    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
        ImageChooserPanel('image'),
    ]


@register_snippet
class FooterText(models.Model):
    """
    This provides editable text for the site footer. Again it uses the decorator
    `register_snippet` to allow it to be accessible via the admin. It is made
    accessible on the template via a template tag defined in base/templatetags/
    navigation_tags.py
    """
    body = RichTextField()

    panels = [
        FieldPanel('body'),
    ]

    def __str__(self):
        return "Footer text"

    class Meta:
        verbose_name_plural = 'Footer Text'


@register_snippet
class ExtraText(models.Model):
    """
    Element html qui va s'inserer dans un bloc.
    accessible on the template via a template tag defined in home/templatetags/
    navigation_tags.py
    """
    name = models.CharField(max_length=255)
    slug = AutoSlugField(
            populate_from='name', 
            editable=True, 
            help_text="Unique identifier")
    body =  models.TextField()

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
        FieldPanel('body'), ]

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name_plural = 'Extra Text'


class GalleryPage(Page):
    """
    This is a page to list locations from the selected Collection. We use a Q
    object to list any Collection created (/admin/collections/) even if they
    contain no items. In this demo we use it for a GalleryPage,
    and is intended to show the extensibility of this aspect of Wagtail
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
        help_text='Landscape mode only; horizontal width between 1000px and '
        '3000px.'
    )
    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])
    
    collection = models.ForeignKey(
        Collection,
        limit_choices_to=~models.Q(name__in=['Root']),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text='Select the image collection for this gallery.'
    )

    content_panels = Page.content_panels + [
        #FieldPanel('title', classname="full"),
        StreamFieldPanel('body'),
        ImageChooserPanel('image'),
        FieldPanel('collection'),
    ]

    # Defining what content type can sit under the parent. Since it's a blank
    # array no subpage can be added
    subpage_types = []



class ServiceStreamFieldPage(Page):
    """ Detail for a Services web """
    """ A Page model that creates an index page (a listview)
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
    
    content = StreamField([
        ('richtext', SimpleRichTextBlock()),
        ('responsive_image', ResponsiveImageBlock()),
        ('service', ServiceBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
        ImageChooserPanel('image'),
        StreamFieldPanel('content'),
    ]
 