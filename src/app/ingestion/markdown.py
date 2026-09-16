from pathlib import Path

from app.ingestion.models import Document


def load_markdown(path: Path) -> Document:
    if path.suffix.lower() not in {".md", ".markdown"}:
        raise ValueError("File must be a Markdown file")

    content = path.read_text(encoding="utf-8")

    return Document(
        content=content,
        source=str(path),
        document_type="markdown",
        metadata={
            "filename": path.name,
        },
    )
