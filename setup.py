import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="world",
    version="1.0",
    description="Give information about different countries",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Mabubakr86/World",
    author="mabubakr",
    author_email="dev.mabubakr@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["world"],
    include_package_data=True,
    install_requires=["pandas"],
    entry_points={
        "console_scripts": [
            "world=world.__main__:main",
        ]
    },
)
