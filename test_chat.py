"""The interactive CLI must never replace another session's transcript."""
import sys
import tempfile
import unittest
from contextlib import redirect_stderr
from io import StringIO
from pathlib import Path
from unittest.mock import patch

import chat


class ChatTranscriptTests(unittest.TestCase):
    def test_path_claimed_during_model_load_is_preserved(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "chat.json"

            def competing_session(_):
                path.write_text("first session", encoding="utf-8")
                return object(), {}, {}

            args = ["chat.py", "--model", "fixture.pt", "--transcript", str(path)]
            with patch.object(sys, "argv", args), patch.object(chat, "load_model", competing_session), \
                    patch.object(chat, "model_hash", return_value="fixture"), redirect_stderr(StringIO()), \
                    self.assertRaises(SystemExit) as stopped:
                chat.main()
            self.assertEqual(stopped.exception.code, 2)
            self.assertEqual(path.read_text(encoding="utf-8"), "first session")
