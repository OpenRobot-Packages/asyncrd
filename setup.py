import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="asyncrd",
    version="2.2.1",
    author="Alex Hutz",
    author_email="frostiitheweeb@outlook.com",
    description="A simple wrapper for Redis.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OpenRobot-Packages/asyncrd",
    project_urls={
        "Bug Tracker": "https://github.com/OpenRobot-Packages/asyncrd/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["asyncrd"],
    python_requires=">=3.7",
    install_requires=["aioconsole", "redis-protocol"],
)
