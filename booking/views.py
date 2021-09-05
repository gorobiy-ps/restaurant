from django.shortcuts import render
from django.views import View
import booking.helper as helper
import datetime


class IndexView(View):
    template_name = 'booking/index.html'
    date = datetime.datetime.today().strftime('%Y-%m-%d')

    def get(self, request, date=None):
        if not date:
            date = self.date
        context = helper.get_tables_for_date(date)
        return render(request, self.template_name, context)

    def post(self, request, date=None):
        if not date:
            date = self.date

        username = request.POST.get('username')
        email = request.POST.get('email')
        tables_ids = request.POST.getlist('tables')

        is_valid = helper.validate_email(email)
        if is_valid and len(tables_ids) > 0:
            result = helper.reserv_and_confirm(username, email, date, tables_ids)
        else:
            result = {
                'status' : 'error',
                'class' : 'danger',
                'message': 'Invalid email'
            }
        context = helper.get_tables_for_date(date)
        context['note'] = result
        return render(request, self.template_name, context)
