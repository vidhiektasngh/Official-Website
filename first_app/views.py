from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature
from .models import UserProfile
from .models import Member  # Import the Member model
from django.http import FileResponse
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.pagesizes import letter
from PIL import Image, ImageOps
import tempfile
from reportlab.lib.pagesizes import letter, landscape  # Import 'landscape' for landscape orientation
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import black
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors
import numpy as np  # Import NumPy
import cv2
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        address = request.POST['address']
        college_name = request.POST['college_name']
        course_name = request.POST['course_name']
        semester = request.POST['semester']
        phone_number = request.POST['phone_number']
        whatsapp_number = request.POST['whatsapp_number']
        insta_username = request.POST['insta_username']
        twitter_username = request.POST['twitter_username']
        telegram_username = request.POST['telegram_username']
        DOB = request.POST['DOB']
        para = request.POST['para']
        declaration = request.POST['declaration']
        flexRadioDefault = request.POST['flexRadioDefault']

        # Access uploaded files
        file_cv = request.FILES['file_cv']
        verified_doc = request.FILES['verified_doc']
        college_id = request.FILES['college_id']
        photo = request.FILES['photo']
        result = request.FILES['result']

        # Now, you have all the data and files to work with
        # You can save the data and files to your models or process them as needed
        user_profile = UserProfile(
            full_name=full_name,
            email=email,
            address=address,
            college_name=college_name,
            course_name=course_name,
            semester=semester,
            phone_number=phone_number,
            whatsapp_number=whatsapp_number,
            insta_username=insta_username,
            twitter_username=twitter_username,
            telegram_username=telegram_username,
            DOB=DOB,
            para=para,
            flexRadioDefault=flexRadioDefault,
            declaration=declaration,
            file_cv=file_cv,
            verified_doc=verified_doc,
            college_id=college_id,
            photo=photo,
            result=result,
        )
        user_profile.save()

        # Don't forget to return a response, e.g., redirect to a success page
        return redirect('pending')
    else:
        return render(request, 'register.html')    

# def register(request):
#     if request.method == 'POST':
#         username= request.POST['username']
#         email= request.POST['email']
#         password= request.POST['password']
#         password2= request.POST['password2']

#         if password == password2:
#             if User.objects.filter(email=email).exists():
#                 messages.info(request, 'Email already exists')
#                 return redirect('register')
#             elif User.objects.filter(username=username).exists():
#                 messages.info(request, 'Email already exists')
#                 return redirect('register')
#             else:
#                 user = User.objects.create_user(username=username, email=email, password=password)
#                 user.save();
#                 return redirect('login')
#         else:
#             messages.info(request, 'Password not same')
#             return redirect('register')
#     else:
#         return render(request, 'register.html')

#    def login(request):
#       if request.method == 'POST':
#           username= request.POST['username']
#            password= request.POST['password']
#
#           user= auth.authenticate(username=username, password=password)
#
#           if user is not None:
#               auth.login(request, user)
#               return redirect('/')
#           else:
#               messages.info(request, 'Invalid details')
#               return redirect('login')
#       
#       else:
#           return render(request, 'login.html')

def idcard(request):
    if request.method == 'POST':
        name = request.POST['name']
        course = request.POST['course']
        college = request.POST['college']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        photo = request.FILES['photo']

        # Create a new Member object and save it to the database
        member = Member(name=name, course=course, college=college, 
                        phone_number=phone_number, email=email, photo=photo)
        member.save()

        # You can add code to generate the ID card PDF here
        return redirect('post', member_id=member.id)  # Redirect to a success page
        # Redirect to the home page

    else:
        return render(request, 'idcard.html')

#___________________________________________________________________________________________________________________#

from PIL import Image

def crop_to_square(image):
    # Ensure the image is open
    img = Image.open(image)

    # Find the dimensions (width and height) of the image
    width, height = img.size

    # Determine the size of the square to crop (use the smaller dimension)
    size = min(width, height)

    # Calculate the coordinates for cropping (left, upper, right, lower)
    left = (width - size) / 2
    upper = 0
    right = left + size
    lower = size

    # Crop the image to the square
    cropped_image = img.crop((left, upper, right, lower))

    return cropped_image

def generate_id_card(request, member_id):
    member = Member.objects.get(id=member_id)  # Retrieve member information

    # Register the "Poppins" font
    pdfmetrics.registerFont(TTFont('Poppins', 'static/assets/Fonts/Poppins Regular 400.ttf'))

    # Register the "Poppins" font
    pdfmetrics.registerFont(TTFont('Poppins-Bold', 'static/assets/Fonts/Poppins-Bold.ttf'))

    # Define your custom page dimensions
    custom_width = 792  # Set your preferred page width in points (1 inch = 72 points)
    custom_height = 512  # Set your preferred page height in points

    # Create a PDF buffer to receive the PDF data
    buffer = BytesIO()

    # Create the PDF object with landscape orientation, using the buffer as its "file."
    p = canvas.Canvas(buffer, pagesize=(custom_width, custom_height))  # Specify landscape orientation here

    # Load the template image
    template_image = Image.open('static/assets/img/College Ambassador.png')

    # Save the template image to a temporary file
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_image:
        template_image.save(temp_image, format='PNG')

    # Draw the template image to cover the entire page
    p.drawImage(temp_image.name, 0, 0, width=792, height=512)  # Swap width and height for landscape

    p.setFont("Poppins-Bold", 12)  # Set font to Helvetica Bold with a size of 12 points

    #    p.drawString(300, 180, f"RESPONSIBILITY: {member.responsibility.upper()}")

    # Use the template design and member data to generate the ID card
    # Replace placeholders with actual member information
    p.drawString(300, 240, f"NAME:")
    p.drawString(300, 220, f"COURSE:")
    p.drawString(300, 200, f"COLLEGE:")
    p.drawString(300, 180, f"PHONE:")
    p.drawString(300, 160, f"EMAIL:")

    p.drawString(360, 240, f"{member.name.upper()}")
    p.drawString(360, 220, f"{member.course.upper()}")
    p.drawString(360, 200, f"{member.college.upper()}")
    p.drawString(360, 180, f"{member.phone_number.upper()}")
    p.drawString(360, 160, f"{member.email}")

    p.setFillColor(colors.white)

    p.setFont("Poppins-Bold", 23)
    p.drawString(280, 290, f"COLLEGE AMBASSADAR")

    p.setFont("Poppins-Bold", 20)
    p.drawString(40, 50, f"MEMBER ID: {member_id}")

    if member.photo:
        cropped_photo = crop_to_square(member.photo.path)

        # Save the cropped image to a temporary file
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_image:
            cropped_photo.save(temp_image, format='PNG')

        # Use the temporary file path in the PDF generation
        p.drawImage(temp_image.name, 82, 148, width=160, height=160)



    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # Set the id_card_generated flag to True for the user
    member.id_card_generated = True
    member.save()

    # FileResponse sets the Content-Disposition header so that browsers present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='id_card.pdf')


#    def display_id_card(request, member_id):
#        member = Member.objects.get(id=member_id)  # Retrieve member information
#        return render(request, 'id_card.html', {'member': member})

def pending(request):
    # In this example, we'll directly render the "id_card.html" template
    return render(request, 'pending.html')

def calender(request):
    # In this example, we'll directly render the "id_card.html" template
    return render(request, 'calender.html')

def generate_infinite_id_cards(request):
    # List of member IDs, you can fetch these from your database or another source
    member_ids = [1, 2, 3, 4, 5, 6, 7]  # Add a new member ID (e.g., 7)

    for member_id in member_ids:
        # Construct the URL for each member's ID card page
        url = f'/post/{member_id}/'  # Use the member's ID to construct the URL
        # Redirect to the member's ID card page
        return redirect(url)

from django.shortcuts import redirect
from django.urls import reverse  # Import reverse for generating URLs

from django.contrib.auth import login
from django.contrib import messages
from .models import AdminProfile  # Import the AdminProfile model

def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already in use, please Sign in!')
                return redirect('sign_up')  # Use the name defined in urls.py
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already in use!')
                return redirect('sign_up')  # Use the name defined in urls.py
            else:
                # Create a new user
                user = User.objects.create_user(username=username, email=email, password=password)

                # Create an associated AdminProfile
                admin_profile = AdminProfile(user=user)
                admin_profile.save()

                # Log in the user
                login(request, user)

                return redirect('dashboard')  # Use the name defined in urls.py for the dashboard
        else:
            messages.info(request, 'Password is not the same!')
            return redirect('sign_up')  # Use the name defined in urls.py
    else:
        return render(request, 'signup.html')


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Fix: Remove the extra 'user' before 'auth.authenticate'
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')  # Correct the redirection
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('sign_in')  # Use 'redirect' instead of returning a tuple
    else:
        return render(request, 'signin.html')

from .models import AdminProfile

@login_required
def dashboard(request):
    # Get the AdminProfile associated with the logged-in user
    admin_profile = AdminProfile.objects.get(user=request.user)
    return render(request, 'dashboard.html', {'admin_profile': admin_profile})

# Announcement

from django.shortcuts import render, redirect
from .models import Announcement


def create_announcement(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Announcement.objects.create(title=title, content=content)
        return redirect('dashboard')  # Redirect to the dashboard after creating an announcement
    return render(request, 'create_announcement.html')


def dashboard(request):
    announcements = Announcement.objects.all().order_by('-created_at')  # Reverse order to show the latest announcement first
    latest_announcement = announcements.first()  # Get the latest announcement
    context = {'announcements': announcements[1:], 'latest_announcement': latest_announcement}

    return render(request, 'dashboard.html', context)

def clear_announcements(request):
    Announcement.objects.all().delete()
    return redirect('dashboard')  # Redirect to the dashboard after clearing announcements


    #This decorator ensures only staff (admin) members can access this view
def clear_announcements(request):
    Announcement.objects.all().delete()
    return redirect('dashboard')

#Tasks
# views.py

from django.shortcuts import render, redirect
from .models import Task


@login_required
def create_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']

        # Get the currently logged-in user
        user = request.user

        # Create a task associated with the logged-in user
        Task.objects.create(user=user, title=title, description=description)

        return redirect('dashboard')  # Redirect to the dashboard after creating a task
    return render(request, 'create_task.html')

@login_required
def dashboard(request):
    # Get tasks associated with the currently logged-in user
    user = request.user
    tasks = Task.objects.filter(user=user)
    context = {'tasks': tasks}
    return render(request, 'dashboard.html', context)


#Spreadsheets

def spreadsheets(request):
    # In this example, we'll directly render the "id_card.html" template
    return render(request, 'spreadsheets.html')

# profile

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required
def edit_profile(request):
    user_profile = AdminProfile.objects.get(user=request.user)

    if request.method == 'POST':
        # Update the user profile based on the form data
        user_profile.profile_picture = request.FILES['profile_picture']
        user_profile.bio = request.POST['bio']
        user_profile.contact_information = request.POST['contact_information']
        # Update other fields as needed
        user_profile.save()
        return redirect('view_profile')  # Redirect to the user's profile view after saving changes

    return render(request, 'edit_profile.html', {'user_profile': user_profile})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import AdminProfile  # Replace with the appropriate import

@login_required
def view_profile(request):
    user_profile = AdminProfile.objects.get(user=request.user)
    return render(request, 'view_profile.html', {'user_profile': user_profile})
