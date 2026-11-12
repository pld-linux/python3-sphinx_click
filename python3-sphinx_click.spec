#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	Sphinx extension that automatically documents click applications
Summary(pl.UTF-8):	Rozszerzenie Sphinksa automatycznie dokumentujące aplikacje clicka
Name:		python3-sphinx_click
Version:	6.2.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-click/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-click/sphinx_click-%{version}.tar.gz
# Source0-md5:	a1000330f3e0a9da6e74920df2faaf80
URL:		https://pypi.org/project/sphinx-click/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.10
BuildRequires:	python3-setuptools >= 1:80
BuildRequires:	python3-setuptools_scm >= 8
%if %{with tests}
BuildRequires:	python3-Sphinx >= 4.0
BuildRequires:	python3-click >= 8.0
BuildRequires:	python3-docutils
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
%if %{with doc}
BuildRequires:	python3-click >= 8.0
BuildRequires:	sphinx-pdg-3 >= 4.0
%endif
Requires:	python3-modules >= 1:3.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sphinx-click is a Sphinx plugin that allows you to automatically
extract documentation from a click-based application and include it in
your docs.

%description -l pl.UTF-8
sphinx-click to wtyczka Sphinksa, pozwalająca automatycznie wydobywać
opisy z aplikacji opartych na module click i dołączać je do
dokumentacji.

%package apidocs
Summary:	API documentation for Python sphinx-click module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona sphinx-click
Group:		Documentation

%description apidocs
API documentation for Python sphinx-click module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona sphinx-click.

%prep
%setup -q -n sphinx_click-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd) \
%{__python3} -m pytest tests
%endif

%if %{with doc}
# reno release-notes directive needs a git checkout, sdist has none
PYTHONPATH=$(pwd) \
sphinx-build-3 -b html \
	-D extensions=sphinx_click \
	-D exclude_patterns=_build,changelog.rst \
	docs docs/_build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/sphinx_click
%{py3_sitescriptdir}/sphinx_click-%{version}.dist-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,examples,*.html,*.js}
%endif
