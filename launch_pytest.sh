#!/bin/bash
source ../venv_dojo/bin/activate
cat files_to_watch | entr -c pytest -v
