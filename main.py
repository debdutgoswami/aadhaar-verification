import mechanize, verification, session

uidno = input('enter the aadhar number - ')

response = session.check_aadhaar(uidno)

verification.check_exist(response)