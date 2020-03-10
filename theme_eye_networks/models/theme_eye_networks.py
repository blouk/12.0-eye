from odoo import models

class ThemeEyeNetworks(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_eye_networks_post_copy(self, mod):
        self.disable_view('website_theme_install.customize_modal')
