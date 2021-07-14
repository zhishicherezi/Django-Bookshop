from django import template
import requests

from time import monotonic
import datetime

register = template.Library()

currency_api_url = 'https://www.nbrb.by/api/exrates/rates/840?parammode=1'


@register.simple_tag(name='currency_rate')
def currency_rate():
    usd_dict = requests.get(currency_api_url)
    rate = usd_dict.json().get('Cur_OfficialRate')
    return rate

@register.simple_tag
def one():
    return 'ones'

@register.simple_tag(name='timer')
def timer():
    t = monotonic()
    delta = datetime.datetime(2021, 10, 10) - datetime.datetime.now()
    while True:
        if monotonic() - t > 10:
            t = monotonic()
            return(delta.days, delta.seconds // 3600, (delta.seconds // 60) % 60, delta.seconds % 60)

    
