import pytest

import crypto_lib

test_cases_md5 = [
    ('qwerty', 'd8578edf8458ce06fbc5bb76a58c5ca4'),
    ('66665555', '3f1d68c6ffa30e8ee24493c0f8872b04'),
    ('f', '8fa14cdd754f91cc6554c9e71929cce7'),
    ('s', '03c7c0ace395d80182db07ae2c30f034'),
]


@pytest.mark.parametrize('value, expected', test_cases_md5)
def test_encode_md5(value, expected):
    assert crypto_lib.encode_md5(value) == expected
