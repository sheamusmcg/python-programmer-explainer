"""Reusable Streamlit UI helpers for the Python Programmer Explainer."""

from __future__ import annotations

import streamlit as st

from components.code_runner import check_user_code, run_user_code
from components.lesson_data import LESSONS, get_next_lesson, get_previous_lesson
from components.state_manager import completion_count, init_state, is_complete, mark_complete


def apply_global_styles():
    """Apply small layout refinements."""
    st.markdown(
        """
        <style>
        .lesson-meta {
            color: #5f6368;
            font-size: 0.95rem;
            margin-bottom: 1rem;
        }
        .code-output {
            border-left: 4px solid #3b82f6;
            padding-left: 0.75rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_progress_sidebar(current_lesson_id: int):
    """Render lesson progress in the sidebar."""
    with st.sidebar:
        st.header("Progress")
        completed = completion_count()
        total = len(LESSONS)
        st.progress(completed / total)
        st.caption(f"{completed} of {total} challenges complete")

        st.divider()
        st.subheader("Lessons")
        for lesson in LESSONS:
            icon = ":material/check_circle:" if is_complete(lesson["id"]) else lesson["icon"]
            label = lesson["short_title"]
            if lesson["id"] == current_lesson_id:
                label = f"{label} - current"
            st.page_link(lesson["page"], label=label, icon=icon)


def _show_run_result(result):
    """Render captured output and errors."""
    if result.output.strip():
        st.code(result.output.rstrip(), language="text")
    else:
        st.caption("No output printed.")

    if result.error:
        st.error(result.error)


def _render_deep_dive(lesson: dict):
    """Render Colab and notebook extension activities."""
    st.subheader("Deep Dive Notebook")
    st.write(
        f"Use the original notebook, `{lesson['source_notebook']}`, when you want a longer lab "
        "with more cells to edit and rerun."
    )
    st.link_button("Open in Google Colab", lesson["colab_url"], use_container_width=True)

    with st.expander("Suggested notebook moves"):
        for item in lesson["deep_dive"]:
            st.markdown(f"- {item}")


def _render_navigation(lesson: dict):
    """Render previous and next page links."""
    previous_lesson = get_previous_lesson(lesson["id"])
    next_lesson = get_next_lesson(lesson["id"])

    st.divider()
    left, right = st.columns(2)
    with left:
        if previous_lesson:
            st.page_link(
                previous_lesson["page"],
                label=f"Back: {previous_lesson['short_title']}",
                icon=":material/arrow_back:",
            )
    with right:
        if next_lesson:
            st.page_link(
                next_lesson["page"],
                label=f"Next: {next_lesson['short_title']}",
                icon=":material/arrow_forward:",
            )
        else:
            st.success("You reached the end of the ten-lesson path.")


def render_lesson(lesson: dict):
    """Render a complete lesson page."""
    init_state()
    apply_global_styles()
    render_progress_sidebar(lesson["id"])

    status = "Complete" if is_complete(lesson["id"]) else "Practice challenge not complete yet"
    st.title(lesson["title"])
    st.markdown(
        f"<div class='lesson-meta'>Lesson {lesson['id']} of {len(LESSONS)} - {status}</div>",
        unsafe_allow_html=True,
    )
    st.write(lesson["objective"])

    st.header("Lesson Brief")
    why_col, summary_col = st.columns(2)
    with why_col:
        st.subheader("Why this matters")
        st.write(lesson["why_it_matters"])
    with summary_col:
        st.subheader("Notebook summary")
        st.write(lesson["notebook_summary"])

    with st.expander("Key topics from the notebook", expanded=True):
        for topic in lesson["key_topics"]:
            st.markdown(f"- {topic}")

    overview_col, notebook_col = st.columns([2, 1])
    with overview_col:
        with st.expander("Concept", expanded=True):
            st.write(lesson["concept"])
        with st.expander("Mental model", expanded=True):
            st.write(lesson["mental_model"])
    with notebook_col:
        st.link_button("Open Colab Deep Dive", lesson["colab_url"], use_container_width=True)
        st.caption(lesson["source_notebook"])

    st.header("Example")
    st.subheader(lesson["example_title"])
    st.code(lesson["example_code"], language="python")

    if st.button("Run example", key=f"run_example_{lesson['id']}"):
        _show_run_result(run_user_code(lesson["example_code"]))

    with st.expander("Walk through the example", expanded=True):
        for item in lesson["walkthrough"]:
            st.markdown(f"- {item}")

    challenge = lesson["challenge"]
    st.header("Try It")
    st.subheader(challenge["title"])
    st.write(challenge["prompt"])

    code_key = f"lesson_{lesson['id']}_code"
    user_code = st.text_area(
        "Code editor",
        value=challenge["starter_code"],
        height=260,
        key=code_key,
        label_visibility="collapsed",
    )

    run_col, check_col = st.columns(2)
    with run_col:
        run_clicked = st.button("Run my code", key=f"run_user_{lesson['id']}", use_container_width=True)
    with check_col:
        check_clicked = st.button("Check challenge", key=f"check_user_{lesson['id']}", use_container_width=True)

    if run_clicked:
        result = run_user_code(user_code)
        st.subheader("Output")
        _show_run_result(result)

    if check_clicked:
        result = check_user_code(user_code, challenge["checks"])
        st.subheader("Check Results")
        if result.passed:
            mark_complete(lesson["id"])
            st.success("Challenge passed.")
        else:
            st.warning("Not quite yet. Read the messages and try another edit.")

        if result.run.output.strip() or result.run.error:
            st.caption("Program output")
            _show_run_result(result.run)

        with st.expander("Validation messages", expanded=True):
            for message in result.messages:
                st.markdown(f"- {message}")

    with st.expander("Hints"):
        for index, hint in enumerate(challenge["hints"], start=1):
            st.markdown(f"{index}. {hint}")

    with st.expander("Show one possible solution"):
        st.code(challenge["solution"], language="python")

    _render_deep_dive(lesson)
    _render_navigation(lesson)
