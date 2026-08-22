from typer.testing import CliRunner

from skill_plotter.main import app

runner = CliRunner()


def test_add_and_list_skill():
    result = runner.invoke(app, ["add", "Python", "9"])
    assert result.exit_code == 0
    result = runner.invoke(app, ["list-skills"])
    assert result.exit_code == 0
    assert "Python" in result.output


def test_add_invalid_level_fails():
    result = runner.invoke(app, ["add", "Python", "11"])
    assert result.exit_code == 1


def test_remove_skill():
    runner.invoke(app, ["add", "Python", "9"])
    result = runner.invoke(app, ["remove", "Python"])
    assert result.exit_code == 0
    result = runner.invoke(app, ["list-skills"])
    assert result.exit_code == 1


def test_remove_missing_skill_fails():
    result = runner.invoke(app, ["remove", "Nope"])
    assert result.exit_code == 1


def test_plot_generates_file(tmp_path):
    runner.invoke(app, ["add", "Python", "9"])
    runner.invoke(app, ["add", "Docker", "7"])
    out = tmp_path / "skills"
    result = runner.invoke(app, ["--file-name", str(out), "--file-type", "svg"])
    assert result.exit_code == 0
    assert (tmp_path / "skills.svg").stat().st_size > 0


def test_plot_missing_group_fails():
    result = runner.invoke(app, ["--skill-group", "does-not-exist"])
    assert result.exit_code == 1


def test_export_import_roundtrip(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    runner.invoke(app, ["add", "Python", "9"])
    result = runner.invoke(app, ["export-skills", "backup"])
    assert result.exit_code == 0
    result = runner.invoke(app, ["import-skills", "backup.json", "--skill-group", "other"])
    assert result.exit_code == 0
    result = runner.invoke(app, ["list-skills", "--skill-group", "other"])
    assert "Python" in result.output


def test_import_invalid_file_fails(tmp_path):
    bad = tmp_path / "bad.json"
    bad.write_text('{"Python": {"level": 99}}')
    result = runner.invoke(app, ["import-skills", str(bad)])
    assert result.exit_code == 1
