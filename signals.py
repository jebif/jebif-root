
def create_profile_for_user(sender, **kwargs):
    from users.models import UserProfile
    user = kwargs['instance']
    UserProfile.objects.get_or_create(user = user)
