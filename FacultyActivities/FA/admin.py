from django.contrib import admin
from .models import AdminLogin,FacultyLogin,SDP_attended,Invited_talks,SDP_organised

# Register your models here.
admin.site.register(AdminLogin)
admin.site.register(FacultyLogin)
admin.site.register(SDP_attended)
admin.site.register(Invited_talks)
admin.site.register(SDP_organised)
