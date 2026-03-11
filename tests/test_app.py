import json
import os
import sys
import time


# region agent log
def _agent_log(hypothesis_id: str, message: str, data: dict) -> None:
    log = {
        "sessionId": "90e090",
        "runId": "local-run",
        "hypothesisId": hypothesis_id,
        "location": "tests/test_app.py",
        "message": message,
        "data": data,
        "timestamp": int(time.time() * 1000),
    }
    try:
        with open("debug-90e090.log", "a", encoding="utf-8") as f:
            f.write(json.dumps(log) + "\n")
    except OSError:
        # Logging failures must not break tests
        pass


# endregion agent log


def test_app():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    _agent_log(
        "H1",
        "About to import app module",
        {
            "cwd": os.getcwd(),
            "sys_path": sys.path,
            "files_in_cwd": os.listdir("."),
        },
    )

    try:
        from ci_cd_pipeline_app.app import app  # type: ignore
    except ModuleNotFoundError as e:
        _agent_log(
            "H1",
            "Import failed with ModuleNotFoundError",
            {"error": repr(e)},
        )
        raise

    _agent_log("H1", "Import succeeded", {"app_repr": repr(app)})

    assert app is not None