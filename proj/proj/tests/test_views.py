import pytest

pytestmark = [pytest.mark.django_db]


def test_view(client):
    response = client.get('/', args=[2, 3])
    assert response.status_code == 200
    assert 'The answer is 5.' in response.content.decode('utf-8')
