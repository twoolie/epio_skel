from fabric.api import local, env, require

def production():
    env['epioapp'] = # production epio instance name

def staging():
    env['epioapp'] = # staging epio instance

def epio(commandstring):
    require('epioapp', provided_by=['production','staging'])
    from os import path
    with lcd(path.dirname(__file__)):
        local("epio {0} -a {1}".format(
            commandstring,
            env['epioapp']))

def deploy():
    """ An example deploy workflow """
    epio('suspend')
    local('./manage.py "collectstatic --noinput"')
    epio('upload')
    epio('django syncdb')
    epio('django migrate')
    epio('django epio_flush_cache')
    epio('resume')

