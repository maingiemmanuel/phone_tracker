from django.shortcuts import render, redirect
from .forms import PhoneTrackingForm
from .models import PhoneTracking
import requests


def track_phone(request):
    if request.method == 'POST':
        form = PhoneTrackingForm(request.POST)
        if form.is_valid():
            phone_tracking = form.save(commit=False)

            # Send data to authorities (assuming a REST API)
            response = requests.post('https://api.authorities.example/track', data={
                'imei': phone_tracking.imei,
                'phone_number': phone_tracking.phone_number
            })

            if response.status_code == 200:
                data = response.json()
                phone_tracking.location = data.get('location', 'Unknown')
                phone_tracking.save()
                return redirect('tracking_success')
            else:
                form.add_error(None, 'Failed to track the phone with authorities.')
    else:
        form = PhoneTrackingForm()

    return render(request, 'track_phone.html', {'form': form})


def tracking_success(request):
    return render(request, 'success.html')
