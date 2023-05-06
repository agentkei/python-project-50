import pytest
from gendiff.utility import (get_key, get_values,
                             get_children, get_meta, get_item)


def test_get_item():

    assert list(get_item([])) == []

    assert list(get_item("item")) == ["item"]

    assert list(get_item([1, 2, 3])) == [1, 2, 3]

    assert list(get_item([1, [2, [3, 4]], 5])) == [1, 2, 3, 4, 5]


def test_get_key():

    assert get_key({"key": "value"}) == "value"

    with pytest.raises(KeyError):
        get_key({"not_key": "value"})


def test_get_values():

    assert get_values({"value": {"both": "value1"}}) == ["value1"]

    assert get_values({"value": {"one": "value1"}}) == ["value1"]

    assert get_values({"value": {"first": "value1",
                                 "second": "value2"}}) == ["value1", "value2"]

    assert get_values({"no_value": None}) is None


def test_get_meta():

    assert get_meta({"unchanged": "data"}) == "data"
    assert get_meta({"added": "data"}) == "data"
    assert get_meta({"removed": "data"}) == "data"
    assert get_meta({"changed": "data"}) == "data"


def test_get_children():

    assert (get_children({"children": {**{"child1": "data1"},
                                       **{"child2": "data2"}}})) == [{'child1':
                                                                      'data1',
                                                                      'child2':
                                                                      'data2'}]

    assert get_children({"not_children": "data"}) is None

    assert get_children({"children": None}) is None

    assert get_children({"children": []}) == []

    assert get_children({**{"child1": "data1"}, **{"child2": "data2"}}) is None
