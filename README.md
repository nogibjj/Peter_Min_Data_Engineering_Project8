# Mini_Project_8
[![Python CI/CD Pipeline](https://github.com/nogibjj/Peter_Min_Data_Engineering_Project8/actions/workflows/python_cicd.yml/badge.svg)](https://github.com/nogibjj/Peter_Min_Data_Engineering_Project8/actions/workflows/python_cicd.yml)
[![Rust CI/CD Pipeline](https://github.com/nogibjj/Peter_Min_Data_Engineering_Project8/actions/workflows/rust_cicd.yml/badge.svg)](https://github.com/nogibjj/Peter_Min_Data_Engineering_Project8/actions/workflows/rust_cicd.yml)

This is the README for my Mini Project 8 for the IDS706 - Data Engineering Systems class at Duke University.

## Overview
The purpose of this project is to translate an existing piece of code in Python3 to Rust and compare their performances. For this assignment, I wrote a naive algorithm that finds all prime numbers smaller than or equal to a specified non-negative value.

## Usage
To use the tool, first ensure you have Rust and Cargo installed:

```
rustc --version
cargo --version
```

Then navigate to this project folder and run the calculator in 1 of 2 ways:

`cargo run`

or
```
cd prime_numbers
cargo build
./target/release/prime_numbers
```

## Code Robustnes Check

![alt text](python3_checks.png "Python3 Code Checks")

![alt text](rust_checks.png "Rust Code Checks")

## Performance

![alt text](python3_performance.png "Python3 Performance")

![alt text](rust_performance.png "Rust Performance")

## Performance Summary Note
Since the performance values are in different units, here's a breakdown:

- For a target value of 100
    - Python: 312 bytes, Rust: 224 bytes, Rust uses **28.21% less memory** than Python.
    - Python: 0.0000391006 second, Rust: 0.00002775 second, Rust runs **29.03% faster** than Python.

- For a target value of 500
    - Python: 920 bytes, Rust: 784 bytes, Rust uses **14.78% less memory** than Python.
    - Python: 0.000644207 seconds, Rust: 0.00038575 seconds, Rust runs **40.12% faster** than Python.

- For a target value of 1000
    - Python: 1432 bytes, Rust: 1368 bytes, Rust uses **4.46% less memory** than Python.
    - Python: 0.0024478436 seconds, Rust: 0.001312125 seconds, Rust runs **46.38% faster** than Python.

- For a target value of 5000
    - Python: 5432 bytes, Rust: 5376 bytes, Rust uses **1.03% less memory** than Python.
    - Python: 0.0497107506 seconds, Rust: 0.019291416 seconds, Rust runs **61.19% faster** than Python.

- For a target value of 10000 
    - Python: 10008 bytes, Rust: 9856 bytes, Rust uses **1.52% less memory** than Python.
    - Python: 0.1756289005 seconds, Rust: 0.043136792 seconds, Rust runs **75.44% faster** than Python.

- For a target value of 50000
    - Python: 41880 bytes, Rust: 41088 bytes, Rust uses **1.89% less memory** than Python.
    - Python: 3.8479928970 seconds, Rust: 0.658702 seconds, Rust runs **82.89% faster** than Python.
