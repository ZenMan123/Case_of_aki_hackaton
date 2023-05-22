from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import UserOrganizerRegistrationForm, ProfileOrganizerRegistrationForm


def redirect_to_organizer_profile(request):
    return redirect('show_organizer_profile')


def registration(request):
    if request.user.is_authenticated:
        return redirect('show_organizer_profile')

    errors = {'email': [],
              'password': [],
              'repeat_password': [],
              'first_name': [],
              'last_name': [],
              'middle_name': [],
              'phone_number': [],
              'position': [],
              'juridical_name': [],
              'inn': []}

    if request.method == 'POST':
        is_valid = True
        if request.POST['password'] != request.POST['repeat_password']:
            errors['repeat_password'].append('Пароли не совпадают')
            is_valid = False

        user_form = UserOrganizerRegistrationForm(request.POST)
        profile_form = ProfileOrganizerRegistrationForm(request.POST)

        is_valid = user_form.validate(errors) and is_valid
        is_valid = profile_form.validate(errors) and is_valid
        if is_valid:
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.username = user.email
            user.save()

            user_profile = profile_form.save(commit=False)
            user_profile.user = user
            user_profile.save()

            auth.login(request, user)
            return redirect(request.path)

    return render(request, 'organizers/registration.html', {'user_form': UserOrganizerRegistrationForm(),
                                                            'profile_form': ProfileOrganizerRegistrationForm(),
                                                            'errors': errors})


def show_organizer_profile(request):
    if not request.user.is_authenticated:
        return redirect('home')

    if not hasattr(request.user, 'organizer'):
        return redirect('show_client_profile')

    return render(request, 'organizers/profile.html', {'email': request.user.username})


def show_organizer_platforms(request):
    if not request.user.is_authenticated:
        return redirect('home')

    if not hasattr(request.user, 'organizer'):
        return redirect('show_client_profile')

    return render(request, 'organizers/profile.html', {'email': request.user.username})
