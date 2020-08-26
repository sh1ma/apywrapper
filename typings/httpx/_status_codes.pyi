"""
This type stub file was generated by pyright.
"""

from enum import IntEnum

class codes(IntEnum):
    """HTTP status codes and reason phrases
    Status codes from the following RFCs are all observed:
        * RFC 7231: Hypertext Transfer Protocol (HTTP/1.1), obsoletes 2616
        * RFC 6585: Additional HTTP Status Codes
        * RFC 3229: Delta encoding in HTTP
        * RFC 4918: HTTP Extensions for WebDAV, obsoletes 2518
        * RFC 5842: Binding Extensions to WebDAV
        * RFC 7238: Permanent Redirect
        * RFC 2295: Transparent Content Negotiation in HTTP
        * RFC 2774: An HTTP Extension Framework
        * RFC 7540: Hypertext Transfer Protocol Version 2 (HTTP/2)
        * RFC 2324: Hyper Text Coffee Pot Control Protocol (HTCPCP/1.0)
        * RFC 7725: An HTTP Status Code to Report Legal Obstacles
    """
    def __new__(cls, value: int, phrase: str = ...) -> codes:
        ...
    
    def __str__(self) -> str:
        ...
    
    @classmethod
    def get_reason_phrase(cls, value: int) -> str:
        ...
    
    @classmethod
    def is_redirect(cls, value: int) -> bool:
        ...
    
    @classmethod
    def is_error(cls, value: int) -> bool:
        ...
    
    @classmethod
    def is_client_error(cls, value: int) -> bool:
        ...
    
    @classmethod
    def is_server_error(cls, value: int) -> bool:
        ...
    
    CONTINUE = ...
    SWITCHING_PROTOCOLS = ...
    PROCESSING = ...
    OK = ...
    CREATED = ...
    ACCEPTED = ...
    NON_AUTHORITATIVE_INFORMATION = ...
    NO_CONTENT = ...
    RESET_CONTENT = ...
    PARTIAL_CONTENT = ...
    MULTI_STATUS = ...
    ALREADY_REPORTED = ...
    IM_USED = ...
    MULTIPLE_CHOICES = ...
    MOVED_PERMANENTLY = ...
    FOUND = ...
    SEE_OTHER = ...
    NOT_MODIFIED = ...
    USE_PROXY = ...
    TEMPORARY_REDIRECT = ...
    PERMANENT_REDIRECT = ...
    BAD_REQUEST = ...
    UNAUTHORIZED = ...
    PAYMENT_REQUIRED = ...
    FORBIDDEN = ...
    NOT_FOUND = ...
    METHOD_NOT_ALLOWED = ...
    NOT_ACCEPTABLE = ...
    PROXY_AUTHENTICATION_REQUIRED = ...
    REQUEST_TIMEOUT = ...
    CONFLICT = ...
    GONE = ...
    LENGTH_REQUIRED = ...
    PRECONDITION_FAILED = ...
    REQUEST_ENTITY_TOO_LARGE = ...
    REQUEST_URI_TOO_LONG = ...
    UNSUPPORTED_MEDIA_TYPE = ...
    REQUESTED_RANGE_NOT_SATISFIABLE = ...
    EXPECTATION_FAILED = ...
    IM_A_TEAPOT = ...
    MISDIRECTED_REQUEST = ...
    UNPROCESSABLE_ENTITY = ...
    LOCKED = ...
    FAILED_DEPENDENCY = ...
    UPGRADE_REQUIRED = ...
    PRECONDITION_REQUIRED = ...
    TOO_MANY_REQUESTS = ...
    REQUEST_HEADER_FIELDS_TOO_LARGE = ...
    UNAVAILABLE_FOR_LEGAL_REASONS = ...
    INTERNAL_SERVER_ERROR = ...
    NOT_IMPLEMENTED = ...
    BAD_GATEWAY = ...
    SERVICE_UNAVAILABLE = ...
    GATEWAY_TIMEOUT = ...
    HTTP_VERSION_NOT_SUPPORTED = ...
    VARIANT_ALSO_NEGOTIATES = ...
    INSUFFICIENT_STORAGE = ...
    LOOP_DETECTED = ...
    NOT_EXTENDED = ...
    NETWORK_AUTHENTICATION_REQUIRED = ...


class StatusCodeCompat:
    def __call__(self, *args, **kwargs):
        ...
    
    def __getattr__(self, attr):
        ...
    
    def __getitem__(self, item):
        ...
    


StatusCode = StatusCodeCompat()
