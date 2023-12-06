#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module

Summary:	Sphinx extension that automatically documents click applications
Summary(pl.UTF-8):	Rozszerzenie Sphinksa automatycznie dokumentujące aplikacje clicka
Name:		python-sphinx_click
# keep 2.x here for python2 support
Version:	2.7.1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-click/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-click/sphinx-click-%{version}.tar.gz
# Source0-md5:	26365da1469bf8b8f00872994471c7d2
URL:		https://pypi.org/project/sphinx-click/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-pbr >= 2.0
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-Sphinx >= 1.5
BuildRequires:	python-click >= 6.0
BuildRequires:	python-docutils
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-pbr >= 2.0
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx >= 1.5
BuildRequires:	python3-Sphinx < 4
BuildRequires:	python3-click >= 6.0
BuildRequires:	python3-click < 8
BuildRequires:	python3-docutils
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-2 >= 1.5
%endif
Requires:	python-modules >= 1:2.7
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

%package -n python3-sphinx_click
Summary:	Sphinx extension that automatically documents click applications
Summary(pl.UTF-8):	Rozszerzenie Sphinksa automatycznie dokumentujące aplikacje clicka
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-sphinx_click
sphinx-click is a Sphinx plugin that allows you to automatically
extract documentation from a click-based application and include it in
your docs.

%description -n python3-sphinx_click -l pl.UTF-8
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
%setup -q -n sphinx-click-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m unittest discover -s tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python} -m unittest discover -s tests
%endif
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
sphinx-build-2 -b html docs docs/_build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE README.rst
%{py_sitescriptdir}/sphinx_click
%{py_sitescriptdir}/sphinx_click-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-sphinx_click
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE README.rst
%{py3_sitescriptdir}/sphinx_click
%{py3_sitescriptdir}/sphinx_click-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
