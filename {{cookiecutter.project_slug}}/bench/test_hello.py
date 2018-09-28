import pytest
import {{cookiecutter.project_slug}}


def hello():
    print("hello")

@pytest.mark.benchmark(group='{{cookiecutter.project_slug}}')
def test_uuid1_rs(benchmark):
    benchmark({{cookiecutter.project_slug}}.hello)

@pytest.mark.benchmark(group='{{cookiecutter.project_slug}}')
def test_uuid1_py(benchmark):
    benchmark(hello)
