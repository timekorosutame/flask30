from app import app
from flask_testing import TestCase
import unittest

class FlaskTestCase(unittest.TestCase):

	# flask налаштований коректно
	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type = 'html/text')
		self.assertEqual(response.status_code, 200)

	# сторінка login загружається добре
	'''response.data -> бінарна стрічка типа bytes у котрій весь html
	   перевірка йде через (знаходження/не знаходження) у b'html' частини b'please login' '''

	def test_login_page_loads(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type = 'html/text')
		self.assertTrue(b'Please login' in response.data)

	# сторінка login поводиться добре з коректним паролем і юзернеймом
	def test_correct_login(self):
		tester = app.test_client(self)
		response = tester.post('/login', 
			data = dict(username = 'admin', password = 'admin'), follow_redirects = True)

		self.assertIn(b'u logged in', response.data)


	# сторінка login поводиться добре з некоректним паролем чи юзернеймом
	def test_incorrect_login(self):
		tester = app.test_client(self)
		response = tester.post('/login', 
			data = dict(username = 'incorrect', password = 'incorrect'), follow_redirects = True)

		self.assertIn(b'invalid credentuals please, try again', response.data)


	# сторінка logout поводиться добре
	def test_logout_page_loads(self):

		tester = app.test_client(self)
		tester.post('/login', 
			data = dict(username = 'admin', password = 'admin'), follow_redirects = True)
		response = tester.get('/logout', follow_redirects = True)

		self.assertIn(b'u logged out', response.data)

	# головна сторінка просить login
	def test_main_requires(self):
		tester = app.test_client(self)
		response = tester.get('/', follow_redirects = True)

		self.assertIn(b'u need to login first', response.data)



	# пости є на головній сторінці
	def test_posts_onmain(self):
		tester = app.test_client(self)
		response = tester.post('/login', 
				data = dict(username = 'admin', password = 'admin'), follow_redirects = True)

		self.assertIn(b'Posts:', response.data)


	# logout вимагає login для спрацювання




if __name__ == '__main__':
	unittest.main()