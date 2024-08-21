from odoo import fields, models
from ..routers import router
from odoo.addons.fastapi.dependencies import (
    authenticated_partner_from_basic_auth_user,
    authenticated_partner_impl,
)


class FastapiEndpoint(models.Model):
    _inherit = "fastapi.endpoint"

    app: str = fields.Selection(
        selection_add=[("partner_api", "Partner API")], ondelete={"partner_api": "cascade"}
    )

    def _get_fastapi_routers(self):
        if self.app == "partner_api":
            return [router]
        return super()._get_fastapi_routers()

    def _get_app(self):
        app = super()._get_app()
        if self.app == "partner_api":
            app.dependency_overrides[
                authenticated_partner_impl
            ] = authenticated_partner_from_basic_auth_user
        return app
