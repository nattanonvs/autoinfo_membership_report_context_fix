{
    "name": "AUTO-INFO : Membership Report Context Fix",
    "version": "15.0.1.0.3",
    "category": "Membership",
    "summary": "Fix Members Analysis context to prevent invalid date domains",
    "author": "The Auto-Info Co., Ltd.",
    "website": "https://the-auto-info.com",
    "license": "LGPL-3",
    "depends": ["membership"],
    "data": [
        "views/res_config_settings_view.xml",
    ],
    "images": [
        "static/description/icon.png",
    ],
    "post_init_hook": "post_init_hook",
    "uninstall_hook": "uninstall_hook",
    "installable": True,
    "application": False,
}
