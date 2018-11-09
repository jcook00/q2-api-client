from client.services.q2_config_service import Q2ConfigService


class Q2Client(object):

    def __init__(self, **kwargs):
        self.q2config = Q2ConfigService(**kwargs)
        kwargs['q2token'] = self.q2config.headers.get('q2token')
