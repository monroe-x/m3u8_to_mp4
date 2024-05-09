from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="m3u8-to-mp4",
    version="0.1.0",
    author="monroe-x",
    description="一个用于将 m3u8 流媒体文件转换为 mp4 视频文件的 Python 库。该库利用多线程下载技术,显著提升了下载速度和转换效率。",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/monroe-x/m3u8_to_mp4",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests",
        "opencv-python",
    ],
)
