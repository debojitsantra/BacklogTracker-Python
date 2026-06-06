import json
import tkinter.filedialog as fd
import tkinter.messagebox as mb

try:
    import customtkinter as ctk
except ImportError:
    raise ImportError("customtkinter is required. Install via: pip install customtkinter")

from utils.validation import validate_and_parse_import
from theme import APP_BG, CARD_BG, SECONDARY_BG, ACCENT, ACCENT_LIGHT, TEXT_DIM, SUCCESS, DANGER



class SettingsPanel:
    """
    Modal settings dialog for the Backlog Tracker app.

    Parameters
    ----------
    parent : CTk / CTkToplevel
        The parent window.
    data : dict
        Current AppData dict (read-only reference; mutations go via callbacks).
    callbacks : dict
        Dictionary of callable hooks — see module docstring.
    """

    def __init__(self, parent, data: dict, callbacks: dict):
        self.parent = parent
        self.data = data
        self.callbacks = callbacks

        # Validation state
        self._validated_result: dict | None = None

        self._build_window()

   

    def _build_window(self):
        self.win = ctk.CTkToplevel(self.parent)
        self.win.title("Settings — Backlog Tracker")
        self.win.geometry("520x680")
        self.win.resizable(False, True)
        self.win.configure(fg_color=APP_BG)
        self.win.wait_visibility()
        self.win.grab_set()

        # Try to set icon via parent
        try:
            if hasattr(self.parent, "_current_icon_photo"):
                self.win.wm_iconphoto(True, self.parent._current_icon_photo)
        except Exception:
            pass

        scroll = ctk.CTkScrollableFrame(self.win, fg_color=APP_BG, corner_radius=0)
        scroll.pack(fill="both", expand=True, padx=0, pady=0)

        # Title
        ctk.CTkLabel(
            scroll, text="⚙️  Settings",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color="white"
        ).pack(anchor="w", padx=20, pady=(18, 2))

        ctk.CTkLabel(
            scroll, text="Manage appearance and data for your Backlog Tracker.",
            font=ctk.CTkFont(size=12),
            text_color=TEXT_DIM
        ).pack(anchor="w", padx=20, pady=(0, 14))

        self._build_appearance_section(scroll)
        self._build_data_section(scroll)

        # Close button
        ctk.CTkButton(
            scroll, text="Close", width=120, height=34, corner_radius=17,
            fg_color=SECONDARY_BG, hover_color=ACCENT, text_color="white",
            font=ctk.CTkFont(size=12, weight="bold"),
            command=self.win.destroy
        ).pack(pady=(16, 20))

    

    @staticmethod
    def _section_header(parent, text: str):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", padx=20, pady=(14, 4))
        ctk.CTkLabel(
            frame, text=text,
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=ACCENT
        ).pack(side="left")

  

    def _build_appearance_section(self, parent):
        self._section_header(parent, "🎨  Appearance")

        card = ctk.CTkFrame(parent, fg_color=CARD_BG, corner_radius=16)
        card.pack(fill="x", padx=20, pady=4)

        # Theme toggle
        theme_row = ctk.CTkFrame(card, fg_color="transparent")
        theme_row.pack(fill="x", padx=16, pady=(12, 6))
        ctk.CTkLabel(
            theme_row, text="Dark Mode",
            font=ctk.CTkFont(size=12, weight="bold"), text_color="white"
        ).pack(side="left")

        current_theme = self.data.get("theme", "dark")
        self._theme_switch = ctk.CTkSwitch(
            theme_row, text="",
            progress_color=ACCENT,
            command=self._on_theme_toggle
        )
        if current_theme == "dark":
            self._theme_switch.select()
        else:
            self._theme_switch.deselect()
        self._theme_switch.pack(side="right")

        ctk.CTkLabel(
            card, text="Theme change applies immediately.",
            font=ctk.CTkFont(size=9), text_color=TEXT_DIM
        ).pack(anchor="w", padx=16, pady=(0, 4))

        # Quotes toggle
        quotes_row = ctk.CTkFrame(card, fg_color="transparent")
        quotes_row.pack(fill="x", padx=16, pady=(6, 12))
        ctk.CTkLabel(
            quotes_row, text="Show Motivational Quotes",
            font=ctk.CTkFont(size=12, weight="bold"), text_color="white"
        ).pack(side="left")

        show_quotes = self.data.get("show_quotes", True)
        self._quotes_switch = ctk.CTkSwitch(
            quotes_row, text="",
            progress_color=ACCENT,
            command=self._on_quotes_toggle
        )
        if show_quotes:
            self._quotes_switch.select()
        else:
            self._quotes_switch.deselect()
        self._quotes_switch.pack(side="right")

    def _on_theme_toggle(self):
        theme = "dark" if self._theme_switch.get() == 1 else "light"
        self.data["theme"] = theme
        cb = self.callbacks.get("on_toggle_theme")
        if cb:
            cb(theme)

    def _on_import_text_changed(self, event=None):
        """Reset stale validation state when the user edits the import textbox."""
        if self._validated_result is not None:
            self._validated_result = None
            self._import_btn.configure(state="disabled", fg_color=SECONDARY_BG, text_color=TEXT_DIM)
            self._feedback_label.configure(text="", text_color=TEXT_DIM)
        # Must reset the Tk modified flag so future edits keep firing the event
        try:
            self._import_textbox._textbox.edit_modified(False)
        except Exception:
            pass

    def _on_quotes_toggle(self):
        # Get the current state from the switch widget
        show = self._quotes_switch.get() == 1
        self.data["show_quotes"] = show
        cb = self.callbacks.get("on_toggle_quotes")
        if cb:
            cb(show)

    #  Data Management 

    def _build_data_section(self, parent):
        self._section_header(parent, "💾  Data Management")

        card = ctk.CTkFrame(parent, fg_color=CARD_BG, corner_radius=16)
        card.pack(fill="x", padx=20, pady=4)

        # Export
        export_row = ctk.CTkFrame(card, fg_color="transparent")
        export_row.pack(fill="x", padx=16, pady=(14, 6))
        ctk.CTkLabel(
            export_row, text="Export Full Backup",
            font=ctk.CTkFont(size=12, weight="bold"), text_color="white"
        ).pack(side="left")
        ctk.CTkButton(
            export_row, text="💾 Save as JSON", width=140, height=30,
            corner_radius=15, fg_color=SECONDARY_BG, hover_color=ACCENT,
            text_color="white", font=ctk.CTkFont(size=11, weight="bold"),
            command=self.export_json
        ).pack(side="right")

        # Divider
        ctk.CTkFrame(card, fg_color=SECONDARY_BG, height=1).pack(fill="x", padx=16, pady=4)

        # Import heading
        import_heading = ctk.CTkFrame(card, fg_color="transparent")
        import_heading.pack(fill="x", padx=16, pady=(8, 4))
        ctk.CTkLabel(
            import_heading, text="Import JSON",
            font=ctk.CTkFont(size=12, weight="bold"), text_color="white"
        ).pack(side="left")
        ctk.CTkButton(
            import_heading, text="📂 Browse file…", width=120, height=28,
            corner_radius=14, fg_color=SECONDARY_BG, hover_color=ACCENT,
            text_color="white", font=ctk.CTkFont(size=10, weight="bold"),
            command=self._browse_json_file
        ).pack(side="right")

        ctk.CTkLabel(
            card, text="Paste raw JSON below or browse a .json file:",
            font=ctk.CTkFont(size=10), text_color=TEXT_DIM
        ).pack(anchor="w", padx=16, pady=(0, 4))

        # Text area
        self._import_textbox = ctk.CTkTextbox(
            card, height=140, corner_radius=10,
            fg_color=SECONDARY_BG, text_color="white",
            font=ctk.CTkFont(size=11)
        )
        self._import_textbox.pack(fill="x", padx=16, pady=(0, 8))
        # Invalidate validation result whenever the user edits the text
        self._import_textbox._textbox.bind("<<Modified>>", self._on_import_text_changed)

        # Feedback label
        self._feedback_label = ctk.CTkLabel(
            card, text="", font=ctk.CTkFont(size=11),
            text_color=TEXT_DIM, wraplength=440, justify="left"
        )
        self._feedback_label.pack(anchor="w", padx=16, pady=(0, 4))

        # Validate + Import buttons row
        btn_row = ctk.CTkFrame(card, fg_color="transparent")
        btn_row.pack(fill="x", padx=16, pady=(4, 14))

        ctk.CTkButton(
            btn_row, text="🔍 Validate", width=120, height=32,
            corner_radius=16, fg_color=SECONDARY_BG, hover_color=ACCENT,
            text_color="white", font=ctk.CTkFont(size=11, weight="bold"),
            command=self._validate_import
        ).pack(side="left", padx=(0, 8))

        self._import_btn = ctk.CTkButton(
            btn_row, text="⬆️ Import", width=120, height=32,
            corner_radius=16,
            fg_color=SECONDARY_BG, hover_color=SUCCESS,
            text_color=TEXT_DIM,
            font=ctk.CTkFont(size=11, weight="bold"),
            state="disabled",
            command=self._do_import
        )
        self._import_btn.pack(side="left")

    # export

    def export_json(self):
        filepath = fd.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json")],
            initialfile="backlog_backup.json",
            title="Save Backup"
        )
        if not filepath:
            return  # user cancelled

        try:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False)
            mb.showinfo("Export Successful", f"Backup saved to:\n{filepath}")
        except OSError as exc:
            mb.showerror("Export Failed", f"Could not write file:\n{exc}")

  

    def _browse_json_file(self):
        filepath = fd.askopenfilename(
            title="Open JSON File",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if not filepath:
            return
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            self._import_textbox.delete("1.0", "end")
            self._import_textbox.insert("1.0", content)
            # Reset validation state
            self._validated_result = None
            self._import_btn.configure(state="disabled", text_color=TEXT_DIM)
            self._feedback_label.configure(text="", text_color=TEXT_DIM)
        except OSError as exc:
            self._feedback_label.configure(
                text=f"❌ Could not read file: {exc}", text_color=DANGER
            )

    def _validate_import(self):
        raw = self._import_textbox.get("1.0", "end").strip()
        if not raw:
            self._feedback_label.configure(
                text="❌ Nothing to validate — paste JSON or browse a file.",
                text_color=DANGER
            )
            return

        result = validate_and_parse_import(raw)
        self._validated_result = result

        if result["success"]:
            label_map = {
                "full_backup":    "✅ Validation successful! Detected a Full Backup file.",
                "course_design":  "✅ Validation successful! Detected a Course Design template.",
            }
            self._feedback_label.configure(
                text=label_map.get(result["type"], "✅ Validation successful!"),
                text_color=SUCCESS
            )
            self._import_btn.configure(
                state="normal",
                fg_color=SUCCESS,
                text_color=APP_BG
            )
        else:
            self._feedback_label.configure(
                text=f"❌ {result['error']}",
                text_color=DANGER
            )
            self._import_btn.configure(state="disabled", text_color=TEXT_DIM, fg_color=SECONDARY_BG)

    def _do_import(self):
        if not self._validated_result or not self._validated_result.get("success"):
            return

        import_type = self._validated_result["type"]
        import_data = self._validated_result["data"]

        if import_type == "full_backup":
            cb = self.callbacks.get("on_import_full_backup")
            if cb:
                self.win.destroy()
                cb(import_data)
        elif import_type == "course_design":
            cb = self.callbacks.get("on_import_course_design")
            if cb:
                self.win.destroy()
                cb(import_data)
