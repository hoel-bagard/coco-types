import nox


@nox.session(python=["3.9", "3.10", "3.11"])
def tests(session) -> None:  # pyright: ignore[reportMissingParameterType]
    """Run the test suite."""
    session.install("-r", "requirements/requirements-test.txt")
    session.install(".")
    session.run("pytest", "-v", "tests")

#     # Here we queue up the test coverage session to run next
#     session.notify("coverage")

# @nox.session
# def coverage(session):
#     session.install("coverage")
#     session.run("coverage")
