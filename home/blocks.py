from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.core.blocks import (
    CharBlock, ChoiceBlock, RichTextBlock, StreamBlock, StructBlock, TextBlock,
)

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TitleAndTextBlock(blocks.StructBlock):
    """Title and text and nothing else."""
    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=True, help_text="Add additional text")

    class Meta:  # noqa
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"

class ImageBlock(StructBlock):
    """
    Custom `StructBlock` for utilizing images with associated caption and
    attribution data
    """
    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)

    class Meta:
        icon = 'image'
        template = "blocks/image_block.html"


class CardBlock(blocks.StructBlock):
    """ Card with image and text and button """
    title = blocks.CharBlock(required=True, help_text="Add your text")
    card = blocks.ListBlock(
        blocks.StructBlock([
            ("image", ImageChooserBlock(required=True)), 
            ( "title", blocks.CharBlock(required=True, max_length=40)),
            ( "text", blocks.CharBlock(required=True, max_length=200)),
            ( "boutton_page", blocks.PageChooseBlock(required=True)),
            ( "boutton_url", blocks.URLBlock(required=True, help_text=""))
        ])
    )
    class Meta:  # noqa
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "Staff Cards"