# CSV to JSON Schema Generator

This Python script generates a [JSON Schema](https://json-schema.org/) from a CSV file using the genson library.

## Requirements

- Python 3.6+
- All dependencies listed in requirements.txt

Install dependencies with:

```
pip3 install -r requirements.txt
```

## Usage

```
python3 index.py path/to/your.csv
```

### Optional Arguments

- `--limit`: Number of rows to sample (helps with large files)

- `--output`: Output path to save the schema as a `.json` file

### Examples

Generate a schema from `data.csv` and print it to the console:

```
python3 index.py data.csv
```

Generate a schema using only the first 100 rows:

```
python3 index.py data.csv --limit 100
```

Generate a schema and write it to schema.json:

```
python3 index.py data.csv --output schema.json
```

## Notes

- The script handles CSVs that contain null bytes (\x00), which can otherwise crash readers.
- Fields are inferred as objects with appropriate types (string, number, boolean, etc.) based on the CSV content.

## License

MIT License
