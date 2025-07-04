from django.contrib import admin
from .models import Task

admin.site.register(Task)

# スーパーユーザー↓
# username = root
# password = rootUser1