class Users:
    """docstring"""
    def __init__(self, id, first_name, last_name, username, email, bio, profile_image_url, created_on, active, password = ''):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.bio = bio
        self.profile_image_url = profile_image_url
        self.created_on = created_on
        self.active = active
