from setuptools import setup, find_packages

setup(
    name="vutils",
    version="1.1.1",
    author="Vichayturen",
    author_email="vichayturen@gmail.com",
    description="vichayturen's utils",
    url="https://github.com/RankKCodeTalker/myutils",
    license="MIT",
    install_requires=[],
    extra_requires=[
        'openai',
        'torch'
    ],
    package_dir={"": "src"},
    packages=find_packages("src")
)