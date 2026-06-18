"""Session state helpers for lesson progress."""

from __future__ import annotations

import streamlit as st


def init_state():
    """Initialize Streamlit session keys used across lessons."""
    defaults = {
        "completed_lessons": set(),
        "last_run_output": {},
        "last_run_error": {},
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def mark_complete(lesson_id: int):
    """Mark a lesson challenge as complete."""
    completed = set(st.session_state.get("completed_lessons", set()))
    completed.add(lesson_id)
    st.session_state.completed_lessons = completed


def is_complete(lesson_id: int) -> bool:
    """Return True when a lesson challenge has passed."""
    return lesson_id in st.session_state.get("completed_lessons", set())


def completion_count() -> int:
    """Return number of completed lessons."""
    return len(st.session_state.get("completed_lessons", set()))
