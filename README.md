# Python environment with requirements.txt

[![Binder](http://mybinder.org/badge_logo.svg)](http://mybinder.org/v2/gh/binder-examples/requirements/master)

A Binder-compatible repo with a `requirements.txt` file.

Access this Binder at the following URL 

http://mybinder.org/v2/gh/binder-examples/requirements/master

## Notes
The `requirements.txt` file should list all Python libraries that your notebooks
depend on, and they will be installed using:

```
pip install -r requirements.txt
```

The base Binder image contains no extra dependencies, so be as
explicit as possible in defining the packages that you need. This includes
specifying explict versions wherever possible.

In this example we include the library `seaborn` which will be installed in
the environment, and our notebook uses it to plot a figure.
