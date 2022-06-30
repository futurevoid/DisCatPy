"""
The MIT License (MIT)

Copyright (c) 2022-present EmreTech

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from ...types import Snowflake
from .._client import _HTTPClient
from .core import APIEndpointData, generate_api_wrapper_functions

__all__ = ("UserEndpointMixin",)

@generate_api_wrapper_functions
class UserEndpointMixin(_HTTPClient):
    get_user = APIEndpointData("GET", "/users/{user_id}", format_args={"user_id": Snowflake})
    get_current_user = APIEndpointData("GET", "/users/@me")
    create_user_dm = APIEndpointData("POST", "/users/@me/channels", param_args=[("recipient_id", Snowflake)])
    modify_current_user = APIEndpointData("PATCH", "/users/@me", param_args=[("username", str)])