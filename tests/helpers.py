import contextlib
import io
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
OUTPUT = ROOT / "output"

if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))


def quiet(func, *args, **kwargs):
    """Wywołuje funkcję skryptu bez zaśmiecania wyniku testów jej raportem."""
    with contextlib.redirect_stdout(io.StringIO()):
        return func(*args, **kwargs)


def write_tsv(path, rows):
    Path(path).write_text("".join("\t".join(r) + "\n" for r in rows), encoding="utf-8")
    return Path(path)
