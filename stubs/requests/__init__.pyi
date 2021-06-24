import logging
from typing import Any, Text

from .api import delete as delete
from .api import get as get
from .api import head as head
from .api import options as options
from .api import patch as patch
from .api import post as post
from .api import put as put
from .api import request as request
from .exceptions import ConnectionError as ConnectionError
from .exceptions import HTTPError as HTTPError
from .exceptions import ReadTimeout as ReadTimeout
from .exceptions import RequestException as RequestException
from .exceptions import Timeout as Timeout
from .exceptions import TooManyRedirects as TooManyRedirects
from .exceptions import URLRequired as URLRequired
from .models import PreparedRequest as PreparedRequest
from .models import Request as Request
from .models import Response as Response
from .sessions import Session as Session
from .sessions import session as session
from .status_codes import codes as codes

__title__: Any
__build__: Any
__license__: Any
__copyright__: Any
__version__: Any

class NullHandler(logging.Handler):
    def emit(self, record): ...

def check_compatibility(
    urllib3_version: Text, chardet_version: Text
) -> None: ...
