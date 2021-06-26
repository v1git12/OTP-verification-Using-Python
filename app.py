import random,math,os
import pywhatkit as kit

#Random OTP Generator
digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP to verify your identity"
msg= otp

#Getting email id from user
emailid = input("Enter your email: ")

#Send the message from Company's/ personal email-id (You can try Both)
kit.send_mail("Your Email","Your Password","New Email from pywhatkit Auomation by Your_Nmae",f"{msg}",f"{emailid}")
print("An OTP is sent to Your email please check your inbox")
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Your OTP Successfully Verified !!!")
    kit.send_mail("Your Email","Your Password","Email Verification","Your Email is Succesfully verified!!" ,f"{emailid}")
else:
    print("Incorrect OTP!!! \nPlease Check your OTP and try again")
