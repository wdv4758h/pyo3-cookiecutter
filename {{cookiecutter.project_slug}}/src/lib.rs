extern crate pyo3;


use pyo3::prelude::*;


#[pymodinit]
fn {{cookiecutter.project_slug}}(py: Python, m: &PyModule) -> PyResult<()> {
    #[pyfn(m, "hello")]
    fn hello(_py: Python) -> () {
        println!("hello");
    }

    Ok(())
}
