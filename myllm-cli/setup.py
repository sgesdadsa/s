from setuptools import setup, find_packages

setup(
    name="myllm",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click>=8.1.0",
        "llama-cpp-python>=0.2.0",
        "fastapi>=0.109.0",
        "uvicorn>=0.27.0",
        "pydantic>=2.5.0",
        "rich>=13.7.0",
        "requests>=2.31.0",
        "pyyaml>=6.0.1",
        "tabulate>=0.9.0",
    ],
    entry_points={
        "console_scripts": [
            "myllm=myllm.cli:cli",
        ],
    },
    author="Your Name",
    description="CLI tool for managing and interacting with local LLM models",
    python_requires=">=3.8",
)
