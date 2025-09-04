#!/usr/bin/env python3
"""
Synthetic Validation Datasets for Fractal-Harmonic Transform
===========================================================

This module generates synthetic datasets for validating the FHT algorithm.
All datasets are artificially created to demonstrate research methodology
without disclosing proprietary or real-world data.

WARNING: These are synthetic datasets created for educational and
validation purposes only. They do not contain real research data.

Author: Bradley Wallace, COO & Lead Researcher, Koba42 Corp
Contact: coo@koba42.com
Website: https://vantaxsystems.com

License: Creative Commons Attribution-ShareAlike 4.0 International
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Tuple, Any
import json
import os


class SyntheticDataGenerator:
    """
    Generates synthetic datasets that mimic the characteristics of
    real-world data used in FHT research, without revealing proprietary information.
    """

    def __init__(self, seed: int = 42):
        """
        Initialize the synthetic data generator.

        Parameters:
        -----------
        seed : int
            Random seed for reproducible results
        """
        self.seed = seed
        np.random.seed(seed)
        self.phi = (1 + np.sqrt(5)) / 2  # Golden ratio

    def generate_fibonacci_sequence(self, length: int) -> np.ndarray:
        """
        Generate a Fibonacci-based sequence.

        Parameters:
        -----------
        length : int
            Length of the sequence

        Returns:
        --------
        np.ndarray : Fibonacci sequence
        """
        if length <= 0:
            return np.array([])

        sequence = [1, 1]
        while len(sequence) < length:
            sequence.append(sequence[-1] + sequence[-2])

        return np.array(sequence[:length], dtype=float)

    def generate_golden_ratio_sequence(self, length: int) -> np.ndarray:
        """
        Generate a sequence based on powers of the golden ratio.

        Parameters:
        -----------
        length : int
            Length of the sequence

        Returns:
        --------
        np.ndarray : Golden ratio power sequence
        """
        powers = np.arange(1, length + 1)
        return np.array([self.phi ** power for power in powers])

    def generate_prime_modulo_sequence(self, length: int, modulo: int = 100) -> np.ndarray:
        """
        Generate a sequence based on prime numbers modulo an integer.

        Parameters:
        -----------
        length : int
            Length of the sequence
        modulo : int
            Modulo value

        Returns:
        --------
        np.ndarray : Prime modulo sequence
        """
        primes = self._generate_primes(length * 3)  # Generate extra primes
        return np.array([prime % modulo for prime in primes[:length]], dtype=float)

    def generate_logarithmic_sequence(self, length: int) -> np.ndarray:
        """
        Generate a logarithmic sequence for testing scale invariance.

        Parameters:
        -----------
        length : int
            Length of the sequence

        Returns:
        --------
        np.ndarray : Logarithmic sequence
        """
        x_values = np.linspace(0.1, 100, length)
        return np.log(x_values)

    def generate_exponential_sequence(self, length: int) -> np.ndarray:
        """
        Generate an exponential sequence.

        Parameters:
        -----------
        length : int
            Length of the sequence

        Returns:
        --------
        np.ndarray : Exponential sequence
        """
        x_values = np.linspace(0.1, 5, length)
        return np.exp(x_values)

    def generate_polynomial_sequence(self, length: int, degree: int = 3) -> np.ndarray:
        """
        Generate a polynomial sequence.

        Parameters:
        -----------
        length : int
            Length of the sequence
        degree : int
            Degree of the polynomial

        Returns:
        --------
        np.ndarray : Polynomial sequence
        """
        x_values = np.linspace(-5, 5, length)
        coefficients = np.random.uniform(-2, 2, degree + 1)

        result = np.zeros(length)
        for i, coeff in enumerate(coefficients):
            result += coeff * (x_values ** i)

        return result

    def generate_sinusoidal_sequence(self, length: int, frequency: float = 1.0) -> np.ndarray:
        """
        Generate a sinusoidal sequence.

        Parameters:
        -----------
        length : int
            Length of the sequence
        frequency : float
            Frequency of the sine wave

        Returns:
        --------
        np.ndarray : Sinusoidal sequence
        """
        x_values = np.linspace(0, 4 * np.pi, length)
        return np.sin(frequency * x_values)

    def generate_fractal_sequence(self, length: int, iterations: int = 5) -> np.ndarray:
        """
        Generate a fractal-like sequence using iterative refinement.

        Parameters:
        -----------
        length : int
            Length of the sequence
        iterations : int
            Number of refinement iterations

        Returns:
        --------
        np.ndarray : Fractal sequence
        """
        sequence = np.array([1.0])

        for _ in range(iterations):
            # Refine by interpolating between points
            new_sequence = []
            for i in range(len(sequence) - 1):
                new_sequence.append(sequence[i])
                # Add interpolated point
                midpoint = (sequence[i] + sequence[i + 1]) / 2
                # Add some fractal variation
                variation = np.random.normal(0, 0.1)
                new_sequence.append(midpoint + variation)

            new_sequence.append(sequence[-1])
            sequence = np.array(new_sequence)

            # Trim to desired length
            if len(sequence) > length:
                sequence = sequence[:length]

        # Pad if necessary
        if len(sequence) < length:
            padding = np.full(length - len(sequence), sequence[-1])
            sequence = np.concatenate([sequence, padding])

        return sequence

    def generate_quantum_inspired_sequence(self, length: int) -> np.ndarray:
        """
        Generate a sequence inspired by quantum mechanical principles.

        Parameters:
        -----------
        length : int
            Length of the sequence

        Returns:
        --------
        np.ndarray : Quantum-inspired sequence
        """
        # Simulate quantum harmonic oscillator energy levels
        n_values = np.arange(length)
        energies = (n_values + 0.5) * 2 * np.pi  # ħω = 2π for simplicity

        # Add quantum fluctuations
        fluctuations = np.random.normal(0, 0.1, length)
        energies += fluctuations

        return energies

    def generate_biological_sequence(self, length: int) -> np.ndarray:
        """
        Generate a sequence inspired by biological processes.

        Parameters:
        -----------
        length : int
            Length of the sequence

        Returns:
        --------
        np.ndarray : Biology-inspired sequence
        """
        # Simulate population growth with logistic constraints
        r = 0.1  # Growth rate
        K = 100  # Carrying capacity

        population = np.zeros(length)
        population[0] = 1.0

        for i in range(1, length):
            growth = r * population[i-1] * (1 - population[i-1] / K)
            population[i] = population[i-1] + growth

            # Add stochastic variation (environmental noise)
            noise = np.random.normal(0, 0.05)
            population[i] += noise

        return population

    def _generate_primes(self, n: int) -> List[int]:
        """
        Generate first n prime numbers using Sieve of Eratosthenes.

        Parameters:
        -----------
        n : int
            Number of primes to generate

        Returns:
        --------
        List[int] : List of prime numbers
        """
        if n <= 0:
            return []

        # Upper bound estimation for nth prime
        if n < 10:
            upper_bound = 30
        else:
            upper_bound = int(n * np.log(n) + n * np.log(np.log(n)))

        # Sieve of Eratosthenes
        sieve = [True] * (upper_bound + 1)
        sieve[0] = sieve[1] = False

        for i in range(2, int(np.sqrt(upper_bound)) + 1):
            if sieve[i]:
                for j in range(i * i, upper_bound + 1, i):
                    sieve[j] = False

        primes = [i for i, is_prime in enumerate(sieve) if is_prime]
        return primes[:n]

    def generate_validation_suite(self, sizes: List[int] = None) -> Dict[str, Any]:
        """
        Generate a complete validation suite with multiple dataset types.

        Parameters:
        -----------
        sizes : List[int], optional
            Dataset sizes to generate

        Returns:
        --------
        Dict : Complete validation suite
        """
        if sizes is None:
            sizes = [1000, 10000, 100000]

        validation_suite = {
            'metadata': {
                'description': 'Synthetic validation datasets for FHT research',
                'warning': 'These are synthetic datasets for educational purposes only',
                'generator_seed': self.seed,
                'generation_date': str(pd.Timestamp.now()),
                'license': 'Creative Commons Attribution-ShareAlike 4.0 International'
            },
            'datasets': {}
        }

        dataset_types = {
            'fibonacci': self.generate_fibonacci_sequence,
            'golden_ratio': self.generate_golden_ratio_sequence,
            'prime_modulo': self.generate_prime_modulo_sequence,
            'logarithmic': self.generate_logarithmic_sequence,
            'exponential': self.generate_exponential_sequence,
            'polynomial': lambda size: self.generate_polynomial_sequence(size, degree=3),
            'sinusoidal': self.generate_sinusoidal_sequence,
            'fractal': self.generate_fractal_sequence,
            'quantum_inspired': self.generate_quantum_inspired_sequence,
            'biological': self.generate_biological_sequence
        }

        print("🔬 Generating Synthetic Validation Suite")
        print("=" * 45)

        for dataset_name, generator_func in dataset_types.items():
            print(f"Generating {dataset_name} datasets...")
            validation_suite['datasets'][dataset_name] = {}

            for size in sizes:
                try:
                    data = generator_func(size)
                    validation_suite['datasets'][dataset_name][f'size_{size}'] = {
                        'data': data.tolist(),
                        'size': len(data),
                        'mean': float(np.mean(data)),
                        'std': float(np.std(data)),
                        'min': float(np.min(data)),
                        'max': float(np.max(data))
                    }
                    print(f"  ✓ {dataset_name} (size {size:,}): {len(data)} points")
                except Exception as e:
                    print(f"  ✗ Error generating {dataset_name} (size {size}): {e}")

        return validation_suite

    def save_validation_suite(self, suite: Dict[str, Any], filename: str = 'synthetic_validation_suite.json'):
        """
        Save the validation suite to a JSON file.

        Parameters:
        -----------
        suite : Dict
            Validation suite to save
        filename : str
            Output filename
        """
        with open(filename, 'w') as f:
            json.dump(suite, f, indent=2)

        print(f"💾 Validation suite saved to {filename}")
        print(f"   Total datasets: {len(suite['datasets'])}")
        total_points = sum(
            len(dataset_info['data'])
            for dataset_type in suite['datasets'].values()
            for dataset_info in dataset_type.values()
        )
        print(f"   Total data points: {total_points:,}")

    def export_to_csv(self, suite: Dict[str, Any], output_dir: str = 'csv_datasets'):
        """
        Export datasets to CSV files for easy analysis.

        Parameters:
        -----------
        suite : Dict
            Validation suite
        output_dir : str
            Output directory for CSV files
        """
        os.makedirs(output_dir, exist_ok=True)

        for dataset_name, datasets in suite['datasets'].items():
            for size_name, dataset_info in datasets.items():
                filename = f"{dataset_name}_{size_name}.csv"
                filepath = os.path.join(output_dir, filename)

                df = pd.DataFrame({
                    'index': range(len(dataset_info['data'])),
                    'value': dataset_info['data']
                })

                df.to_csv(filepath, index=False)
                print(f"📄 Exported {filename}")


def main():
    """
    Main execution for synthetic data generation.
    """
    print("🔬 Synthetic Data Generator for FHT Validation")
    print("=" * 50)

    # Initialize generator
    generator = SyntheticDataGenerator(seed=42)

    # Generate comprehensive validation suite
    print("\n🚀 Generating validation datasets...")
    validation_suite = generator.generate_validation_suite([1000, 10000, 50000])

    # Save to JSON
    generator.save_validation_suite(validation_suite)

    # Export to CSV for analysis
    generator.export_to_csv(validation_suite)

    # Display summary
    print("\n📊 Validation Suite Summary:")
    print("-" * 30)
    print(f"Dataset types: {len(validation_suite['datasets'])}")
    print(f"Synthetic data points: {sum(len(d['data']) for dt in validation_suite['datasets'].values() for d in dt.values()):,}")
    print(f"Generation seed: {validation_suite['metadata']['generator_seed']}")

    print("\n✅ Synthetic data generation complete!")
    print("\n⚠️  IMPORTANT: These are synthetic datasets created for")
    print("   educational and validation purposes only. They do not")
    print("   contain real research data or proprietary information.")


if __name__ == "__main__":
    main()
