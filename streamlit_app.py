"""Extract the bundled, reviewable release and start its hosted entrypoint."""
from pathlib import Path
import hashlib, os, runpy, sys, tempfile, zipfile
archive = Path(__file__).with_name("crashzero_source.zip")
digest = hashlib.sha256(archive.read_bytes()).hexdigest()[:16]
root = Path(tempfile.gettempdir()) / ("crashzero-" + digest)
if not (root / ".ready").exists():
    root.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive) as bundle:
        for item in bundle.infolist():
            destination = (root / item.filename).resolve()
            if not destination.is_relative_to(root.resolve()):
                raise ValueError("Invalid release archive path")
        bundle.extractall(root)
    (root / ".ready").touch()
sys.path.insert(0, str(root))
os.environ["CRASHZERO_HOSTED"] = "1"
runpy.run_path(str(root / "app.py"), run_name="__main__")
