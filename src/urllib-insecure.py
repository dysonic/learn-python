import urllib.request
import ssl

# Create an unverified SSL context
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# The URL you want to access
url = 'https://example.com' 

# Use the context in the urlopen call
try:
    with urllib.request.urlopen(url, context=ctx) as response:
        html = response.read()
        print(html)
except urllib.error.URLError as e:
    print(f"An error occurred: {e.reason}")
