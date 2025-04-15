import csv
import json
import argparse
from genson import SchemaBuilder


def generate_schema_from_csv(file_path, sample_limit=None):
    builder = SchemaBuilder()
    builder.add_schema({"type": "object", "properties": {}})

    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        # Filter out null bytes from each line
        filtered_lines = (line.replace('\x00', '') for line in f)
        reader = csv.DictReader(filtered_lines)

        for i, row in enumerate(reader):
            builder.add_object(row)
            if sample_limit and i + 1 >= sample_limit:
                break

    return builder.to_schema()


def main():
    parser = argparse.ArgumentParser(description="Generate JSON Schema from CSV file using genson.")
    parser.add_argument("csvfile", help="Path to the input CSV file")
    parser.add_argument("--limit", type=int, default=None, help="Optional: Number of rows to sample")
    parser.add_argument("--output", help="Optional: Output file path (JSON). If omitted, prints to stdout")

    args = parser.parse_args()

    schema = generate_schema_from_csv(args.csvfile, sample_limit=args.limit)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as out:
            json.dump(schema, out, indent=2)
    else:
        print(json.dumps(schema, indent=2))


if __name__ == "__main__":
    main()
