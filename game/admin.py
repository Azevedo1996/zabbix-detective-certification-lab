from django.contrib import admin
from .models import Mission, Challenge, ChallengeAttempt, PlayerProgress
class ChallengeInline(admin.TabularInline):
    model = Challenge
    extra = 0
@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ('code','title','certification','track','order','active')
    list_filter = ('track','certification','active')
    search_fields = ('title','summary')
    inlines = [ChallengeInline]
@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('title','mission','difficulty','order','active')
    list_filter = ('mission','difficulty','active')
    search_fields = ('title','scenario','question')
admin.site.register(ChallengeAttempt)
admin.site.register(PlayerProgress)
