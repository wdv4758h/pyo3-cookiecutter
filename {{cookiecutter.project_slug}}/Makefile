wheel:
	# RUSTFLAGS="-C link-arg=-s" python3 setup.py bdist_wheel
	# pyo3-pack build -i python3.7 --skip-auditwheel
	pyo3-pack build --skip-auditwheel

install:
	# pip3 install dist/*.whl --upgrade
	pip3 install target/wheels/*cp3*.whl --upgrade

install-test:
	pip3 install -r requirements-test.txt

develop:
	pyo3-pack develop

test:
	pytest tests/

bench:
	pytest bench/
