import pytest
from httpapi import HttpApi


@pytest.fixture
def http_bin():
    return HttpApi("http://httpbin.org/")


def test_html(http_bin):
    html = http_bin.html
    assert html.base_url == "http://httpbin.org/html"
    assert "<!DOCTYPE html>" in html.get().text


def test_404(http_bin):
    assert 404 == http_bin.status(404).get().status_code
