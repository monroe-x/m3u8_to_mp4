m3u8_to_mp4

一个用于将 m3u8 流媒体文件转换为 mp4 视频文件的 Python 库。该库利用多线程下载技术,显著提升了下载速度和转换效率。

## 特点

- 简单易用的 API
- 多线程下载,显著提升下载速度
- 自动处理临时文件,无需手动清理
- 支持自定义输入输出文件名和路径

## 安装

git clone或者直接下载
```
git clone https://github.com/monroe-x/m3u8_to_mp4.git
```

## 使用

```python
import m3u8_to_mp4

m3u8_to_mp4.m3u8_to_mp4('mixed.m3u8', 'ts_files', 'final_video.mp4', 'https://example.com/hls/')
```

参数说明:
- `mixed.m3u8`:m3u8 文件名,相对路径
- `ts_files`:临时文件存储目录,相对路径 
- `final_video.mp4`:导出的 mp4 文件名,相对路径
- `https://example.com/hls/`:m3u8 文件的 base URL

### 如何获取 base URL?

在浏览器中打开 m3u8 文件,查看网络请求,找到 ts 文件的网络请求 URL,去掉文件名部分,剩下的就是 base URL。

## 依赖

本库依赖 ffmpeg。请前往[官网](https://ffmpeg.org/)下载,并将 bin 目录添加到系统环境变量 PATH 中。
```
pip install requests opencv-python
```

m3u8-to-mp4

A Python library for converting m3u8 streaming media files to mp4 video files. This library utilizes multi-threading download technology to significantly improve the download speed and conversion efficiency.

## Features

- Simple and easy-to-use API
- Multi-threading download for faster download speed
- Automatically handles temporary files, no manual cleanup required
- Supports customizable input and output filenames and paths

## Installation

Git clone or download directly
```
git clone https://github.com/monroe-x/m3u8_to_mp4.git
```

## Usage

```python
import m3u8_to_mp4

m3u8_to_mp4.m3u8_to_mp4('mixed.m3u8', 'ts_files', 'final_video.mp4', 'https://example.com/hls/')
```

Parameter explanation:
- `mixed.m3u8`: m3u8 filename, relative path
- `ts_files`: temporary file storage directory, relative path
- `final_video.mp4`: exported mp4 filename, relative path 
- `https://example.com/hls/`: base URL of the m3u8 file

### How to get the base URL?

Open the m3u8 file in a browser, check the network requests, find the network request URL of the ts files, remove the filename part, and the rest is the base URL.

## Dependency

This library depends on ffmpeg. Please go to the [official website](https://ffmpeg.org/) to download and add the bin directory to the system environment variable PATH.
```
pip install requests opencv-python
```
