from django.contrib import admin
from django_summernote.admin import SummernoteModelAdminMixin
from .models import patient, doctor, rating_review
# from .models import patient , doctor , diseaseinfo , consultation,rating_review

# Custom admin configuration for Patient model
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender','mobile_no')  # Adjust based on your model fields
    search_fields = ('name', 'id')
    list_filter = ('gender','age')
    # list_editable = ('status',)
    ordering = ('name',)

# # Custom admin configuration for Doctor model
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization','qualification','gender','age')
    search_fields = ('name', 'specialization','qualification')
    list_filter = ('specialization','gender','qualification')
    ordering = ('name',)

# # Custom admin configuration for RatingReview model
# class RatingReviewAdmin(SummernoteModelAdminMixin, admin.ModelAdmin):
#     list_display = ('id', 'patient', 'doctor', 'rating', 'created_at')
#     search_fields = ('patient__name', 'doctor__name')
#     list_filter = ('rating', 'created_at')
#     ordering = ('-created_at',)
#     summernote_fields = ('review',)  # If you want rich-text support for reviews

# # Register models with custom admin configurations
admin.site.register(patient, PatientAdmin)
admin.site.register(doctor, DoctorAdmin)
# admin.site.register(rating_review, RatingReviewAdmin)
