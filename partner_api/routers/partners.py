from fastapi import APIRouter, Depends
from typing import Annotated
from odoo.api import Environment
from odoo.addons.fastapi.dependencies import odoo_env, authenticated_partner
from ..schemas import PartnerSchema
from odoo.addons.base.models.res_partner import Partner

router = APIRouter(tags=["partners"])


@router.get("/partners", response_model=list[PartnerSchema])
def get_partners(
    env: Annotated[Environment, Depends(odoo_env)], partner: Annotated[Partner, Depends(authenticated_partner)]
) -> list[PartnerSchema]:
    return [
        PartnerSchema(name=partner.name)
        for partner in env["res.partner"].search([])
    ]
