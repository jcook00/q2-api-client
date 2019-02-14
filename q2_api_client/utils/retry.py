import time

import requests


def retry(poll_frequency=3, timeout=15, raise_for_status=False):
    """Calls the method provided until the response status code is 200.

    :param poll_frequency: number of seconds to wait before retrying a call
    :param timeout: total number of seconds to retry a call before timing out
    :param bool raise_for_status: If True, raise a HTTPError
        if the return status code is in the 400-599 range
    :raise HTTPError: the return status code is in the 400-599 range
    """
    def decorator(method):

        def retry_method(*args, **kwargs):
            end_time = time.time() + timeout
            while True:
                response = method(*args, **kwargs)
                if response.status_code == requests.codes.ok or time.time() > end_time:
                    if raise_for_status:
                        response.raise_for_status()
                    return response
                time.sleep(poll_frequency)

        return retry_method

    return decorator
