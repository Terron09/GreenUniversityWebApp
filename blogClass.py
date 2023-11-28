# base class code
class Blog:
  blog_id = 0
  def __init__(self, account, post_name, post_content, upvote_count, genre):
    Blog.blog_id += 1
    self.__blog_id = Blog.blog_id
    self.__account = account
    self.__post_name = post_name
    self.__post_content = post_content
    self.__upvote_count = upvote_count
    self.__genre = genre

  def set_account(self, account):
      self.__account = account

  def set_post_name(self, post_name):
      self.__post_name = post_name

  def set_post_content(self, post_content):
      self.__post_content = post_content

  def set_upvote_count(self, upvote_count):
      self.__upvote_count = upvote_count

  def set_genre(self, genre):
      self.__genre = genre

  def get_account(self):
      return self.__account

  def get_post_name(self):
      return self.__post_name

  def get_post_content(self):
      return self.__post_content

  def get_upvote_count(self):
      return self.__upvote_count

  def get_genre(self):
      return self.__genre
    
