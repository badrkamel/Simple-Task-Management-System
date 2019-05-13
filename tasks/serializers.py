from rest_framework import serializers
from .models import Task
      
class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ('user','id','title','description','completed','created_at','updated_at')