import subprocess
from pathlib import Path

THIS_DIR = Path(__file__).parent
PROJECT_DIR = THIS_DIR / "../"

def test__can_generate_project():
    """
    execute: 'cookoecutter <template directory> ... 
    """

    subprocess.run([
        "cookiecutter",
        str(PROJECT_DIR),

    ])