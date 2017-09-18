import pytest
from Edge import Edge


def test_init():
    with pytest.raises(ValueError) as error:
        assert Edge("a", "b", "c"), error
