import pytest

pytestmark = [pytest.mark.django_db]


def test_view(client):
    response = client.get('/')
    assert response.status_code == 200
