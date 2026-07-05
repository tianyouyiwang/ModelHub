from setuptools import setup, find_packages

setup(
    name='llama',
    version='3.0.0',
    packages=find_packages(),
    install_requires=[
        'torch>=2.0.0',
        'transformers>=4.30.0',
        'fire',
        'sentencepiece',
        'pyyaml',
    ],
    extras_require={
        'dev': ['pytest', 'flake8'],
    },
    python_requires='>=3.10.0',
)