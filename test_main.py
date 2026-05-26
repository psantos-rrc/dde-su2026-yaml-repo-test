from goodhello import hello, bye, greet

def test_hello_returns_none():
    assert hello() is None

def test_bye_returns_none():
    assert bye() is None

def test_greet_returns_none():
    assert greet() is None

def test_hello_prints_expected_text(capsys):
    hello()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, DevOps learner!"

def test_bye_prints_expected_text(capsys):
    bye()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Goodbye!"