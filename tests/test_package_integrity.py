"""Structural checks on the package.

Catches the class of mistake that ships fine to git but breaks at install
time: a resource path that points at a folder name Package Control will
never create, or a JSON file that does not parse.
"""

import json
import os
import re
import struct

from tests.helpers import REPO_ROOT, Checker

PACKAGE_NAME = "PolyOS-Edi-for-Sublime-Text"
PACKAGE_PREFIX = "Packages/" + PACKAGE_NAME + "/"

# layer#.texture paths are resolved relative to Packages/ by the package's own
# installed name, which repository.json sets to "PolyOS Editor" (see README:
# the repo folder name would resolve to a directory that never exists).
TEXTURE_PREFIX = "PolyOS Editor/"

# Sublime ships these, so a reference to them is correct even though they are
# not part of this package.
STOCK_PREFIXES = ("Packages/User/", "Packages/Text/", "Packages/Default/",
                  "Packages/Color Scheme - Default", "Packages/Theme - ")

TEXT_RESOURCES = (
    ".sublime-settings",
    ".sublime-color-scheme",
    ".sublime-theme",
    ".sublime-keymap",
    ".sublime-menu",
    ".sublime-commands",
)

# Strict JSON. Sublime tolerates trailing commas and comments, but a plain
# json.load catches a genuinely broken file, and Sublime's own parser is the
# authority on anything more lenient.
PLAIN_JSON = ("repository.json", "PolyMark.sublime-commands",
              "PolyOS Editor.sublime-menu")


def strip_jsonc(text):
    """Strip // line comments and /* */ blocks, then any trailing commas.

    Sublime's parser accepts both, so a strict json.loads would report
    perfectly valid files as broken.
    """
    out = []
    i = 0
    n = len(text)
    while i < n:
        ch = text[i]
        if ch == '"':
            # Copy the string literal verbatim, honouring escapes.
            out.append(ch)
            i += 1
            while i < n:
                out.append(text[i])
                if text[i] == "\\" and i + 1 < n:
                    out.append(text[i + 1])
                    i += 2
                    continue
                if text[i] == '"':
                    i += 1
                    break
                i += 1
            continue
        if ch == "/" and i + 1 < n and text[i + 1] == "/":
            while i < n and text[i] != "\n":
                i += 1
            continue
        if ch == "/" and i + 1 < n and text[i + 1] == "*":
            i += 2
            while i + 1 < n and not (text[i] == "*" and text[i + 1] == "/"):
                i += 1
            i += 2
            continue
        out.append(ch)
        i += 1
    stripped = "".join(out)
    # Remove trailing commas before } or ].
    return re.sub(r",(\s*[}\]])", r"\1", stripped)


# Directories that hold development material rather than shipped package files.
NON_PACKAGE_DIRS = (".git", "__pycache__", "tests")


def read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as handle:
        return handle.read()


def test_package_name_matches_repo(c):
    print("package name matches the repo folder")
    # Package Control names the installed folder after the repo, so every
    # Packages/<name>/ reference has to match that name exactly.
    references = set()
    for dirpath, dirnames, filenames in os.walk(REPO_ROOT):
        dirnames[:] = [d for d in dirnames if d not in NON_PACKAGE_DIRS]
        for filename in filenames:
            # Prose is not loaded by Sublime; a Packages/... path in the
            # README is documentation, not a resource reference.
            if filename.endswith((":Zone.Identifier", ".png", ".pyc", ".md")):
                continue
            path = os.path.join(dirpath, filename)
            with open(path, encoding="utf-8", errors="replace") as handle:
                references |= set(re.findall(r"Packages/[A-Za-z0-9._-]+/", handle.read()))

    ours = {r for r in references if r.startswith("Packages/")
            and not r.startswith(STOCK_PREFIXES)}
    c.check("all package refs use %s/" % PACKAGE_NAME,
            ours == {PACKAGE_PREFIX})

    stale = {r for r in references if "PolyMark/" in r or "polymark/" in r}
    c.check("no refs to the old packages/ layout", not stale)


def test_resource_paths_resolve(c):
    print("package-relative resource paths resolve")
    missing = []
    checked = set()
    for dirpath, dirnames, filenames in os.walk(REPO_ROOT):
        dirnames[:] = [d for d in dirnames if d not in NON_PACKAGE_DIRS]
        for filename in filenames:
            # Prose is never loaded by Sublime, and an ellipsis in the README
            # is an example rather than a path to resolve.
            if filename.endswith((":Zone.Identifier", ".md")):
                continue
            path = os.path.join(dirpath, filename)
            try:
                text = open(path, encoding="utf-8").read()
            except (UnicodeDecodeError, ValueError):
                continue
            for ref in re.findall(
                    re.escape(PACKAGE_PREFIX) + r"([^\"'\\\s)…)]+)", text):
                    checked.add(ref)
                    if not os.path.exists(os.path.join(REPO_ROOT, ref)):
                        missing.append(ref)

    c.check("%d distinct references checked" % len(checked), True)
    for ref in sorted(missing):
        c.check("resolves: %s" % ref, False)
    if not missing:
        c.check("every reference resolves", True)


def test_theme_textures_resolve(c):
    print("theme textures resolve")
    theme = read("PolyOS Editor Dark.sublime-theme")
    # No Packages/ prefix here: Sublime rejects it for layer0.texture.
    textures = set(re.findall(r'"' + TEXTURE_PREFIX + r'assets/[^"]+"', theme))
    # The reference already carries the package name; the path is relative to
    # the repo root, so drop it before joining.
    missing = [t.strip('"') for t in textures
               if not os.path.exists(os.path.join(REPO_ROOT, t.strip('"')[len(TEXTURE_PREFIX):]))]
    c.check("%d unique textures referenced" % len(textures), len(textures) > 0)
    for ref in missing:
        c.check("texture exists: %s" % ref, False)
    if not missing:
        c.check("every texture exists", True)


def png_chunks(path):
    """Return the ordered list of chunk type codes in a PNG file."""
    with open(path, "rb") as handle:
        data = handle.read()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("%s: not a PNG" % path)
    types = []
    pos = 8
    while pos + 8 <= len(data):
        length = struct.unpack(">I", data[pos:pos + 4])[0]
        types.append(data[pos + 4:pos + 8].decode("latin1"))
        pos += 12 + length
    return types


def png_size(path):
    with open(path, "rb") as handle:
        header = handle.read(24)
    if header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("%s: not a PNG" % path)
    # signature (8) + length (4) + "IHDR" (4), then width, height.
    return struct.unpack(">II", header[16:24])


def test_pngs_are_plain_srgb(c):
    print("textures are plain sRGB PNGs")
    # Colour-management chunks (iCCP profiles, chromaticity, gamma, pHYs,
    # text) are interpreted differently by Sublime's OpenGL path and the
    # software renderer, so they shift hues between drivers: the green
    # indicators in this theme read as yellow/orange/red on affected
    # machines. Ship only IHDR/PLTE/IDAT/IEND so raw sRGB is assumed
    # everywhere.
    allowed = {"IHDR", "PLTE", "IDAT", "IEND"}
    found = 0
    problems = []
    for dirpath, dirnames, filenames in os.walk(os.path.join(REPO_ROOT, "assets")):
        dirnames[:] = [d for d in dirnames if d not in NON_PACKAGE_DIRS]
        for filename in sorted(filenames):
            if not filename.endswith(".png"):
                continue
            found += 1
            path = os.path.join(dirpath, filename)
            try:
                extra = [t for t in png_chunks(path) if t not in allowed]
            except ValueError as exc:
                problems.append(str(exc))
                continue
            if extra:
                problems.append("%s: %s" % (
                    os.path.relpath(path, REPO_ROOT), ", ".join(sorted(set(extra)))))
    c.check("%d texture files found" % found, found > 0)
    for problem in problems:
        c.check("plain sRGB: %s" % problem, False)
    if not problems:
        c.check("every texture is a plain IHDR/IDAT/IEND PNG", True)


def test_texture_inner_margins_fit(c):
    print("texture inner margins fit their images")
    # An inner_margin wider than the image makes Sublime stretch edge pixels
    # that do not exist, producing stray bands down the sides of tabs,
    # scrollbars and sidebar rows.
    problems = []
    checked = 0
    for dirpath, dirnames, filenames in os.walk(REPO_ROOT):
        dirnames[:] = [d for d in dirnames if d not in NON_PACKAGE_DIRS]
        for filename in sorted(filenames):
            if not filename.endswith(".sublime-theme") or filename.endswith(":Zone.Identifier"):
                continue
            path = os.path.join(dirpath, filename)
            try:
                rules = json.loads(strip_jsonc(open(path, encoding="utf-8").read()))
            except json.JSONDecodeError as exc:
                problems.append("%s: %s" % (filename, exc))
                continue
            for rule in walk_dicts(rules):
                for key, value in rule.items():
                    if not key.endswith(".texture") or not isinstance(value, str):
                        continue
                    if not value.startswith(TEXTURE_PREFIX):
                        continue
                    rel = value[len(TEXTURE_PREFIX):]
                    texture = os.path.join(REPO_ROOT, rel)
                    margin = rule.get(key[:key.index(".")] + ".inner_margin", 0)
                    checked += 1
                    try:
                        width, height = png_size(texture)
                    except (OSError, ValueError) as exc:
                        problems.append("%s: %s" % (value, exc))
                        continue
                    bad = margin_too_wide(margin, width, height)
                    if bad:
                        problems.append("%s: margin %s exceeds %dx%d %s"
                                        % (value, margin, width, height, bad))
    c.check("%d texture/margin pairs checked" % checked, checked > 0)
    for problem in problems:
        c.check("fits: %s" % problem, False)
    if not problems:
        c.check("every inner_margin fits inside its texture", True)


def walk_dicts(node):
    """Yield every dict nested inside a decoded theme."""
    if isinstance(node, dict):
        yield node
        for value in node.values():
            for found in walk_dicts(value):
                yield found
    elif isinstance(node, list):
        for value in node:
            for found in walk_dicts(value):
                yield found


def margin_too_wide(margin, width, height):
    """Return a description if margin eats more pixels than the image has."""
    if not isinstance(margin, list):
        return ""  # scalar 0 (or a percentage) is never geometrically wrong
    if len(margin) == 2:
        h, v = margin
        left, top, right, bottom = h, v, h, v
    elif len(margin) == 4:
        left, top, right, bottom = margin
    else:
        return "has %d entries" % len(margin)
    if left + right > width:
        return "(horizontal %d > %d)" % (left + right, width)
    if top + bottom > height:
        return "(vertical %d > %d)" % (top + bottom, height)
    return ""


def test_json_parses(c):
    print("JSON resources parse")
    for rel in PLAIN_JSON:
        try:
            json.loads(read(rel))
            c.check("parses: %s" % rel, True)
        except json.JSONDecodeError as exc:
            c.check("parses: %s (%s)" % (rel, exc), False)


def test_settings_parses(c):
    print("settings resources parse as JSON")
    # These carry // comments, so strip them the way Sublime does.
    bad = []
    found = 0
    for dirpath, dirnames, filenames in os.walk(REPO_ROOT):
        dirnames[:] = [d for d in dirnames if d not in NON_PACKAGE_DIRS]
        for filename in filenames:
            if not filename.endswith(".sublime-settings"):
                continue
            if filename.endswith(":Zone.Identifier"):
                continue
            found += 1
            path = os.path.join(dirpath, filename)
            text = open(path, encoding="utf-8").read()
            try:
                json.loads(strip_jsonc(text))
            except json.JSONDecodeError as exc:
                bad.append((os.path.relpath(path, REPO_ROOT), str(exc)))

    c.check("%d settings files found" % found, True)
    for rel, err in bad:
        c.check("parses: %s (%s)" % (rel, err), False)
    if not bad:
        c.check("every settings file parses", True)


def test_theme_colours_parse(c):
    print("theme and colour scheme resources parse")
    bad = []
    found = 0
    for dirpath, dirnames, filenames in os.walk(REPO_ROOT):
        dirnames[:] = [d for d in dirnames if d not in NON_PACKAGE_DIRS]
        for filename in filenames:
            if not filename.endswith((".sublime-theme", ".sublime-color-scheme")):
                continue
            if filename.endswith(":Zone.Identifier"):
                continue
            found += 1
            path = os.path.join(dirpath, filename)
            text = open(path, encoding="utf-8").read()
            try:
                json.loads(strip_jsonc(text))
            except json.JSONDecodeError as exc:
                bad.append((os.path.relpath(path, REPO_ROOT), str(exc)))

    c.check("%d colour resources found" % found, True)
    for rel, err in bad:
        c.check("parses: %s (%s)" % (rel, err), False)
    if not bad:
        c.check("every colour resource parses", True)


def test_syntax_yaml(c):
    print("syntax definition parses as YAML")
    try:
        import yaml
    except ImportError:
        print("  SKIP  PyYAML not installed")
        return
    try:
        data = yaml.safe_load(read("polymark.sublime-syntax"))
        c.check("parses, %d contexts" % len(data.get("contexts", [])), True)
    except yaml.YAMLError as exc:
        c.check("parses (%s)" % exc, False)


def test_python_parses(c):
    print("plugin sources parse")
    import ast
    for filename in ("activate_profile.py", "prose_toggles.py", "color_schemes.py"):
        try:
            ast.parse(read(filename), filename)
            c.check("parses: %s" % filename, True)
        except SyntaxError as exc:
            c.check("parses: %s (%s)" % (filename, exc), False)


def test_menu_commands_are_defined(c):
    print("menu commands map to plugin classes")
    # Sublime derives polyos_editor_foo_bar from PolyosEditorFooBarCommand, so
    # compare derived names against the class names actually defined.
    sources = (read("activate_profile.py") + read("prose_toggles.py")
               + read("color_schemes.py"))
    defined = set()
    for match in re.finditer(r"class\s+(\w+?)Command\b", sources):
        name = match.group(1)
        defined.add(re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower())

    referenced = set()

    def walk(node):
        if isinstance(node, dict):
            if isinstance(node.get("command"), str):
                referenced.add(node["command"])
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)

    try:
        walk(json.loads(read("PolyOS Editor.sublime-menu")))
    except json.JSONDecodeError:
        pass

    for command in sorted(referenced):
        c.check("defined: %s" % command, command in defined)


def test_visible_profile_keys_absent_from_defaults(c):
    print("visible keys are not shipped as defaults")
    # If these were in Preferences.sublime-settings, installing would change
    # someone's editor before they were asked.
    defaults = json.loads(strip_jsonc(read("Preferences.sublime-settings")))
    profile_keys = {"theme", "color_scheme", "default_syntax", "font_size"}
    leaked = sorted(profile_keys & set(defaults))
    c.check("no profile keys in shipped defaults", not leaked)
    if leaked:
        print("        leaked: %s" % ", ".join(leaked))


def main():
    c = Checker()
    for test in (
        test_package_name_matches_repo,
        test_resource_paths_resolve,
        test_theme_textures_resolve,
        test_pngs_are_plain_srgb,
        test_texture_inner_margins_fit,
        test_json_parses,
        test_settings_parses,
        test_theme_colours_parse,
        test_syntax_yaml,
        test_python_parses,
        test_menu_commands_are_defined,
        test_visible_profile_keys_absent_from_defaults,
    ):
        test(c)
    return 0 if c.report("package structure") else 1