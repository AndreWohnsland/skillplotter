import matplotlib as mpl
import pytest

from skill_plotter import preparator

mpl.use("Agg")


@pytest.fixture(autouse=True)
def isolated_app_dir(tmp_path, monkeypatch):
    """Point the skill storage to a temp dir so tests never touch real user data."""
    monkeypatch.setattr(preparator, "_app_dir", tmp_path / "appdir")
