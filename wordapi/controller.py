import tornado.web
import tornado.httpclient
import tornado.gen
from .model import Word
from .helper import *


class WebsiteController(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def post(self, *args):
        http_client = tornado.httpclient.AsyncHTTPClient()
        url = self.request.body_arguments.get('url')[0]
        response = yield http_client.fetch(url)
        wordlist = extract_page_source(response)
        words = word_count(wordlist)
        Word.save_to_db(words)
        self.render("template/word_display.html", items=words)


class HomePageController(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        self.render("template/homepage.html", title="home page")


class AdminController(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        words = Word.retrieve_all_from_db()
        self.render("template/word_display.html", items=words)
