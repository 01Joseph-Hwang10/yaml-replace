from os.path import dirname, join
import yaml


def get_dummy_yaml_string():
    with open(join(dirname(__file__), "dummy.yaml")) as f:
        return f.read()


def get_expected_yaml():
    with open(join(dirname(__file__), "expected.yaml")) as f:
        return yaml.safe_load(f.read())
