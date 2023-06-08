import os

from setuptools import setup, find_packages


_PATH_ROOT = os.path.dirname(__file__)

with open(os.path.join(_PATH_ROOT, "README.md"), encoding="utf-8") as fo:
    readme = fo.read()

setup(
    name='gptq-llama',
    version='0.1.0',
    description='4 bits quantization of LLaMA using GPTQ',
    author='qwopqwop200',
    url='https://github.com/qwopqwop200/GPTQ-for-LLaMa',
    install_requires=[
        "safetensors==0.3.0",
        "datasets==2.10.1",
        "sentencepiece",
        "transformers",
        "accelerate",
        "triton==2.0.0",
        "texttable==1.6.7",
        "toml==0.10.2"
    ],
    packages=find_packages("."),
    package_dir={"": "."},
    long_description=readme,
    long_description_content_type="text/markdown",
)
