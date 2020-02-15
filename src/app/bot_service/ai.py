from app.bot_service.direct_line_api import DirectLineAPI
from app.variables import Bot
class AI(object):
    """description of class"""

    @staticmethod
    def get_answer(question):
        temporary_key = DirectLineAPI.get_temporary_token(Bot.bot_secret)
        api = DirectLineAPI("new user",temporary_key)
        api.start_conversation()
        api.send(question)
        answer = api.receive()
        if(api.end_conversation()):
            print('conversation ended')
        else:
            print('Failed to end the conversation.')
        return answer