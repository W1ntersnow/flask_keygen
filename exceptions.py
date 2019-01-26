import sqlite3
from config import KEY_LENGTH


KEY_RULE_MESSAGE = 'Key length must be {}'.format(KEY_LENGTH)


class KeyRuleException(Exception):
    pass


class DuplicateKeyException(sqlite3.IntegrityError):
    pass
