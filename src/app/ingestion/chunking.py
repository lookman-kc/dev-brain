import re

from app.ingestion.models import Chunk, Document


def chunk_markdown(document: Document) -> list[Chunk]:
    sections = re.split(r"(?m)^(#{1,6})\s+(.+?)\s*$", document.content)

    chunks: list[Chunk] = []

    if sections[0].strip():
        chunks.append(
            Chunk(
                content=sections[0].strip(),
                metadata={
                    "source": document.source,
                    "document_type": document.document_type,
                    "section": "",
                },
            )
        )

    for index in range(1, len(sections), 3):
        heading = sections[index + 1].strip()
        content = sections[index + 2].strip()

        if not content:
            continue

        chunks.append(
            Chunk(
                content=content,
                metadata={
                    "source": document.source,
                    "document_type": document.document_type,
                    "section": heading,
                },
            )
        )

    return chunks
