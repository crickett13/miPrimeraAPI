import json
import decimal
import html
import bleach
import bcrypt
from werkzeug.http import http_date

def sanitize_input(user_input):
    escaped_input = html.escape(user_input)
    clean_input = bleach.clean(escaped_input)
    return clean_input

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): return float(obj)

def calculariva(importe):
    return importe*0.21


def cipher_password(password):
    hashAndSalt = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(10));
    return hashAndSalt
def compare_password(password_hash,password):
    if password_hash is None:
        return False
    try:
        return bcrypt.checkpw(password,password_hash)
    except:
        return False
    
def prepare_response_extra_headers(include_security_headers):
    response_extra_headers = {
        # always
        'Cache-Control': 'no-cache, no-store, must-revalidate',
        'Pragma': 'no-cache',
        'Expires': '0',
        'Last-Modified': http_date(datetime.datetime.now()),
    }
    if include_security_headers:
        response_security_headers = {
            # X-Frame-Options: page can only be shown in an iframe of the same site
            'X-Frame-Options': 'SAMEORIGIN',
            # ensure all app communication is sent over HTTPS
            'Strict-Transport-Security': 'max-age=63072000; includeSubdomains',
            # instructs the browser not to override the response content type
            'X-Content-Type-Options': 'nosniff',
            # enable browser cross-site scripting (XSS) filter
            'X-XSS-Protection': '1; mode=block', 'Server':'API'
        }
        response_extra_headers.update(response_security_headers)
    return response_extra_headers