import dal_helpers as dh
import exceptions as exs
import sql
import helpers


class DBInterface(dh.DBBaseCommands):

    def __init__(self):
        self.connnection = self.define_connection()

    def create_tables(self):
        self.execute_query(sql.SQL_CREATE_TABLE_KEYS, commit=False)
        self.execute_query(sql.SQL_CREATE_TABLE_COUNTERS, commit=False)
        self.insert_counters()
        self.close_connection()

    def insert_counters(self):
        if self.execute_query(sql.SQL_SELECT_COUNT, 'keys_unique_count'):
            return
        key_combs_count = helpers.get_uniques_count()
        self.execute_query(sql.SQL_INSERT_COUNT, key_combs_count, commit=True)

    def generate_key(self):
        while True:
            key_code = helpers.generate_random_unique_string()
            try:
                self.execute_query(sql.SQL_INSERT_GENERATED_KEY, key_code, commit=True)
            except exs.DuplicateKeyException:
                pass
            else:
                break
        self.close_connection()
        return key_code

    def select_by_key(self, key_code):
        helpers.validate_key(key_code)
        data = self.execute_query(sql.SQL_SELECT_KEY_INFO, key_code)
        if not data:
            result = helpers.pack_key_info_dict(key_code, False, False)
        else:
            data = data[0]
            result = helpers.pack_key_info_dict(key_code,
                                                helpers.get_bool_value(data[1]),
                                                helpers.get_bool_value(data[2]))
        return result

    def get_remaining_key_count(self):
        result = self.execute_query(sql.SQL_SELECT_REMAINING_KEY_COUNT)
        return result[0][0]

    def expire_key(self, key_code):
        helpers.validate_key(key_code)
        self.execute_query(sql.SQL_UPDATE_KEY_CODE, key_code, commit=True)
        return True




