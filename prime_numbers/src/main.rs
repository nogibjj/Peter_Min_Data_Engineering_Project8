use std::time::Instant;

pub fn find_all_primes(target: u64) -> Vec<u64> {
    let mut result = Vec::new();
    if target <= 1 {
        return result;
    }

    for value in 2..target {
        let mut is_prime = true;
        for i in 2..value {
            if value % i == 0 {
                is_prime = false;
                break;
            }
        }
        if is_prime {
            result.push(value);
        }
    }
    result
}

pub fn runtime_calculator() {
    let target_values = [100, 500, 1000, 5000, 10000, 50000];

    for &target in target_values.iter() {
        println!("Testing {}", target);

        let start_time = Instant::now();
        let prime_numbers = find_all_primes(target);
        let duration = start_time.elapsed();

        let memory_usage = std::mem::size_of_val(&prime_numbers)
            + std::mem::size_of::<u64>() * prime_numbers.len();

        println!("Time usage: {:.10?} seconds", duration);
        println!("Memory usage: {} bytes", memory_usage);
    }
}

fn main() {
    runtime_calculator();
}
