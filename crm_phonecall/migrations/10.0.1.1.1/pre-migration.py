from openupgradelib import openupgrade


xmlid_renames = [
    ('crm.group_scheduled_calls',
     'crm_phonecall.group_scheduled_calls'),
]


@openupgrade.migrate(use_env=True)
def migrate(env, version):
    cr = env.cr
    openupgrade.rename_xmlids(cr, xmlid_renames)
