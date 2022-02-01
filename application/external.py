from django.http import JsonResponse


class CustomException(Exception):

    reason: str
    code: int
    workaround: str

    def response(self):
        body = {
            'reason': self.reason,
            'workaround': self.workaround,
        }

        return JsonResponse(data=body, reason=self.reason, status=self.code)


class ProcessRequestException(CustomException):
    reason = 'Error processing request'
    code = 204
    workaround = 'Try again later'


def process_request():
    raise ProcessRequestException
