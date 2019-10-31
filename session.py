import mechanize
from PIL import Image
from io import BytesIO

def check_aadhaar(uidno):
    # initializing the session
    br = mechanize.Browser()
    br.addheaders = [('User-agent', 'Firefox')]

    br.set_handle_robots(False)   # ignore robots
    br.set_handle_refresh(False)  # can sometimes hang without this

    response = br.open( "https://resident.uidai.gov.in/CaptchaSecurityImages.php?width=100&height=40&characters=5" )

    img = Image.open(BytesIO(response.read()))
    img.show()

    security_code = input('enter the captcha - ')

    # populating the fields in the form
    br.open('https://resident.uidai.gov.in/verify')
    br.select_form('verifyform')
    br.form['uidno'] = uidno
    br.form['security_code'] = security_code
    response = br.submit().read()

    return response