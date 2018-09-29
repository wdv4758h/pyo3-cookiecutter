wheel: has_pyo3_pack
	@echo "===> building wheels"
	@# RUSTFLAGS="-C link-arg=-s" python3 setup.py bdist_wheel
	@# pyo3-pack build -i python3.7 --skip-auditwheel
	pyo3-pack build --skip-auditwheel

install:
	# pip3 install dist/*.whl --upgrade
	pip3 install target/wheels/*cp3*.whl --upgrade

install-test:
	pip3 install -r requirements-test.txt

develop: has_pyo3_pack
	pyo3-pack develop

test: has_pytest
	pytest tests/

bench: has_pytest
	pytest bench/

has_pyo3_pack:
	@echo "===> checking pyo3-pack"
	@which pyo3-pack 1>/dev/null 2> /dev/null

has_pytest:
	@echo "===> checking pytest"
	@which pytest 1>/dev/null 2>/dev/null
