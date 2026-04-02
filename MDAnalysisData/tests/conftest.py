# see also pyproject.toml pytest.markers
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "online: will fetch remote files (deselect with with '-m \"not online\"')",
    )
