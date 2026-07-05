from setuptools import setup, find_packages

setup(
    name='accelerate',
    version='0.28.0',
    packages=find_packages(),
    install_requires=[
        'torch>=1.10.0',
        'numpy',
        'packaging>=20.0',
        'huggingface-hub>=0.21.0',
    ],
    extras_require={
        'dev': ['pytest', 'pytest-xdist', 'psutil', 'black~=23.1', 'ruff>=0.0.241'],
        'quality': ['black~=23.1', 'ruff>=0.0.241'],
        'docs': ['hf-doc-builder', 'hf-doc-builder[cli]'],
    },
    python_requires='>=3.8.0',
)