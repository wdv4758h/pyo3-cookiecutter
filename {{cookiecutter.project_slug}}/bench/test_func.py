import pytest
import {{cookiecutter.project_slug}}


def func(data):
    print(data)

@pytest.mark.benchmark(group='{{cookiecutter.project_slug}}')
def test_func_rs(benchmark):
    benchmark({{cookiecutter.project_slug}}.func, "test")

@pytest.mark.benchmark(group='{{cookiecutter.project_slug}}')
def test_func_py(benchmark):
    benchmark(func, "test")
