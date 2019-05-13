from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
	list_filter = ('completed', 'created_at', 'user')
	list_editable = ('completed',)
	search_fields = ('title', 'description')
	list_display = ['title', 'completed']

	class Meta:
		model = Task
	
admin.site.register(Task, TaskAdmin)