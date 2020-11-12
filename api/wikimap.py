from random import randrange

class Wikimap:
  def __init__(self, db_src_url):
    pass

  def get_page(self, title):
    return (randrange(10000, 100000), title)

  def determine_path(self, src_id, dest_id, algorithm='bfs'):
    return [ randrange(10000, 100000) for _ in range(randrange(100)) ]
