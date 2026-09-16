from app.ingestion.chunking import chunk_markdown
from app.ingestion.models import Document


def test_chunk_markdown_by_headings():
    document = Document(
        content=(
            "# Authentication\n\n"
            "DevBrain uses token-based authentication.\n\n"
            "## Token Validation\n\n"
            "Tokens are validated by middleware."
        ),
        source="docs/auth.md",
        document_type="markdown",
    )

    chunks = chunk_markdown(document)

    assert len(chunks) == 2

    assert chunks[0].content == ("DevBrain uses token-based authentication.")
    assert chunks[0].metadata["section"] == "Authentication"

    assert chunks[1].content == "Tokens are validated by middleware."
    assert chunks[1].metadata["section"] == "Token Validation"


def test_chunk_markdown_content_before_heading():
    document = Document(
        content=(
            "This document explains DevBrain.\n\n"
            "# Authentication\n\n"
            "Authentication uses tokens."
        ),
        source="docs/auth.md",
        document_type="markdown",
    )

    chunks = chunk_markdown(document)

    assert len(chunks) == 2
    assert chunks[0].content == "This document explains DevBrain."
    assert chunks[0].metadata["section"] == ""
    assert chunks[1].metadata["section"] == "Authentication"
