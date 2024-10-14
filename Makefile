.PHONY: release sdist wheel clean

release: sdist wheel

sdist:
	python3 setup.py sdist

wheel:
	python3 setup.py bdist_wheel

clean:
	$(RM) -vrf py2fa_cli.egg-info py2fa/__pycache__ build dist
