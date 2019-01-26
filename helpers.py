import random
import itertools
from string import ascii_letters, digits
import config
import exceptions as exs


def get_uniques_count():
    return len([_ for _ in itertools.product(ascii_letters + digits, repeat=config.KEY_LENGTH)])


def generate_random_unique_string():
    return ''.join(random.SystemRandom().choice(ascii_letters + digits) for _ in range(config.KEY_LENGTH))


def get_bool_value(data):
    return True if str(data).isdigit() == 1 else False


def validate_key(key_code):
    size = len(str(key_code))
    if size != 4:
        raise exs.KeyRuleException(exs.KEY_RULE_MESSAGE)


def pack_key_info_dict(key_code, issued, expired):
    return {
        config.KEY_CODE: key_code,
        config.KEY_ISSUED: issued,
        config.KEY_EXPIRED: expired
    }
