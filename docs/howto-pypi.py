
# coding: utf-8

# # How to package and distribut projects - with [a template project](https://github.com/yang-zhang/howto-pypi)

# Upgrade `setuptools` and install `twine` and `wheel`.

# Create `setup.py`, for [example](https://github.com/yang-zhang/howto-pypi/blob/master/setup.py):

# Create a source distribution:
# ```sh
# python setup.py sdist
# ```
# 
# Build the [wheel](https://packaging.python.org/tutorials/distributing-packages/#wheels):
# ```sh
# python setup.py bdist_wheel --universal
# ```

# Uploading the project to PyPI
# 
# Register on PyPI and Create a ~/.pypirc file with your username and password:
# ```
# [pypi]
# username = yang-zhang
# password = my-passward
# ```
# Upload:
# ```sh
# $ twine upload dist/*
# Uploading distributions to https://upload.pypi.org/legacy/
# Uploading howto_pypi-0.0.0-py2.py3-none-any.whl
# [================================] 4351/4351 - 00:00:01
# Uploading howto-pypi-0.0.0.tar.gz
# [================================] 3234/3234 - 00:00:00
# ```

# Now you can install the package:
# 
# ```sh
# $ pip install howto-pypi
# Collecting howto-pypi
#   Downloading howto_pypi-0.0.0-py2.py3-none-any.whl
# Installing collected packages: howto-pypi
# Successfully installed howto-pypi-0.0.0
# ```

# And run:
# ```py
# >>> import howto_pypi.display
# >>> howto_pypi.display.howto()
# ```

# References:
# - https://packaging.python.org/tutorials/distributing-packages/
# - https://github.com/pypa/sampleproject

# [Home](https://yang-zhang.github.io/)
