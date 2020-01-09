from openupgradelib import openupgrade


@openupgrade.migrate(use_env=True)
def migrate(env, version):
    cr = env.cr
    openupgrade.load_data(
        cr, 'crm_phonecall', 'migrations/10.0.1.1.1/noupdate_changes.xml',
    )
