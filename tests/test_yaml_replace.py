from os.path import join, dirname
from yaml_replace import YAMLTemplate
from .fixtures import (
    get_dummy_yaml_string,
    get_expected_yaml,
    get_simple_yaml,
    get_expected_simple_yaml,
    get_dummy_substitutions,
)


def test_yaml_template():
    yaml_string = get_dummy_yaml_string()
    parsed = YAMLTemplate(yaml_string).render(
        {
            "languages": ["Python", "JavaScript", "Java", "C++", "C#"],
            "version": "1.0.0",
        }
    )
    assert parsed == get_expected_yaml()


def test_yaml_template_from_file():
    file_path = join(dirname(__file__), "fixtures", "dummy.yaml")
    parsed = YAMLTemplate.from_file(file_path).render(
        {
            "languages": ["Python", "JavaScript", "Java", "C++", "C#"],
            "version": "1.0.0",
        }
    )
    assert parsed == get_expected_yaml()


def test_yaml_template_none():
    assert (
        YAMLTemplate(get_simple_yaml()).render(get_dummy_substitutions())
        == get_expected_simple_yaml()
    )
