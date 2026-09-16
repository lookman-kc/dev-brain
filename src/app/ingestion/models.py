from pydantic import BaseModel, Field


class Document(BaseModel):
    content: str
    source: str
    document_type: str
    metadata: dict[str, str] = Field(default_factory=dict)
