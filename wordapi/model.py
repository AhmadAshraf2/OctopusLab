from peewee import *
from .cryptography import *

db = MySQLDatabase('word', user='word', password='word', host='db', port=3306)


class Word(Model):

    id = CharField(primary_key=True)
    word = CharField()
    frequency = IntegerField()

    class Meta:
        database = db

    @staticmethod
    def save_to_db(words):
        for word, frequency in words.items():
            w = Word(id=salt_hash(word), word=encrypt_message(word), frequency=frequency)
            try:
                w.save(force_insert=True)
            except:
                w.update()

    @staticmethod
    def retrieve_all_from_db():
        return {decrypt_message(w.word): w.frequency for w in Word.select().order_by(Word.frequency.desc())}


Word.create_table()
