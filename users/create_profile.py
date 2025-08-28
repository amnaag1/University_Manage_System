import os
import django

# Django settings load karo
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'university_management.settings')
django.setup()

from django.contrib.auth import get_user_model
from users.models import Profile

User = get_user_model()

for user in User.objects.all():
    # Check karo ki profile exist karti hai ya nahi
    if not hasattr(user, 'profile'):
        Profile.objects.create(user=user)
        print(f"Profile created for user: {user.username}")

print("All missing profiles created.")


