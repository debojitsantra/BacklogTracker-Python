import json

_DEFAULT_SUBJECT = {
    "backlog": 0,
    "daily_increase": 1,
    "emoji": "",
    "color": "#6750a4",
}


def _normalise_subjects(subjects: dict) -> dict:
    """Fill missing fields in each subject entry with defaults."""
    normalised = {}
    for name, sub in subjects.items():
        entry = dict(_DEFAULT_SUBJECT)  
        entry.update(sub)               
        # Enforce types
        try:
            entry["backlog"] = int(entry["backlog"])
        except (ValueError, TypeError):
            entry["backlog"] = 0
        try:
            entry["daily_increase"] = int(entry["daily_increase"])
        except (ValueError, TypeError):
            entry["daily_increase"] = 1
        normalised[name] = entry
    return normalised


def validate_and_parse_import(raw_text: str) -> dict:
    """
    Parses and validates a JSON string as either a 'course_design' or
    'full_backup' import.

    Returns:
        {
            "success": bool,
            "type": "course_design" | "full_backup" | None,
            "data": dict | None,   # parsed AppData-compatible dict
            "error": str | None
        }
    """
  
    try:
        obj = json.loads(raw_text)
    except json.JSONDecodeError as exc:
        return {
            "success": False,
            "type": None,
            "data": None,
            "error": f"Invalid JSON: {exc.msg} (line {exc.lineno}, col {exc.colno})",
        }

    if not isinstance(obj, dict):
        return {
            "success": False,
            "type": None,
            "data": None,
            "error": "Invalid JSON: top-level value must be an object.",
        }

   
    has_subjects = "subjects" in obj
    has_setup_done = "setup_done" in obj

    if not has_subjects:
        return {
            "success": False,
            "type": None,
            "data": None,
            "error": "Unrecognized format: missing required 'subjects' key.",
        }

    if has_setup_done:
        detected_type = "full_backup"
    else:
        detected_type = "course_design"

   
    raw_subjects = obj.get("subjects", {})
    if not isinstance(raw_subjects, dict):
        return {
            "success": False,
            "type": None,
            "data": None,
            "error": "Invalid format: 'subjects' must be a JSON object.",
        }

    obj["subjects"] = _normalise_subjects(raw_subjects)

    # Return success
    return {
        "success": True,
        "type": detected_type,
        "data": obj,
        "error": None,
    }
