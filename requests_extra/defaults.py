import requests

timeout = 10

auto_raise_for_status = True

retries_total = 2  # = 3 requests in total
retries_backoff_factor = 1  # retry after 1, 2, 4 secs

retries_status_forcelist = [
    requests.codes.internal_server_error,  # HTTP 500
    requests.codes.bad_gateway,  # HTTP 502
    requests.codes.service_unavailable,  # HTTP 503
    requests.codes.gateway_timeout,  # HTTP 504

    requests.codes.request_timeout,  # HTTP 408
    requests.codes.too_many_requests,  # HTTP 429
]

retries_allowed_methods = [
    "HEAD",
    "GET",
    "PUT",
    "DELETE",
    "OPTIONS",
    "TRACE",
]
