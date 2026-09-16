import pytest

from app.ingestion.markdown import load_markdown


def test_load_markdown(tmp_path):
    markdown_file = tmp_path / "example.md"
    markdown_file.write_text(
        "# Authentication\n\nDevBrain uses token-based authentication.",
        encoding="utf-8",
    )

    document = load_markdown(markdown_file)

    assert document.content == (
        "# Authentication\n\nDevBrain uses token-based authentication."
    )
    assert document.source == str(markdown_file)
    assert document.document_type == "markdown"
    assert document.metadata["filename"] == "example.md"


def test_load_markdown_rejects_non_markdown_file(tmp_path):
    text_file = tmp_path / "example.txt"
    text_file.write_text("Some content", encoding="utf-8")

    with pytest.raises(ValueError, match="File must be a Markdown file"):
        load_markdown(text_file)
