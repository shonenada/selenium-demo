from flask.ext.testing import LiveServerTestCase
from selenium import webdriver

from demo.app import create_app as create_demo_app


class FrontEndTestCase(LiveServerTestCase):

    def setUp(self):
        self.brower = webdriver.PhantomJS()
        # or:
        # self.brower = webdriver.FireFox() etc.

    def create_app(self):
        app = create_demo_app()
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 4000
        return app

    def get_url(self, url):
        return ''.join([self.get_server_url(), url])

    def test_basic_html(self):
        self.brower.get(self.get_url('/'))
        demo_box = self.brower.find_element_by_id('demo-box')
        self.assertIn('Demo', demo_box.text)

    def test_add_content_script(self):
        self.brower.get(self.get_url('/'))
        demo_box = self.brower.find_element_by_id('demo-box')
        self.brower.execute_script('''
        add_content('Content added');
        ''')
        self.assertIn('Content added', demo_box.text)

    def test_a_button(self):
        self.brower.get(self.get_url('/'))
        demo_box = self.brower.find_element_by_id('demo-box')
        add_btn = self.brower.find_element_by_id('add-btn')
        add_btn.click()
        self.assertIn('Added by button', demo_box.text)
