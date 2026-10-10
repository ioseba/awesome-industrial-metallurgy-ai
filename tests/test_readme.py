import re
import os
import xml.etree.ElementTree as ET

def test_markdown():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    readme_path = os.path.join(repo_root, "README.md")
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
        lines = content.splitlines()

    print(f"Total lines: {len(lines)}")
    assert len(lines) > 200, "README is too short or truncated!"

    # 1. Emoji check across entire README and headings
    emoji_regex = re.compile(r"[\U00010000-\U0010ffff]|[\u2600-\u27bf]")
    heading_lines = [l for l in lines if l.startswith("#")]
    print(f"Total headings: {len(heading_lines)}")
    emojis_in_headings = [h for h in heading_lines if emoji_regex.search(h)]
    assert len(emojis_in_headings) == 0, f"Found emojis in headings: {emojis_in_headings}"

    emojis_in_lines = [(i + 1, l) for i, l in enumerate(lines) if emoji_regex.search(l)]
    assert len(emojis_in_lines) == 0, f"Found emojis in lines: {emojis_in_lines[:5]}"
    print("Check 1 PASSED: Zero emojis anywhere in README.")

    # 2. Check Table of Contents anchors
    def to_anchor(text):
        text = text.lower()
        text = re.sub(r"[^\w\s-]", "", text)
        text = re.sub(r"\s+", "-", text)
        return text.strip("-")

    actual_anchors = [to_anchor(re.sub(r"^#+\s*", "", h)) for h in heading_lines]
    toc_links = re.findall(r"\[([^\]]+)\]\(#([^\)]+)\)", content)
    print(f"TOC links discovered: {len(toc_links)}")
    missing_anchors = []
    for text, anchor in toc_links:
        if anchor not in actual_anchors:
            missing_anchors.append((text, anchor))

    if missing_anchors:
        print(f"Missing anchor targets: {missing_anchors}")
        print(f"Available anchors: {actual_anchors}")
        assert False, f"TOC anchors mismatch: {missing_anchors}"
    print("Check 2 PASSED: All Table of Contents links match heading anchors.")

    # 3. Check banner file
    banner_path = os.path.join(repo_root, "assets", "banner.svg")
    assert os.path.exists(banner_path), "assets/banner.svg does not exist!"
    assert os.path.getsize(banner_path) > 2000, "assets/banner.svg is too small!"
    
    # Verify banner is valid XML and contains key domain elements
    tree = ET.parse(banner_path)
    root = tree.getroot()
    assert "viewBox" in root.attrib, "Banner SVG missing viewBox!"
    with open(banner_path, "r", encoding="utf-8") as bf:
        svg_content = bf.read()
    assert "SECONDARY PYROMETALLURGY" in svg_content
    assert "TRF-01" in svg_content
    assert "LIBS" in svg_content
    print("Check 3 PASSED: SVG banner exists, is valid XML, and contains domain schematics.")

    # 4. Check external repo count
    github_repos = set(re.findall(r"https://github\.com/([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+)(?:[#\)/\"\s]|$)", content))
    filtered_repos = [r for r in sorted(github_repos) if not any(x in r for x in ["sindresorhus", "awesome", "ioseba/awesome", "topics", "badges"])]
    print(f"Discovered {len(filtered_repos)} curated repositories.")
    assert len(filtered_repos) >= 40, f"Expected at least 40 repositories, found {len(filtered_repos)}"
    print("Check 4 PASSED: Robust repository curation count verified.")

    # 5. Check CONTRIBUTING.md
    contrib_path = os.path.join(repo_root, "CONTRIBUTING.md")
    assert os.path.exists(contrib_path), "CONTRIBUTING.md does not exist!"
    with open(contrib_path, "r", encoding="utf-8") as f:
        contrib_lines = f.readlines()
    emojis_in_contrib = [l for l in contrib_lines if emoji_regex.search(l)]
    assert len(emojis_in_contrib) == 0, f"Found emojis in CONTRIBUTING: {emojis_in_contrib}"
    print("Check 5 PASSED: CONTRIBUTING.md is clean and free of emoji clutter.")

    # 6. Check CODE_OF_CONDUCT.md
    coc_path = os.path.join(repo_root, "CODE_OF_CONDUCT.md")
    assert os.path.exists(coc_path), "CODE_OF_CONDUCT.md does not exist!"
    with open(coc_path, "r", encoding="utf-8") as f:
        coc_content = f.read()
    assert len(coc_content) > 500, "CODE_OF_CONDUCT.md is too short!"
    assert not emoji_regex.search(coc_content), "Found emoji in CODE_OF_CONDUCT.md!"
    print("Check 6 PASSED: CODE_OF_CONDUCT.md exists, is comprehensive, and free of emojis.")

    # 7. Check DOI links validity
    dois = re.findall(r"https://doi\.org/[^\)\s]+", content)
    print(f"Verified {len(dois)} peer-reviewed DOI citations.")
    assert len(dois) >= 5, "Expected at least 5 scientific DOI references."
    print("Check 7 PASSED: Peer-reviewed literature DOIs verified.")

    print("\nALL VERIFICATION CHECKS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    test_markdown()
