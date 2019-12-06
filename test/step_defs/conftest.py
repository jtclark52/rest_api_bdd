import pytest

from pytest_bdd import given
from selenium import webdriver


# Constants



# Hooks

def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')


# Fixtures

# @pytest.fixture
# def browser():
#     b = webdriver.chrome()
#     b.implicitly_wait(10)
#     yield b
#     b.quit()


# Shared Given Steps

# @given('')

