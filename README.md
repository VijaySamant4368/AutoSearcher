
# AutoSearcher

AutoSearcher is a Python script that automates web searches using a specified search engine and browser. You can provide a file of search queries or generate random queries.

## Features

- Specify the browser to use for searches.
- Provide a file containing search queries or generate random queries.
- Choose the search engine.
- Set a wait time between searches.

## Requirements

- Python 3.x
- `webbrowser` module (included in the Python Standard Library)
- `random` module (included in the Python Standard Library)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/VijaySamant4368/AutoSearcher.git
   cd AutoSearcher
   ```

2. Ensure you have Python installed on your machine.

## Usage

Run the script from the command line with the following options:

```bash
python main.py [options]
```

### Options:

- `-b <path>`: Path to the browser executable. Default is `"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"`.
- `-f <file>`: Path to a file containing queries (one per line). If not provided, use `-q` to specify the number of queries.
- `-q <number>`: Total number of random queries to generate if `-f` is not given. Default is `10`.
- `-e <engine>`: Search engine URL to use for searches. Default is `"https://www.bing.com"`.
- `-w <seconds>`: Wait time (in seconds) between subsequent searches. Default is `3`.

### Example:

```bash
python main.py -b "C:\Path\To\Browser.exe" -f queries.txt -e "https://www.google.com" -w 5
```

### Help:

To view help and usage information, run:

```bash
python main.py -h
```
Or
```bash
python main.py --help
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

## Author

Vijay Samant  
vijaysamant4368@gmail.com  
[VijaySamant4368](https://github.com/VijaySamant4368)
