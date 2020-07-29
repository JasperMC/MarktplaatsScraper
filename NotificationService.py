from pushover import init, Client

class NotificationService:
    def __init__(self,api_token,user_token):
        self.api_token = api_token
        "a5r3e32d6ghuqyq28u7m4s5cajdsjf"
        self.user_token = user_token
        "uuc8mmii14jezy2uzpcwj2nc9ru4mi"
        self.device = ""
        init(self.api_token)

    def Notify(self, title, message, url, url_title):
        Client(self.user_token, None, self.api_token).send_message(message,title=title, url=url,url_title=url_title)