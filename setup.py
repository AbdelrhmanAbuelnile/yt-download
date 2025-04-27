from setuptools import setup, find_packages

setup(
    name="yt-download",
    version="0.1.0",
    description="A simple YouTube video and playlist downloader",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/yt-download",
    packages=find_packages(),
    install_requires=[
        "yt-dlp",
    ],
    entry_points={
        "console_scripts": [
            "yt-download=yt_download.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)