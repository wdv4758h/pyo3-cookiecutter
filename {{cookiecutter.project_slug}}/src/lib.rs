extern crate pyo3;


use pyo3::prelude::*;


#[pymodinit]
fn {{cookiecutter.project_slug}}(_py: Python, m: &PyModule) -> PyResult<()> {
    #[pyfn(m, "func")]
    fn func(_py: Python, data: &str) -> () {
        println!("{}", data);
    }

    Ok(())
}
