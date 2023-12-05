# -*- coding: utf-8 -*-
"""
Date: 2023/11/20
Author: @1chooo(Hugo ChunHo Lin)
E-mail: hugo970217@gmail.com
Version: v0.1.0
"""

import os
import json
import datetime as dt
# import boto3
from linebot import LineBotApi
from linebot import WebhookHandler
from linebot.models import MessageEvent
from linebot.models import TextMessage
from linebot.models import ImageMessage
from linebot.models import VideoMessage
from linebot.models import AudioMessage
from linebot.models import FileMessage
from linebot.models import StickerMessage
from linebot.models import LocationMessage
from linebot.models import TextSendMessage
from linebot.models import ImageSendMessage
from linebot.models import VideoSendMessage
from linebot.models import TemplateSendMessage
from linebot.models import ImageCarouselTemplate
from linebot.models import ImageCarouselColumn
from linebot.models import MessageAction
from linebot.exceptions import InvalidSignatureError

line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])

def handle_todo_goal(event):

    ready_to_add_todo = False
    todos = []

    event_text = event.message.text

    if event_text == "Got things to do, busy! 🥴":

        reply_messages = [
            TextSendMessage(
                text="Please choose the type of your goal"
            ),
            TemplateSendMessage(
                alt_text='ImageCarousel template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/BkwF_MI23.jpg',
                            action=MessageAction(
                                label='Add a TODO',
                                text='I want to add sth...'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/BkwF_MI23.jpg',
                            action=MessageAction(
                                label='Add a Diary',
                                text='I just want to say something... ✍🏼'
                            )
                        ),
                    ]
                )
            ),
        ]
        
        line_bot_api.reply_message(
            event.reply_token,
            reply_messages
        )
    else:
        return
    
def lambda_handler(event, context):
    # boto3.resource("dynamodb")

    @handler.add(MessageEvent, message=TextMessage)
    def handle_text_message(event):

        event_text = event.message.text

        handle_todo_goal(event)
        if event_text == "I want to see how busy you really are 👨🏻‍💻":
            reply_messages = [
                TextSendMessage(
                    text=f'Hi, I want to see how busy you really are 👨🏻‍💻'
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "I want you to know how extravagant I can be 🤑":
            reply_messages = [
                TextSendMessage(
                    text=f'Hi, I want you to know how extravagant I can be 🤑'
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "How rich am I, Huh? 💳":
            reply_messages = [
                TextSendMessage(
                    text=f'Here is your bank account 💳'
                ),
                TemplateSendMessage(
                    alt_text='ImageCarousel template',
                    template=ImageCarouselTemplate(
                        columns=[
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/04_savings/fuban_bank.png',
                                action=MessageAction(
                                    label='Fuban Bank',
                                    text='I want to check my Fuban Bank account 💳'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/04_savings/fuban_credit.png',
                                action=MessageAction(
                                    label='Fuban Credit',
                                    text='I want to check my Fuban Credit Card account 💳'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/04_savings/next_bank.png',
                                action=MessageAction(
                                    label='Next Bank',
                                    text='I want to check my Next Bank account 💳'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/04_savings/line_bank.png',
                                action=MessageAction(
                                    label='Line Bank',
                                    text='I want to check my Line Bank account 💳'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/04_savings/post_office.png',
                                action=MessageAction(
                                    label='Post Office',
                                    text='I want to check my Post Office account 💳'
                                )
                            ),
                        ]
                    )
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == 'I want to check my Fuban Bank account 💳':
            reply_messages = [
                TextSendMessage(
                    text=f'Your Fuban Bank account 💳'
                ),
                TextSendMessage(
                    text=f'012'
                ),
                TextSendMessage(
                    text=f'81680007844308'
                ),
                TemplateSendMessage(
                    alt_text='ImageCarousel template',
                    template=ImageCarouselTemplate(
                        columns=[
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/04_savings/fuban_credit.png',
                                action=MessageAction(
                                    label='Fuban Credit',
                                    text='I want to check my Fuban Credit Card account 💳'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/04_savings/next_bank.png',
                                action=MessageAction(
                                    label='Next Bank',
                                    text='I want to check my Next Bank account 💳'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/04_savings/line_bank.png',
                                action=MessageAction(
                                    label='Line Bank',
                                    text='I want to check my Line Bank account 💳'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/04_savings/post_office.png',
                                action=MessageAction(
                                    label='Post Office',
                                    text='I want to check my Post Office account 💳'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/04_savings/fuban_bank.png',
                                action=MessageAction(
                                    label='Fuban Bank',
                                    text='I want to check my Fuban Bank account 💳'
                                )
                            ),
                        ]
                    )
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == 'I want to check my Fuban Credit Card account 💳':
            reply_messages = [
                TextSendMessage(
                    text=f'Your Fuban Credit Card account 💳'
                ),
                TextSendMessage(
                    text=f'012'
                ),
                TextSendMessage(
                    text=f'66306131441395'
                ),
                TemplateSendMessage(
                    alt_text='ImageCarousel template',
                    template=ImageCarouselTemplate(
                        columns=[
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/04_savings/next_bank.png',
                                action=MessageAction(
                                    label='Next Bank',
                                    text='I want to check my Next Bank account 💳'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/04_savings/line_bank.png',
                                action=MessageAction(
                                    label='Line Bank',
                                    text='I want to check my Line Bank account 💳'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/04_savings/post_office.png',
                                action=MessageAction(
                                    label='Post Office',
                                    text='I want to check my Post Office account 💳'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/04_savings/fuban_bank.png',
                                action=MessageAction(
                                    label='Fuban Bank',
                                    text='I want to check my Fuban Bank account 💳'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/04_savings/fuban_credit.png',
                                action=MessageAction(
                                    label='Fuban Credit',
                                    text='I want to check my Fuban Credit Card account 💳'
                                )
                            ),
                        ]
                    )
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == 'I want to check my Next Bank account 💳':
            reply_messages = [
                TextSendMessage(
                    text=f'Your Next Bank account 💳'
                ),
                TextSendMessage(
                    text=f'823'
                ),
                TextSendMessage(
                    text=f'88660000039748'
                ),
                TemplateSendMessage(
                    alt_text='ImageCarousel template',
                    template=ImageCarouselTemplate(
                        columns=[
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/04_savings/line_bank.png',
                                action=MessageAction(
                                    label='Line Bank',
                                    text='I want to check my Line Bank account 💳'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/04_savings/post_office.png',
                                action=MessageAction(
                                    label='Post Office',
                                    text='I want to check my Post Office account 💳'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/04_savings/fuban_bank.png',
                                action=MessageAction(
                                    label='Fuban Bank',
                                    text='I want to check my Fuban Bank account 💳'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/04_savings/fuban_credit.png',
                                action=MessageAction(
                                    label='Fuban Credit',
                                    text='I want to check my Fuban Credit Card account 💳'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/04_savings/next_bank.png',
                                action=MessageAction(
                                    label='Next Bank',
                                    text='I want to check my Next Bank account 💳'
                                )
                            ),
                        ]
                    )
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == 'I want to check my Line Bank account 💳':
            reply_messages = [
                TextSendMessage(
                    text=f'Your Line Bank account 💳'
                ),
                TextSendMessage(
                    text=f'824'
                ),
                TextSendMessage(
                    text=f'111015850968'
                ),
                TemplateSendMessage(
                    alt_text='ImageCarousel template',
                    template=ImageCarouselTemplate(
                        columns=[
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/04_savings/post_office.png',
                                action=MessageAction(
                                    label='Post Office',
                                    text='I want to check my Post Office account 💳'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/04_savings/fuban_bank.png',
                                action=MessageAction(
                                    label='Fuban Bank',
                                    text='I want to check my Fuban Bank account 💳'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/04_savings/fuban_credit.png',
                                action=MessageAction(
                                    label='Fuban Credit',
                                    text='I want to check my Fuban Credit Card account 💳'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/04_savings/next_bank.png',
                                action=MessageAction(
                                    label='Next Bank',
                                    text='I want to check my Next Bank account 💳'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/04_savings/line_bank.png',
                                action=MessageAction(
                                    label='Line Bank',
                                    text='I want to check my Line Bank account 💳'
                                )
                            ),
                        ]
                    )
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == 'I want to check my Post Office account 💳':
            reply_messages = [
                TextSendMessage(
                    text=f'Your Post Office account 💳'
                ),
                TextSendMessage(
                    text=f'700'
                ),
                TextSendMessage(
                    text=f'00019900525908'
                ),
                TemplateSendMessage(
                    alt_text='ImageCarousel template',
                    template=ImageCarouselTemplate(
                        columns=[
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/04_savings/fuban_bank.png',
                                action=MessageAction(
                                    label='Fuban Bank',
                                    text='I want to check my Fuban Bank account 💳'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/04_savings/fuban_credit.png',
                                action=MessageAction(
                                    label='Fuban Credit',
                                    text='I want to check my Fuban Credit Card account 💳'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/04_savings/next_bank.png',
                                action=MessageAction(
                                    label='Next Bank',
                                    text='I want to check my Next Bank account 💳'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/04_savings/line_bank.png',
                                action=MessageAction(
                                    label='Line Bank',
                                    text='I want to check my Line Bank account 💳'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/04_savings/post_office.png',
                                action=MessageAction(
                                    label='Post Office',
                                    text='I want to check my Post Office account 💳'
                                )
                            ),
                        ]
                    )
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "You know how much weight I pushed today? 😮‍💨":
            reply_messages = [
                TextSendMessage(
                    text=f'You know how much weight I pushed today? 😮‍💨'
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "I want to check 1chooo Diary ✍🏼":
            reply_messages = [
                TextSendMessage(
                    text=f'Please select the type of 1chooo\'s life'
                ),
                TemplateSendMessage(
                    alt_text='ImageCarousel template',
                    template=ImageCarouselTemplate(
                        columns=[
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/06_diary/test2.png',
                                action=MessageAction(
                                    label='Reading List',
                                    text='I want to check my reading list 📚'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/06_diary/test2.png',
                                action=MessageAction(
                                    label='Reading List',
                                    text='I want to check my reading list 📚'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/06_diary/test2.png',
                                action=MessageAction(
                                    label='Reading List',
                                    text='I want to check my reading list 📚'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/06_diary/test2.png',
                                action=MessageAction(
                                    label='Reading List',
                                    text='I want to check my reading list 📚'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/06_diary/test2.png',
                                action=MessageAction(
                                    label='Reading List',
                                    text='I want to check my reading list 📚'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/06_diary/test2.png',
                                action=MessageAction(
                                    label='Reading List',
                                    text='I want to check my reading list 📚'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/06_diary/test2.png',
                                action=MessageAction(
                                    label='Reading List',
                                    text='I want to check my reading list 📚'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/06_diary/test2.png',
                                action=MessageAction(
                                    label='Reading List',
                                    text='I want to check my reading list 📚'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/06_diary/test2.png',
                                action=MessageAction(
                                    label='Reading List',
                                    text='I want to check my reading list 📚'
                                )
                            ),
                            ImageCarouselColumn(
                                image_url='https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/06_diary/test2.png',
                                action=MessageAction(
                                    label='Reading List',
                                    text='I want to check my reading list 📚'
                                )
                            ),
                        ]
                    )
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "我想看帥哥":
            reply_messages = [
                TextSendMessage(
                    text=f'Test get image from s3 public bucket'
                ),
                TextSendMessage(
                    text=f'This is Hugo!'
                ),
                ImageSendMessage(
                    original_content_url = "https://2023-amazon-ambassador.s3.amazonaws.com/hugo_grad.png",
                    preview_image_url = "https://2023-amazon-ambassador.s3.amazonaws.com/hugo_grad.png",
                ),
                ImageSendMessage(
                    original_content_url = "https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/06_diary/test2.png",
                    preview_image_url = "https://1chooo-jarvis.s3.ap-northeast-3.amazonaws.com/06_diary/test2.png",
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "Image":
            reply_messages = [
                TextSendMessage(
                    text=f'Test get image from s3 public bucket'
                ),
                TextSendMessage(
                    text=f'This is Hugo!'
                ),
                ImageSendMessage(
                    original_content_url = "https://2023-amazon-ambassador.s3.amazonaws.com/hugo_grad.png",
                    preview_image_url = "https://2023-amazon-ambassador.s3.amazonaws.com/hugo_grad.png",
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        else:
            reply_messages = [
                TextSendMessage(
                    text=f'{event_text}'
                ),
            ]
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )

    @handler.add(MessageEvent, message=LocationMessage)
    def handle_sticker_message(event):
        reply_messages = [
            TextSendMessage(
                text=f'We have received your location; however, we won\'t do anything with it now.'
            ),
        ]
            
        line_bot_api.reply_message(
            event.reply_token,
            reply_messages
        )

    @handler.add(MessageEvent, message=StickerMessage)
    def handle_sticker_message(event):
        reply_messages = [
            TextSendMessage(
                text=f'We have received your sticker; however, we won\'t do anything with it now.'
            ),
        ]
            
        line_bot_api.reply_message(
            event.reply_token,
            reply_messages
        )

    @handler.add(MessageEvent, message=FileMessage)
    def handle_file_message(event):
        reply_messages = [
            TextSendMessage(
                text=f'We have received your file; however, we won\'t do anything with it now.'
            ),
        ]
            
        line_bot_api.reply_message(
            event.reply_token,
            reply_messages
        )

    @handler.add(MessageEvent, message=AudioMessage)
    def handle_audio_message(event):
        reply_messages = [
            TextSendMessage(
                text=f'We have received your audio; however, we won\'t do anything with it now.'
            ),
        ]
            
        line_bot_api.reply_message(
            event.reply_token,
            reply_messages
        )
        
    @handler.add(MessageEvent, message=VideoMessage)
    def handle_video_message(event):
        reply_messages = [
            TextSendMessage(
                text=f'We have received your video; however, we won\'t do anything with it now.'
            ),
        ]
            
        line_bot_api.reply_message(
            event.reply_token,
            reply_messages
        )

    @handler.add(MessageEvent, message=ImageMessage)
    def handle_image_message(event):
        reply_messages = [
            TextSendMessage(
                text=f'We have received your image; however, we won\'t do anything with it now.'
            ),
        ]
            
        line_bot_api.reply_message(
            event.reply_token,
            reply_messages
        )

    try:
        # get X-Line-Signature header value
        signature = event['headers']['x-line-signature']

        # get request body as text
        body = event['body']
        handler.handle(body, signature)
    except InvalidSignatureError:
        return {
            'statusCode': 502,
            'body': json.dumps(
                "Invalid signature. Please check your channel access token/channel secret."
            )
        }
    return {
        'statusCode': 200,
        'body': json.dumps(
            "Hello from Lambda!"
        )
    }
