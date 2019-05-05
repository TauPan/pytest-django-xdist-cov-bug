# pytest-django-xdist-cov-bug
Reproducing https://github.com/pytest-dev/pytest-cov/issues/285

 - Install pipenv: https://docs.pipenv.org/en/latest/#install-pipenv-today
 - Install dependencies: `pipenv sync --dev`
 - Add `proj` to path, e.g.: `add2virtualenv proj`
 - Run tests: `pipenv run pytest` (should be green)
 - Run tests with coverage and xdist: `pipenv run pytest --cov -n2` (red for me)

The exception will look similar to this:
```python
----------------------------------------------------------------------------- Captured log call ------------------------------------------------------------------------------
log.py                     228 ERROR    Internal Server Error: /
Traceback (most recent call last):
  File "/home/friedel/.virtualenvs/pytest-django-xdist-cov-bug-fdjissHu/lib/python3.6/site-packages/django/template/defaulttags.py", line 1021, in find_library
    return parser.libraries[name]
KeyError: 'tags'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/friedel/.virtualenvs/pytest-django-xdist-cov-bug-fdjissHu/lib/python3.6/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/friedel/.virtualenvs/pytest-django-xdist-cov-bug-fdjissHu/lib/python3.6/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/friedel/.virtualenvs/pytest-django-xdist-cov-bug-fdjissHu/lib/python3.6/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/friedel/git/pytest-django-xdist-cov-bug/proj/app/views.py", line 8, in home
    dict(args=request.GET.getlist('args[]')))
  File "/home/friedel/.virtualenvs/pytest-django-xdist-cov-bug-fdjissHu/lib/python3.6/site-packages/django/shortcuts.py", line 36, in render
    content = loader.render_to_string(template_name, context, request, using=using)
  File "/home/friedel/.virtualenvs/pytest-django-xdist-cov-bug-fdjissHu/lib/python3.6/site-packages/django/template/loader.py", line 61, in render_to_string
    template = get_template(template_name, using=using)
  File "/home/friedel/.virtualenvs/pytest-django-xdist-cov-bug-fdjissHu/lib/python3.6/site-packages/django/template/loader.py", line 15, in get_template
    return engine.get_template(template_name)
  File "/home/friedel/.virtualenvs/pytest-django-xdist-cov-bug-fdjissHu/lib/python3.6/site-packages/django/template/backends/django.py", line 34, in get_template
    return Template(self.engine.get_template(template_name), self)
  File "/home/friedel/.virtualenvs/pytest-django-xdist-cov-bug-fdjissHu/lib/python3.6/site-packages/django/template/engine.py", line 143, in get_template
    template, origin = self.find_template(template_name)
  File "/home/friedel/.virtualenvs/pytest-django-xdist-cov-bug-fdjissHu/lib/python3.6/site-packages/django/template/engine.py", line 125, in find_template
    template = loader.get_template(name, skip=skip)
  File "/home/friedel/.virtualenvs/pytest-django-xdist-cov-bug-fdjissHu/lib/python3.6/site-packages/django/template/loaders/base.py", line 30, in get_template
    contents, origin, origin.template_name, self.engine,
  File "/home/friedel/.virtualenvs/pytest-django-xdist-cov-bug-fdjissHu/lib/python3.6/site-packages/django/template/base.py", line 156, in __init__
    self.nodelist = self.compile_nodelist()
  File "/home/friedel/.virtualenvs/pytest-django-xdist-cov-bug-fdjissHu/lib/python3.6/site-packages/django/template/base.py", line 194, in compile_nodelist
    return parser.parse()
  File "/home/friedel/.virtualenvs/pytest-django-xdist-cov-bug-fdjissHu/lib/python3.6/site-packages/django/template/base.py", line 478, in parse
    raise self.error(token, e)
  File "/home/friedel/.virtualenvs/pytest-django-xdist-cov-bug-fdjissHu/lib/python3.6/site-packages/django/template/base.py", line 476, in parse
    compiled_result = compile_func(self, token)
  File "/home/friedel/.virtualenvs/pytest-django-xdist-cov-bug-fdjissHu/lib/python3.6/site-packages/django/template/defaulttags.py", line 1078, in load
    lib = find_library(parser, name)
  File "/home/friedel/.virtualenvs/pytest-django-xdist-cov-bug-fdjissHu/lib/python3.6/site-packages/django/template/defaulttags.py", line 1025, in find_library
    name, "\n".join(sorted(parser.libraries)),
django.template.exceptions.TemplateSyntaxError: 'tags' is not a registered tag library. Must be one of:
admin_list
admin_modify
admin_static
admin_urls
cache
i18n
l10n
log
static
staticfiles
tz

----------- coverage: platform linux, python 3.6.8-final-0 -----------
Name    Stmts   Miss  Cover
---------------------------

===================================================================== 1 failed, 1 passed in 2.62 seconds =====================================================================
```
