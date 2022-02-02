from django.http import JsonResponse, HttpResponse


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


class CustomException2(Exception):
    reason: str
    code: int
    workaround: str

    def response(self):
        return HttpResponse(status=204)


class ProcessRequestException2(CustomException):
    reason = 'Error processing request'
    code = 204
    workaround = 'Try again later'


def process_request_2():
    raise ProcessRequestException2(CustomException2)
