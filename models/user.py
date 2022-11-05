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
      bio,
      created_on,
      password = ''
      ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password
        self.bio = bio
        self.created_on = created_on


new_user = User(
  17,
  'Elliot',
  'Spencer',
  'Pinhead',
  'pins@hellmail.com',
  'h3ll',
  'Captain of British Expeditionary Force',
  0
  )
