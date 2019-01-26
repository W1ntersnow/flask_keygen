SQL_CREATE_TABLE_KEYS = """
  CREATE TABLE IF NOT EXISTS keys (
    key TEXT PRIMARY KEY, 
    issued INTEGER DEFAULT 0, 
    expired INTEGER DEFAULT 0
  );
"""

SQL_CREATE_TABLE_COUNTERS = """
  CREATE TABLE IF NOT EXISTS counters (
    name TEXT PRIMARY KEY, 
    count INTEGER DEFAULT FALSE
  );
"""

SQL_INSERT_COUNT = """
  INSERT INTO counters (name, count) 
  VALUES ('keys_unique_count', {})
"""

SQL_SELECT_COUNT = """
  SELECT count FROM counters WHERE name = '{}'
"""

SQL_INSERT_GENERATED_KEY = """
  INSERT INTO keys (issued, key) VALUES (1, '{}')
"""


SQL_SELECT_KEY_INFO = """
  SELECT key, issued, expired FROM keys WHERE key = '{}'
"""

SQL_SELECT_REMAINING_KEY_COUNT = """
  SELECT count - (SELECT count(1) FROM keys) 
  FROM counters WHERE name = 'keys_unique_count' 
"""

SQL_UPDATE_KEY_CODE = """
  UPDATE keys SET expired = 1 WHERE key = '{}'
"""
