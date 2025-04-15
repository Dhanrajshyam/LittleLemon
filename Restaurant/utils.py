from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db.models import Count
import os
import requests
from dotenv import load_dotenv
from datetime import time, timedelta, datetime
from .models import Booking, Restaurant

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
    

def get_12hour_format(time_obj):
    """Convert 24-hour format to 12-hour format"""
    return time_obj.strftime("%I:%M %p")

def get_branches():
    """Return list of branches"""
    return Restaurant.objects.values_list("branch", flat=True)

def get_working_hours(branch):
    """Return working hours of the branch"""
    branch = Restaurant.objects.get(branch=branch)
    opening_time = branch.opening_time.strftime("%H:%M")
    closing_time = branch.closing_time.strftime("%H:%M")
    return opening_time, closing_time

def is_slot_available(branch, booking_date, start_time, end_time, buffer_tables=2):
    """
    Assuming we can take booking of the same time equal to number of tables available in the branch.
    We can have buffer tables like 2 for walk-in customers.
    Check existing booking between start_time and end_time for the given branch and booking_date.
    If number of bookings exceeds or equal to number of tables minus buffer tables, return False.
    else return True.
    """
    branch = Restaurant.objects.get(branch=branch)
    # booking_date = datetime.strptime(booking_date, "%Y-%m-%d").date()
    # start_time = datetime.strptime(start_time, "%H:%M").time()
    # end_time = datetime.strptime(end_time, "%H:%M").time()
    booked_slots = Booking.objects.filter(
        branch=branch.branch,
        booking_date=booking_date,
        start_time__lt=end_time,
        start_time__gte=start_time,
        end_time__gt=start_time,
        end_time__lte=end_time,
        status=Booking.Status.BOOKED
    )
    if booked_slots.count() >= (branch.no_of_tables - buffer_tables):
        return False
    else:
        return True
    