
from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from .models import Booking

@shared_task
def send_booking_notification(booking_id):
    try:
        booking = Booking.objects.get(id=booking_id)
        booking_time = booking.booking_time
        notification_time = booking_time - timezone.timedelta(hours=2)
        current_time = timezone.now()
        
        if current_time >= notification_time:
            # Send notification
            send_mail(
                'Upcoming Booking Notification',
                f'Your booking ({booking.id}) is scheduled in 2 hours.Thank you',
                'sportigoplayspot@gmail.com',
                [booking.user.email],
                fail_silently=False,
            )
    except Booking.DoesNotExist:
        pass
