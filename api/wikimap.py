import os.path
import sqlite3
from random import randrange
from graph_algorithms import breadth_first_search

class Wikimap:
  def __init__(self, db_src_url):
    if not os.path.isfile(db_src_url):
      raise IOError(f'Source file {db_src_url} does not exist')

    self.connection = sqlite3.connect(db_src_url, check_same_thread=False)
    self.cursor = self.connection.cursor()
    self.cursor.arraysize = 1000

  def get_page(self, title):
    # return (randrange(10000, 100000), title)
    title = self.serialize_title(title)
    query = 'SELECT * FROM pages WHERE title = ? COLLATE NOCASE'
    query_bindings = (title,)
    self.cursor.execute(query, query_bindings)

    result = self.cursor.fetchall()

    if not result:
      raise ValueError(f'Queried page does not exist')

    for current_page_id, current_page_title, current_page_is_redirect in result:
      if current_page_title == title and not current_page_is_redirect:
        return (current_page_id, self.serialize_title(current_page_title))

    for current_page_id, current_page_title, current_page_is_redirect in result:
      if not current_page_is_redirect:
        return (current_page_id, self.serialize_title(current_page_title))

    raise ValueError(f'Queried page did not show up in results')

  def determine_path(self, src_id, dest_id, algorithm='bfs'):
    # return [ randrange(10000, 100000) for _ in range(randrange(100)) ]
    return breadth_first_search(src_id, dest_id, self)

  def get_outgoing_link_count(self, ids):
    ids = str(tuple(ids)).replace(',)', ')')

    query = f'SELECT SUM(outgoing_links_count) FROM links WHERE id IN {ids}'

    self.cursor.execute(query)
    return self.cursor.fetchone()[0]

  def get_incoming_link_count(self, ids):
    ids = str(tuple(ids)).replace(',)', ')')

    query = f'SELECT SUM(incoming_links_count) FROM links WHERE id IN {ids}'

    self.cursor.execute(query)
    return self.cursor.fetchone()[0]

  def get_outgoing_links(self, ids):
    ids = str(tuple(ids)).replace(',)', ')')

    query = f'SELECT id, outgoing_links FROM links WHERE id IN {ids}'

    self.cursor.execute(query)
    return self.cursor

  def get_incoming_links(self, ids):
    ids = str(tuple(ids)).replace(',)', ')')

    query = f'SELECT id, incoming_links FROM links WHERE id IN {ids}'

    self.cursor.execute(query)
    return self.cursor

  def serialize_title(self, title):
    return title.strip().replace(' ', '_').replace("'", "\\'").replace('"', '\\"')

  def deserialize_title(self, title):
    return title.strip().replace('_', ' ').replace("\\'", "'").replace('\\"', '"')
