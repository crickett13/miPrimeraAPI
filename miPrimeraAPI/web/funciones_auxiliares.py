import json
import decimal
import html
import bleach

def sanitize_input(user_input):
    escaped_input = html.escape(user_input)
    clean_input = bleach.clean(escaped_input)
    return clean_input

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): return float(obj)

def calculariva(importe):
    return importe*0.21