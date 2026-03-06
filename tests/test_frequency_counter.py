from src.frequency_counter import char_frequency


def test_hello_world():
    result = char_frequency("hello world")

    assert result == {
        "h":1,
        "e":1,
        "l":3,
        "o":2,
        "w":1,
        "r":1,
        "d":1
    }


def test_empty():
    assert char_frequency("") == {}


def test_special_characters():
    result = char_frequency("aa!!bb")
    assert result == {
        "a":2,
        "!":2,
        "b":2
    }


def test_case_sensitive():
    result = char_frequency("AaA")
    assert result == {
        "A":2,
        "a":1
    }