class Post():
  def __init__(
      self,
       id,
       user_id,
       category_id,
       title,
       publication_date,
       content,
       approved):
    self.id = id
    self.user_id = user_id
    self.category_id = category_id
    self.title = title
    self.publication_date = publication_date
    self.content = content
    self.approved = approved
