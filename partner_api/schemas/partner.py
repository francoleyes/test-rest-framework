from pydantic import BaseModel


class PartnerSchema(BaseModel):
    name: str
