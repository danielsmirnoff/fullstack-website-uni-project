import pytest
from django.urls import reverse


@pytest.mark.django_db
@pytest.mark.parametrize(
    "url, expected_fragments",
    [
        (
            reverse("marketplace_home"),
            [
                'for="mobile-search"',
                'id="mobile-search"',
                'for="desktop-search"',
                'id="desktop-search"',
                'aria-label="Search"',
            ],
        ),
        (
            reverse("login"),
            [
                'for="username"',
                'for="password"',
            ],
        ),
        (
            reverse("register"),
            [
                'for="username"',
                'for="email"',
                'for="password1"',
                'for="password2"',
                'autocomplete="username"',
                'autocomplete="email"',
                'autocomplete="new-password"',
            ],
        ),
        (
            f"{reverse('search_results')}?q=test",
            [
                'for="type-mobile"',
                'id="type-mobile"',
                'for="type-desktop"',
                'id="type-desktop"',
                'for="date-mobile"',
                'id="date-mobile"',
                'for="date-desktop"',
                'id="date-desktop"',
                'for="intent-mobile"',
                'id="intent-mobile"',
                'for="intent-desktop"',
                'id="intent-desktop"',
            ],
        ),
    ],
)
def test_accessibility_labels_and_aria_tags(client, url, expected_fragments):
    response = client.get(url)

    assert response.status_code == 200

    html = response.content.decode()
    for fragment in expected_fragments:
        assert fragment in html