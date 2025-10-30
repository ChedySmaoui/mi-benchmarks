from setuptools import setup, find_packages

setup(
    name="mi-benchmarks",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Synthetic data generation with known mutual information",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mi-benchmarks",
    packages=find_packages(exclude=["tests", "examples"]),
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.20.0",
        "torch>=1.9.0",
        "matplotlib>=3.3.0",
        "scikit-learn>=0.24.0",
    ],
    extras_require={"dev": ["pytest>=6.0", "black>=21.0"]},
)
