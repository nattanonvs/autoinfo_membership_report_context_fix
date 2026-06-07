import json

from odoo.tests.common import TransactionCase, tagged
from odoo.tools.safe_eval import safe_eval


@tagged("post_install", "-at_install")
class TestMembershipActionContext(TransactionCase):
    def test_members_analysis_action_context_has_no_date_equals_one(self):
        action = self.env.ref("membership.action_report_membership_tree")
        context_str = action.context or "{}"
        try:
            ctx = safe_eval(context_str)
        except Exception:
            ctx = json.loads(context_str)

        self.assertNotIn("search_default_start_date", ctx)
        self.assertNotIn("search_default_member", ctx)
