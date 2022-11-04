class User():
    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(
      self,
      id,
      first_name,
      last_name,
      username,
      email,
      password,
      bio,
      created_on,
      active
      ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password
        self.bio = bio
        self.created_on = created_on
        self.active = 1

new_user = User(
  17,
  'Elliot',
  'Spencer',
  'Pinhead',
  'pins@hellmail.com',
  'h3ll',
  'Captain of British Expeditionary Force',
  0,
  1
  )
    def __init__(self, id, first_name, last_name, email, bio, profile_image_url, created_on, active, username, password = ''):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.bio = bio
        self.profile_image_url = profile_image_url
        self.created_on = created_on
        self.active = active
        self.username = username
        self.password = password
