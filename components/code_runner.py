"""Small code execution helper for beginner practice cells."""

from __future__ import annotations

from contextlib import contextmanager, redirect_stderr, redirect_stdout
from dataclasses import dataclass
from io import StringIO
import builtins
import math
import signal
import statistics
import json
import random


ALLOWED_MODULES = {
    "json": json,
    "math": math,
    "random": random,
    "statistics": statistics,
}

TYPE_MAP = {
    "bool": bool,
    "dict": dict,
    "float": float,
    "int": int,
    "list": list,
    "set": set,
    "str": str,
    "tuple": tuple,
}


class ExecutionTimeout(Exception):
    """Raised when learner code runs for too long."""


@dataclass
class RunResult:
    """Result returned by the code runner."""

    output: str
    error: str | None
    namespace: dict


@dataclass
class CheckResult:
    """Result returned by challenge validation."""

    passed: bool
    messages: list[str]
    run: RunResult


def _safe_import(name, globals=None, locals=None, fromlist=(), level=0):
    """Allow imports for a small set of teaching-friendly standard modules."""
    root_name = name.split(".")[0]
    if root_name not in ALLOWED_MODULES:
        raise ImportError(f"Importing '{name}' is not allowed in this practice runner.")
    return builtins.__import__(name, globals, locals, fromlist, level)


def _safe_builtins() -> dict:
    """Return the built-ins exposed to learner code."""
    names = [
        "abs",
        "all",
        "any",
        "bool",
        "dict",
        "enumerate",
        "float",
        "int",
        "isinstance",
        "len",
        "list",
        "max",
        "min",
        "object",
        "print",
        "range",
        "round",
        "set",
        "sorted",
        "str",
        "sum",
        "tuple",
        "type",
        "zip",
        "Exception",
        "ValueError",
        "ZeroDivisionError",
    ]
    safe = {name: getattr(builtins, name) for name in names}
    safe["__build_class__"] = builtins.__build_class__
    safe["__import__"] = _safe_import
    return safe


@contextmanager
def _time_limit(seconds: int):
    """Apply a simple Unix timeout for code that may loop forever."""
    if not hasattr(signal, "SIGALRM"):
        yield
        return

    def _handler(signum, frame):
        raise ExecutionTimeout("Code ran for too long. Check for an infinite loop.")

    previous = signal.signal(signal.SIGALRM, _handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, previous)


def run_user_code(code: str, timeout_seconds: int = 3) -> RunResult:
    """Run learner code and capture stdout, stderr, errors, and names."""
    output = StringIO()
    namespace = {
        "__builtins__": _safe_builtins(),
        "__name__": "__main__",
    }

    try:
        with _time_limit(timeout_seconds):
            with redirect_stdout(output), redirect_stderr(output):
                exec(code, namespace, namespace)
    except Exception as exc:  # noqa: BLE001 - learner-facing error display
        return RunResult(output=output.getvalue(), error=f"{type(exc).__name__}: {exc}", namespace=namespace)

    return RunResult(output=output.getvalue(), error=None, namespace=namespace)


def _values_match(actual, expected) -> bool:
    """Compare values, giving floats a small amount of grace."""
    if isinstance(actual, float) and isinstance(expected, float):
        return abs(actual - expected) < 1e-9
    return actual == expected


def _evaluate_expression(expression: str, namespace: dict):
    """Evaluate an expression inside the completed learner namespace."""
    return eval(expression, namespace, namespace)


def check_user_code(code: str, checks: list[dict]) -> CheckResult:
    """Run code and validate it against lesson checks."""
    run = run_user_code(code)
    messages: list[str] = []

    if run.error:
        return CheckResult(
            passed=False,
            messages=["The code needs to run before it can be checked."],
            run=run,
        )

    for check in checks:
        check_type = check["type"]

        try:
            if check_type == "name_exists":
                name = check["name"]
                if name in run.namespace:
                    messages.append(f"Found `{name}`.")
                else:
                    messages.append(f"Missing `{name}`.")

            elif check_type == "namespace_type":
                name = check["name"]
                expected = TYPE_MAP[check["expected_type"]]
                value = run.namespace.get(name)
                if isinstance(value, expected):
                    messages.append(f"`{name}` has the right type.")
                else:
                    messages.append(f"`{name}` should be a {check['expected_type']}.")

            elif check_type == "output_contains":
                text = check["text"]
                if text in run.output:
                    messages.append(f"Output includes `{text}`.")
                else:
                    messages.append(f"Output should include `{text}`.")

            elif check_type == "expr_equals":
                actual = _evaluate_expression(check["expr"], run.namespace)
                expected = check["value"]
                if _values_match(actual, expected):
                    messages.append(f"`{check['expr']}` has the expected value.")
                else:
                    messages.append(f"`{check['expr']}` returned {actual!r}, expected {expected!r}.")

            elif check_type == "expr_close":
                actual = _evaluate_expression(check["expr"], run.namespace)
                expected = check["value"]
                tolerance = check.get("tolerance", 0.001)
                if abs(actual - expected) <= tolerance:
                    messages.append(f"`{check['expr']}` is close enough.")
                else:
                    messages.append(f"`{check['expr']}` returned {actual!r}, expected about {expected!r}.")

            elif check_type == "expr_contains":
                actual = _evaluate_expression(check["expr"], run.namespace)
                text = check["text"]
                if text in str(actual):
                    messages.append(f"`{check['expr']}` includes `{text}`.")
                else:
                    messages.append(f"`{check['expr']}` should include `{text}`.")

            else:
                messages.append(f"Unknown check type: {check_type}.")
        except Exception as exc:  # noqa: BLE001 - learner-facing check display
            messages.append(f"Could not check `{check.get('expr', check_type)}`: {type(exc).__name__}: {exc}")

    # The explicit loop above keeps messages helpful; this second pass determines pass/fail.
    failed_markers = [
        "Missing ",
        "Output should",
        " should be ",
        " returned ",
        "Could not check",
        "Unknown check type",
    ]
    passed = not any(any(message.startswith(marker) or marker in message for marker in failed_markers) for message in messages)

    return CheckResult(passed=passed, messages=messages, run=run)
