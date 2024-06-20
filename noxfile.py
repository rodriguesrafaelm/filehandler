import nox

dependencies_installed = False

@nox.session(python=["3.12"])
def tests(session):
    global dependencies_installed

    if not dependencies_installed:
        session.install('-r', 'requirements.txt')
        dependencies_installed = True
    
    args = session.posargs

    session.run("pytest", *args)

@nox.session(python=["3.12"])
def coverage_tests(session):
    global dependencies_installed

    if not dependencies_installed:
        session.install('-r', 'requirements.txt')
        dependencies_installed = True
    
    args = session.posargs

    session.run("pytest", "--cov", *args)