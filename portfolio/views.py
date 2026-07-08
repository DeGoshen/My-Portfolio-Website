from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Skill, Blog
from .forms import ContactForm


def home(request):
    """
    Home page view.
    Displays top skills and welcome message.
    """
    # Get top 3 skills with highest proficiency
    top_skills = Skill.objects.filter(level__gte=80).order_by('-level')[:3]
    
    # Optional: Get latest blog posts (if you have any)
    latest_posts = Blog.objects.filter(is_published=True).order_by('-date_created')[:3]
    
    context = {
        'top_skills': top_skills,
        'latest_posts': latest_posts,
        'page_title': 'Home'
    }
    
    return render(request, 'pages/home.html', context)


def about(request):
    """
    About page view.
    Displays personal information and services.
    """
    context = {
        'page_title': 'About Us'
    }
    return render(request, 'pages/about.html', context)


def skills_page(request):
    """
    Skills page view.
    Displays all skills with proficiency levels.
    """
    # Get all skills ordered by level (highest first)
    all_skills = Skill.objects.all().order_by('-level')
    
    context = {
        'skills': all_skills,
        'page_title': 'My Skills'
    }
    
    return render(request, 'pages/skills.html', context)


def contact(request):
    """
    Contact page view.
    Handles the contact form submission.
    """
    if request.method == 'POST':
        # Form was submitted
        form = ContactForm(request.POST)
        
        if form.is_valid():
            # Save the contact message to database
            contact_message = form.save()
            
            # Optional: Send email notification (uncomment to enable)
            # try:
            #     send_mail(
            #         subject=f"New Contact Message: {contact_message.subject}",
            #         message=f"From: {contact_message.name} ({contact_message.email})\n\n{contact_message.message}",
            #         from_email=settings.DEFAULT_FROM_EMAIL,
            #         recipient_list=['your.email@example.com'],  # Replace with your email
            #         fail_silently=False,
            #     )
            # except Exception as e:
            #     print(f"Email sending failed: {e}")
            
            # Show success message
            messages.success(
                request, 
                'Thank you for your message! We\'ll get back to you soon.'
            )
            
            # Redirect to clear the form (prevents duplicate submissions on refresh)
            return redirect('contact')
        else:
            # Form has errors
            messages.error(
                request, 
                'There were errors in your form. Please check and try again.'
            )
    else:
        # GET request - show empty form
        form = ContactForm()
    
    context = {
        'form': form,
        'page_title': 'Contact Us'
    }
    
    return render(request, 'pages/contact.html', context)


# Optional: Error handlers (for production)
def custom_404(request, exception):
    """Custom 404 error page."""
    return render(request, 'pages/404.html', status=404)


def custom_500(request):
    """Custom 500 error page."""
    return render(request, 'pages/500.html', status=500)