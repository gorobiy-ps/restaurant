from django.core import validators, exceptions, mail
from django.conf import settings
from .models import Table, Reservation


def get_tables_for_date(date):
    tables = Table.objects.all()
    booked = tables.filter(reservation__date=date)
    for table in tables:
        if table in booked:
            table.reserved = 'reserved'
    return {'current_date': date, 'tables': tables}

def validate_email(email):
    try:
        validators.validate_email(email)
        return True
    except exceptions.ValidationError:
        return False


def reserv_and_confirm(username, email, date, tables_ids):
    tables = Table.objects.filter(id__in=tables_ids)
    reservations = []
    for table in tables:
        reservations.append(Reservation(
            table = table,
            date = date,
            username = username,
            email = email
        ))
    Reservation.objects.bulk_create(reservations)
    send_confirmation(username, email, date, tables_ids)
    result = {
        'status' : 'success',
        'class' : 'success',
        'message': 'Your table(s) successfully reserved. Check your email.'
    }
    return result


def send_confirmation(username, email, date, tables_ids):
    tables_str = ','.join(tables_ids)
    subject = 'Confirmation of reservation'
    message = 'Dear {}, table(s) {} have been successfully booked for {}'
    mail.send_mail(
        subject,
        message.format(username, tables_str, date),
        settings.EMAIL_HOST_USER,
        [email]
    )
