import pytest

# The autouse=True parameter makes this fixture run automatically for every test in this module,
# without needing to explicitly request it in the test function parameters.
#
# Setup with autouse fixtures:
# 1. They run automatically for every test in their scope (function, class, module, or session)
# 2. Useful for setup/teardown that applies to multiple tests

# We use `yield` to separate setup from teardown:
# - Code before `yield` runs before the test (setup)
# - Code after `yield` runs after the test (teardown)

# Jest/Jasmine        | # Pytest equivalent
# -------------------|--------------------
# beforeAll          | @pytest.fixture(scope="module", autouse=True)
# afterAll           | @pytest.fixture(scope="module", autouse=True) with yield
# beforeEach         | @pytest.fixture(autouse=True)
# afterEach          | Code after yield in an autouse fixture

@pytest.fixture(autouse=True)
def prepare_data():
    # Setup: Runs before each test
    data = [i for i in range(10)]
    
    # The test runs at this point
    yield data
    
    # Teardown: Runs after each test
    # The only time you'd need explicit cleanup is when:
    # Working with external resources (files, databases, network connections)
    # Managing global state
    # Dealing with non-memory resources
    # data.clear()

def test_elements(prepare_data):
    # prepare_data is automatically provided by the autouse fixture
    assert 9 in prepare_data
    assert 10 not in prepare_data