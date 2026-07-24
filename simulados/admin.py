from django.contrib import admin
from .models import *
class AnswerOptionInline(admin.TabularInline):
    model = AnswerOption; extra = 4
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','certification','topic','difficulty','requires_lab','active')
    list_filter = ('certification','topic','difficulty','requires_lab','active')
    search_fields = ('statement','reference')
    inlines = [AnswerOptionInline]
@admin.register(Simulation)
class SimulationAdmin(admin.ModelAdmin):
    list_display = ('title','certification','simulation_type','question_count','duration_minutes','active')
    filter_horizontal = ('topics',)
admin.site.register(CertificationLevel); admin.site.register(Topic); admin.site.register(AnswerOption); admin.site.register(SimulationAttempt); admin.site.register(AttemptAnswer); admin.site.register(UserProgress)
