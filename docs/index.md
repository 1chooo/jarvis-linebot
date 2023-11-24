# 1chooo's Jarvis

### Image Carousel
```py
TemplateSendMessage(
    alt_text='ImageCarousel template',
    template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url='https://hackmd.io/_uploads/BkwF_MI23.jpg',
                action=MessageAction(
                    label='Add a goal',
                    text='I want to add sth...'
                )
            ),
        ]
    )
),
```

### ImageSendMessage
```py
ImageSendMessage(
    original_content_url = "https://2023-amazon-ambassador.s3.amazonaws.com/hugo_grad.png",
    preview_image_url = "https://2023-amazon-ambassador.s3.amazonaws.com/hugo_grad.png",
),
```