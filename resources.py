import dal
from flask_restful import Resource


class KeyManager(Resource):
    custom_url = '/keys/<key_code>'

    def get(self, key_code):
        db = dal.DBInterface()
        return {'data': db.select_by_key(key_code)}

    def put(self, key_code):
        db = dal.DBInterface()
        db.expire_key(key_code)
        return {'data': key_code}, 201


class KeyGenerator(Resource):
    custom_url = '/acquire_key'

    def post(self):
        db = dal.DBInterface()
        return {'data': db.generate_key()}


class KeyCounter(Resource):
    custom_url = '/keys_count'

    def get(self):
        db = dal.DBInterface()
        return {'data':  db.get_remaining_key_count()}
