# MI Benchmarks

A Python library for generating synthetic data with known mutual information (MI) for benchmarking MI estimation methods.

## Installation
```bash
pip install mi-benchmarks
```

## Quick Start
```python
from mi_benchmarks import GaussianMIGenerator

gen = GaussianMIGenerator(dim_x=10, dim_z=8, rho=0.7, rank=5)
X, Z = gen.sample(10000)
print(f"True MI: {gen.true_mi():.4f} nats")
```

## License

MIT License
