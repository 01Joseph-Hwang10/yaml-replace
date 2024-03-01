from yaml_replace import YAMLTemplate
from .fixtures import get_dummy_yaml_string, get_expected_yaml


def test_yaml_template():
    yaml_string = get_dummy_yaml_string()
    parsed = YAMLTemplate(yaml_string).render(
        {
            "languages": ["Python", "JavaScript", "Java", "C++", "C#"],
            "version": "1.0.0",
        }
    )
    assert parsed == get_expected_yaml()
