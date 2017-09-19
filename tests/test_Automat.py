import pytest
from Automat import Automaton
from Edge import Edge
from Vertex import Vertex, initial, final, error


@pytest.fixture(scope="module")
def automaton():
    cvor0 = Vertex("0", True)
    cvor1 = Vertex("1", False, True)

    e1 = Edge(cvor0, cvor0, "b")
    e2 = Edge(cvor0, cvor1, "a")
    return Automaton({cvor0, cvor1}, {e1, e2}, "ab")


@pytest.fixture
def two_automatons():
    return Automaton(alphabet="a"), Automaton(alphabet="b")


def test_transition_by_letter(automaton):
    assert automaton.transition_by_letter(
        automaton.fetch(final), "b") == automaton.fetch(error)


def test_transition_by_letter_exception(automaton):
    with pytest.raises(ValueError) as value_error:
        assert automaton.transition_by_letter(
            automaton.fetch(initial), "ab"), value_error


def test_transition_by_letter_from_error(automaton):
    assert automaton.transition_by_letter(
        automaton.fetch(error), "a") == automaton.fetch(error)


def test_multiply_automaton_error(two_automatons):
    with pytest.raises(ValueError) as value_error:
        assert two_automatons[0] & two_automatons[1], value_error