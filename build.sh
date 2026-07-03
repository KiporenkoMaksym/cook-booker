#!/usr/bin/env bash
# Exit on error
set -o errexit

# 1. Modify this line as needed for your package manager(pip, poetry, etc.)
pip install -r requirements.txt

# 2. Convert static asset files
python manage.py collectstatic --no-input

# 3. Apply any outstanding database migrations
python manage.py migrate