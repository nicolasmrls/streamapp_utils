"""Card viasulization for streamlit.

This class creates an animated card to show content in your
streamlit app wiht a linked url to redirect to other url in
a new tab.
"""
import streamlit.components.v1 as components


class Card:
    """
    This class creates an animated card to show content in your
    streamlit app wiht a linked url to redirect to other url in
    a new tab.
    """
    html = """
        <div style="height: {height}px; width: {width}px; margin: 0; \
            border-radius: 30px; position: realtive;
            text-align: center; background-color: black">
        <a style="text-decoration: none;" href="{url}" target="_blank">
        <img src="{img}"
            style="height: 100%; width: 100%; border-radius: 30px; \
                transition: .5s; opacity: 0.3;">
        <div style="position: absolute; top: 50%; left: 50%; transform: \
            translate(-50%, -50%);">
            <h1 style="color: white; font-size: 2.5rem; font-family: \
                sans-serif">{title}</h1>
            <p style="color: white; font-size: 1.2rem; font-family: \
                sans-serif; font-weight:bold;">{description}</p>
        </div>
        </a>
        </div>
    """

    @classmethod
    def add_card(cls, url: str, title: str, img: str, description: str = '',
                 width: int = 400, height: int = 400) -> None:
        """Show a rendered html card in frontend.

        Args:
            url: str url to redirect to other web in a new tab.
            title str title to show in the card.
            img: str url to the image to use in the card.
            description: optional description to explain something in the card.
            width: int card`s width.
            heigth: int card`s heigth.

        Return:
            None
        """
        components.html(
            Card.html.format(
                url=url,
                title=title,
                img=img,
                description=description,
                width=width*.97,
                height=height*.97
            ),
            width=width,
            height=height
        )
        return
