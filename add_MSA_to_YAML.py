#!/usr/bin/env python3
import sys
from pathlib import Path
import yaml

if __name__ == "__main__":
    input_yaml = Path(sys.argv[1]).resolve()
    msa_csv = Path(sys.argv[2]).resolve()
    output_yaml = Path(sys.argv[3]).resolve()

    if not input_yaml.is_file():
        sys.exit(f"Error: input YAML not found: {input_yaml}")
    if not msa_csv.is_file():
        sys.exit(f"Error: MSA CSV not found: {msa_csv}")

    with input_yaml.open("r") as f:
        data = yaml.safe_load(f)

    if not isinstance(data, dict) or "sequences" not in data:
        sys.exit("Error: YAML has no top-level 'sequences' key.")

    msa_path_str = str(msa_csv)
    n_added = 0

    for entry in data["sequences"]:
        if not isinstance(entry, dict):
            continue
        for entity_type, body in entry.items():
            if entity_type == "protein" and isinstance(body, dict):
                body["msa"] = msa_path_str
                n_added += 1

    if n_added == 0:
        print("Warning: no protein entries found; YAML written unchanged.",
              file=sys.stderr)
        
    output_yaml.parent.mkdir(parents=True, exist_ok=True)
    with output_yaml.open("w") as f:
        yaml.safe_dump(data, f, sort_keys=False, default_flow_style=False)

    print(f"Added MSA to {n_added} protein entr{'y' if n_added == 1 else 'ies'}.")
    print(f"Wrote: {output_yaml}")