# Pass Importer

This project is a simple utility for importing passwords from a CSV file into the [pass](https://www.passwordstore.org/) password manager.

## What is this?

**Pass Importer** reads a CSV file (with columns: title, login, password, notes) and inserts each entry into your [pass](https://www.passwordstore.org/) password store. If a value in the CSV is `"0"` or empty, the corresponding column name from the header is used. All columns after the third are combined into a single notes field.

> **Warning:**  
> Before running this script, make a backup of your `.password-store` directory and check your CSV file for duplicates. This script does not handle duplicates robustly.

## Requirements

- [pass](https://www.passwordstore.org/) (must be installed and initialized)
- Python 3.6+

## Installation

Clone this repository and install Python if you haven't already.

```bash
git clone https://github.com/yourusername/pass-importer.git
cd pass-importer
```