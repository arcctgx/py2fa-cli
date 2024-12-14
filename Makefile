.PHONY: release sdist wheel clean

release: sdist wheel

sdist:
	python3 -m build --sdist

wheel:
	python3 -m build --wheel

clean:
	$(RM) -vrf py2fa_cli.egg-info py2fa/__pycache__ build dist
