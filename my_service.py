
class MyService:

    def __init__(self, sso_registry):
	    self.sso_registry = sso_registry
		
		
    def handle_request(self, request, token):
	    if self.sso_registry_is_valid(None):
		    return "hello world"
		return "please enter your login details"
		