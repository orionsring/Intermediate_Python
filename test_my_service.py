

from my_service import MyService
from single_sign_on import *

class MyServiceTest(unittest.TestCase):
    def test_invalid_token(self):
	    registry = FakeSignleSignOnRegistry()
		my_service = MyService(registry)
		
		response = my_service.handle_request("do stuff", token=None)
		self.assertIn("please enter your login details", response)
		
	def test_valid_token(self):
	    registry = FakeSignleSignOnRegistry()
		token = registry.register("valid credentials")
		my_service = MyService(registry)
		
		response = my_service.handle_request("do stuff", token)
		self.assertIn("hello world", response)
		
	def test_invalid_token_with_mock(self):
	    token = SSOToken()
		registry = MockSingleSignOnRegistry(expected_token=token, token_is_valid=True)
		my_service = MyService(registry)
		
		response = my_service.handle_request("do stuff", token)
		self.assertTrue(registry.is_valid_was_called)
		

	
