import pytest
import json
import json



@pytest.fixture
def target_env(request):
  config_path = request.config.getoption('--target-env')
  with open(config_path) as config_file:
    config_data = json.load(config_file)
  return config_data


def pytest_addoption(parser):
  parser.addoption(
    '--target-env',
    action='store',
    default='dev.json',
    help='Path to the target environment config file')