import pytest

from src.decorators import log


def test_log_decorator_stdout(capsys):
    @log()
    def add(a, b):
        return a + b

    add(2, 3)
    captured = capsys.readouterr()
    assert "Function add started with args: (2, 3), kwargs: {}" in captured.out
    assert "Function add finished with result: 5" in captured.out


def test_log_decorator_file(tmpdir):
    log_file = tmpdir.join("log.txt")

    @log(filename=str(log_file))
    def multiply(a, b):
        return a * b

    multiply(4, 5)
    with open(log_file, 'r') as f:
        log_content = f.read()
        assert "Function multiply started with args: (4, 5), kwargs: {}" in log_content
        assert "Function multiply finished with result: 20" in log_content
