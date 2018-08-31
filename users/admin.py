from django.contrib import admin
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ Setup for the profile model Admin """

    """Columns that the admin show"""
    list_display = ('pk', 'user', 'phone_number','website', 'picture')
    """Columns with link to detail view"""
    list_display_links = ('pk', 'user',)
    """Fields editables into de columns"""
    list_editable = ('phone_number', 'website', 'picture')
    """Search Fields (some of them are from auth.user)"""
    search_fields = ('user__username', 'user__email',
                     'user__first_name', 'user__last_name',
                     'phone_number')

    """ List filters (Django know when we use a date) """
    list_filter = ('created', 'modified', 'user__is_active',
                   'user__is_staff')

    """ Order to display fields """
    fieldsets = (
        ('Profile', {
            'fields':(('user', 'picture'),)
        }),
        ('Extra Info', {
            'fields':(
                ('website', 'phone_number'),
                ('biography'))
        }),
        ('Metadata', {
            'fields':(('created', 'modified'),)
        }),
    )

    readonly_fields = ('created', 'modified')
