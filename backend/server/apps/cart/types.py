from typing import Union

from django.http import HttpResponse
from rest_framework.response import Response as DRFResponse

ResponseType = Union[HttpResponse, DRFResponse]
