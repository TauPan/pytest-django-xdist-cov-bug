import pytest

from app.templatetags import tags

pytestmark = [pytest.mark.django_db]


def test_add_tag():
    assert tags.add([3, 5]) == 'The answer is 8.'
