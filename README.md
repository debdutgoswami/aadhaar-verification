[![HitCount](http://hits.dwyl.io/debdutgoswami/aadhaar-verification.svg)](http://hits.dwyl.io/debdutgoswami/aadhaar-verification)

# Aadhar Number Verification

I tried to make a simple python project to check whether a particular Aadhaar Number actually exists or not. Here the user just needs to enter the Aadhaar Card Number and enter the captcha (the image will pop open on a different window) and if the Aadhaar Number exists or not, it would any way show the appropiate message.

Currently the captcha is needed to be entered by the user manually but I am trying to automate this process. I have tried using ```pytesseract``` to detect the captcha text but it fails to detect it. I think the only way of doing this is by using Deep Learning.

I am open to all suggestion, specially for automating the ```Captcha recognition```.

## Instructions

Run the ```main.py``` file and enter the Aadhaar Number and the Captcha. Execute the file using the following command ```python main.py```
