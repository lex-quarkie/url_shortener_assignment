from app.utils import generate_short_link

def test_generate_link():
    assert len(generate_short_link(10)) == 10