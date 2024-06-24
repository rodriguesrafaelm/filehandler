import nox

nox.options.python = ["3.12"]

dependencies_installed = False

@nox.session
def tests(session):
    global dependencies_installed

    if not dependencies_installed:
        session.install('-r', 'requirements.txt')
        dependencies_installed = True
    
    args = session.posargs

    session.run("pytest", *args)

@nox.session
def coverage_tests(session):
    global dependencies_installed

    if not dependencies_installed:
        session.install('-r', 'requirements.txt')
        dependencies_installed = True
    
    args = session.posargs

    session.run("pytest", "--cov", *args, external=True)


@nox.session
def pylint_tests(session):
    global dependencies_installed

    if not dependencies_installed:
        session.install('-r', 'requirements.txt',)
        dependencies_installed = True
    
    args = session.posargs or ["filehandler/", "tests/"]

    session.run("pylint", *args, external=True)