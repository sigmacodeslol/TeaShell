# TeaShell (tsh)

A custom, lightweight shell terminal built in Python 3.12.3.

## Overview

TeaShell (tsh) is a DIY shell terminal that provides a simple, customizable command-line interface similar to PowerShell (pwsh). Built from scratch with Python, TeaShell offers features such as command aliasing.
This is a personal project and not affiliated with any organizations or individuals.

## Installation

```bash
# Clone the repository
git clone https://github.com/sigmacodeslol/TeaShell
cd teashell

# Install dependencies
pip install -r requirements.txt

# Run TeaShell
python tsh.py
```

## Features

- Available commands from different terminals
- Custom pipe operator for command chaining
- Inline command editing
- Custom command syntax
- Cross-platform compatibility

## Usage

```
$ tsh
TeaShell v[0.1] > cls
```

### Basic Commands

- `help` - Display available commands
- `exit` - Exit the shell
- `cls` - Clear the shell display
- `cd` - Change directory
- `touch` - Create a new file

## Configuration

TeaShell can be configured by editing the `config.yaml` file in the installation directory:

```yaml
# Example configuration
prompt: "tsh$ "
history_size: 100
```

## Development

TeaShell is developed using:

- Python 3.12.3
- [Key libraries/dependencies]
- Development environments: Neovim (primary), Trae AI code editor (occasional)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see below for details:

MIT License

Copyright (c) 2025 Torrez Tsoi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Acknowledgments

- I was inspired by the Shell section in [Build Your Own X](https://github.com/codecrafters-io/build-your-own-x) because I always wanted to build my own shell but after weeks, all I could do is just implement simple tools like math functions and tools I could use but I have to go to my shell directory + run my self-coded project that I haven't paid much attention to lately.

## Notes

- I will add the functionality of files and folders soon in the future, probably after the version 1.0.0 official release.