#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	Sphinx extension that automatically documents click applications
Summary(pl.UTF-8):	Rozszerzenie Sphinksa automatycznie dokumentujące aplikacje clicka
Name:		python3-sphinx_click
Version:	5.1.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-click/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-click/sphinx-click-%{version}.tar.gz
# Source0-md5:	9baf1d4e0fbc83d3c56b5b5fc75b0887
URL:		https://pypi.org/project/sphinx-click/
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	python3-pbr >= 2.0
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx >= 2.0
BuildRequires:	python3-click >= 7.0
BuildRequires:	python3-docutils
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-3 >= 2.0
%endif
Requires:	python3-modules >= 1:3.8
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
%setup -q -n sphinx-click-%{version}

%build
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s tests
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
sphinx-build-3 -b html docs docs/_build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE README.rst
%{py3_sitescriptdir}/sphinx_click
%{py3_sitescriptdir}/sphinx_click-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,examples,*.html,*.js}
%endif
