from django.core.management.base import BaseCommand
# from authentication.models import Account
from django.contrib.auth.models import User as Account

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
    ('admin', 'admin@mysite.com'),
)


class Command(BaseCommand):

    def handle(self, *args, **options):
        if Account.objects.count() == 0:
            for user in ADMINS:
                username = user[0].replace(' ', '')
                email = user[1]
                password = 'admin'
                print('Creating account for %s (%s)' % (username, email))
                admin = Account.objects.create_superuser(email=email, username=username, password=password)
                admin.is_active = True
                admin.is_admin = True
                admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')
