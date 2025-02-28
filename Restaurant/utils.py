from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import get_user_model
from django.urls import reverse
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

User = get_user_model()

def generate_email_verification_token(user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    return uid, token

def verify_email_token(uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return True
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        pass
    return False

def send_mailgun_email(subject, message, to_email = 'littlelemondemo@gmail.com'):
  	return requests.post(
  		"https://api.mailgun.net/v3/sandbox066e373697194dd1a51dcdde20c93dca.mailgun.org/messages",
  		auth=("api", os.getenv('MAILGUN_API_KEY', 'MAILGUN_API_KEY')),
  		data={"from": "Mailgun Sandbox <postmaster@sandbox066e373697194dd1a51dcdde20c93dca.mailgun.org>",
			"to": to_email,
  			"subject": subject,
  			"text": message})

def send_verification_email(user):
    uid, token = generate_email_verification_token(user)
    verification_url = reverse("verify_email", kwargs={"uidb64": uid, "token": token})
    full_url = f"http://127.0.0.1:8000{verification_url}"  # update domain for production
    subject = "LLittle Lemon - verify your email"
    message = f"click the link to verify your email: {full_url}"
    to_email = user.email
    send_mailgun_email(subject, message, to_email)