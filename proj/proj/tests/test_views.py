import pytest

pytestmark = [pytest.mark.django_db]


def test_view(client):
    response = client.get('/', args=[2, 3])
    assert response.status_code == 200
    assert 'The answer is 5.' in response.content.decode('utf-8')
    response = client.get('/', args=[5, 4])
    assert response.status_code == 200
    assert 'The answer is 9.' in response.content.decode('utf-8')
    response = client.get('/', args=[3, 5, 7])
    assert response.status_code == 200
    assert 'The answer is 15.' in response.content.decode('utf-8')
