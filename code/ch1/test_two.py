def test_failing():
    assert (1, 2, 3) == (3, 2, 1)


def test_unfailing():
    assert 3 in (3, 2, 1)
