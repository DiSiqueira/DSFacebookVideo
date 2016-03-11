# DSFacebookVideo ![Language Badge](https://img.shields.io/badge/Language-Python-red.svg) ![License Badge](https://img.shields.io/badge/License-MIT-blue.svg) ![Status Badge](https://img.shields.io/badge/Status-Development-red.svg)

Easily download videos from Facebook. You can use as program or as module!

![](https://i.imgur.com/Sh2TKvy.gif)

## Features

- Download Videos from Facebook
- Written in uncomplicated Python
- Easily download files in the fastest speed possible
- Download using Multi-Threaded Downloads
- Easy to [install](https://github.com/DiSiqueira/DSFacebookVideo#installation)
- Stupidly [easy to use](https://github.com/DiSiqueira/DSFacebookVideo#usage)

## Installation

### Option 1: [Pip](https://pip.pypa.io/en/stable/installing/)

```bash
$ pip install DSFacebookVideo
```

### Option 2: From source

```bash
$ git clone https://github.com/DiSiqueira/DSFacebookVideo.git
$ cd DSFacebookVideo/
$ python setup.py install
```

## Usage

### Basic usage

```bash
# Download a video
$ DSFacebookVideo https://www.facebook.com/SkySports/videos/vb.10911153761/10153310275743762
```

### Download using Workers

```bash
# Download 2 videos using 2 Workers
$ DSFacebookVideo --workers 2 https://www.facebook.com/SkySports/videos/vb.10911153761/10153310275743762 https://www.facebook.com/SkySports/videos/10153972581588762/
```

### Set output folder

```bash
# Download 1 image and put it in my-images folder
$ DSFacebookVideo --output my-videos https://www.facebook.com/SkySports/videos/10153972581588762/
```

### Combine everything

```bash
# Download 2 videos using 2 Workers and put on my-videos folder
$ DSFacebookVideo --output my-videos --workers 2 https://www.facebook.com/SkySports/videos/vb.10911153761/10153310275743762 https://www.facebook.com/SkySports/videos/10153972581588762/
```

## Module Usage
The module allows you to download url lists in your own Python programs without going through the command line. Here's an example of it's usage:

###Example
```python
from DSFacebookVideo import DSFacebookVideo

urls = ['https://www.facebook.com/SkySports/videos/vb.10911153761/10153310275743762', 'https://www.facebook.com/SkySports/videos/10153972581588762/']
workers = 2
output = 'My-Videos'

DSFacebookVideo(urls, workers, output)
```
## Requirements

* [Python](https://www.python.org)
* [DSDownload](https://github.com/DiSiqueira/DSDownload)

## Program Help

![](https://i.imgur.com/mKHbLay.png)

## Contributing

### Bug Reports & Feature Requests

Please use the [issue tracker](https://github.com/DiSiqueira/DSFacebookVideo/issues) to report any bugs or file feature requests.

### Developing

PRs are welcome. To begin developing, do this:

```bash
$ git clone --recursive git@github.com:DiSiqueira/DSFacebookVideo.git
$ cd DSFacebookVideo/src/
```

## Social Coding

1. Create an issue to discuss about your idea
2. [Fork it] (https://github.com/DiSiqueira/DSFacebookVideo/fork)
3. Create your feature branch (`git checkout -b my-new-feature`)
4. Commit your changes (`git commit -am 'Add some feature'`)
5. Push to the branch (`git push origin my-new-feature`)
6. Create a new Pull Request
7. Profit! :white_check_mark:

## License

The MIT License (MIT)

Copyright (c) 2016 Diego Siqueira

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
