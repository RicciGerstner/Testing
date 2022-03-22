"""Test root endpoint"""

from Demo.routers import health


def test_root(client):
    # arrange
    endpoint_url = health.prefix + health.path

    # act
    resp = client.get(endpoint_url)
    resp_data = resp.json()

    # assert
    assert resp.status_code == 200
    assert isinstance(resp_data, dict)
