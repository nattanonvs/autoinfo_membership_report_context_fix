from odoo import SUPERUSER_ID, api

MODULE_KEY = "autoinfo_membership_report_context_fix"
PARAM_ENABLED = "%s.enabled" % MODULE_KEY
PARAM_PREVIOUS_CONTEXT = "%s.previous_action_context" % MODULE_KEY

SAFE_CONTEXT = {
    "group_by_no_leaf": 1,
    "search_default_Revenue": 1,
    "search_default_salesman": 1,
    "search_default_this_month": 1,
}


def _get_action(env):
    return env.ref("membership.action_report_membership_tree", raise_if_not_found=False)


def _get_params(env):
    return env["ir.config_parameter"].sudo()


def _safe_context_str():
    return repr(SAFE_CONTEXT)


def apply_fix(env):
    action = _get_action(env)
    if not action:
        return

    params = _get_params(env)
    if params.get_param(PARAM_PREVIOUS_CONTEXT) is None:
        params.set_param(PARAM_PREVIOUS_CONTEXT, action.context or "")

    enabled = params.get_param(PARAM_ENABLED, "True")
    if enabled in ("True", "1", "true", "yes", "Y", "y"):
        action.write({"context": _safe_context_str()})
        return

    previous = params.get_param(PARAM_PREVIOUS_CONTEXT, "")
    action.write({"context": previous})


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    apply_fix(env)


def uninstall_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    action = _get_action(env)
    params = _get_params(env)
    previous = params.get_param(PARAM_PREVIOUS_CONTEXT)
    if action and previous is not None:
        action.write({"context": previous})

    to_delete = params.search([("key", "in", [PARAM_ENABLED, PARAM_PREVIOUS_CONTEXT])])
    to_delete.unlink()

