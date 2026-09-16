from app.ingestion.models import Chunk


def test_chunk():
    chunk = Chunk(
        content="DevBrain uses token-based authentication.",
        metadata={
            "source": "docs/auth.md",
            "section": "Authentication",
        },
    )

    assert chunk.content == "DevBrain uses token-based authentication."
    assert chunk.metadata["source"] == "docs/auth.md"
    assert chunk.metadata["section"] == "Authentication"
