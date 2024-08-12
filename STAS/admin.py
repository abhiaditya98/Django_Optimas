from django.contrib import admin
from STAS.models import Test ,RecruitmentMaster,VendorName


class RecruitmentMasterAdmin(admin.ModelAdmin):
    list_display=("candidate_name","vendor_name")

admin.site.register(Test)
admin.site.register(RecruitmentMaster,RecruitmentMasterAdmin)
admin.site.register(VendorName)
# Register your models here.

