#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	A collection of Python deprecation patterns and strategies that help you collect your technical debt in a non-destructive manner
Summary(pl.UTF-8):	Zbiór wzorców i strategii odchodzenia, pozwalający gromadzić dług technologiczny w sposób niedestruktywny
Name:		python3-debtcollector
Version:	3.0.0
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/debtcollector/
Source0:	https://files.pythonhosted.org/packages/source/d/debtcollector/debtcollector-%{version}.tar.gz
# Source0-md5:	399a20e47b0aec6c3007beb7cc7e017a
URL:		https://pypi.org/project/debtcollector/
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	python3-pbr >= 3.0.0
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-fixtures >= 3.0.0
BuildRequires:	python3-stestr >= 2.0.0
BuildRequires:	python3-subunit >= 1.0.0
BuildRequires:	python3-testtools >= 2.2.0
BuildRequires:	python3-wrapt >= 1.7.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-openstackdocstheme >= 2.2.1
BuildRequires:	python3-reno >= 3.1.0
BuildRequires:	sphinx-pdg-3 >= 2.0.0
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of Python deprecation patterns and strategies that help
you collect your technical debt in a non-destructive manner. The goal
of this library is to provide well documented developer facing
deprecation patterns that start of with a basic set and can expand
into a larger set of patterns as time goes on. The desired output of
these patterns is to apply the warnings module to emit
DeprecationWarning or PendingDeprecationWarning or similar derivative
to developers using libraries (or potentially applications) about
future deprecations.

%description -l pl.UTF-8
Zbiór wzorców i strategii odchodzenia, pozwalający gromadzić dług
technologiczny w sposób niedestruktywny. Celem biblioteki jest
dostarczenie dobrze udokumentowanych, wychodzących naprzeciw
programistom wzorców odchodzenia, które zaczynają się od podstawowego
zbioru i mogą rozszerzać do większego zbioru wzorców w miarę upływu
czasu. Pożądanym wyjściem wzorców jest wykorzystanie modułu warnings
do emitowania wyjątków DeprecationWarning, PendingDeprecationWarning
lub pochodnych programistom wykorzystującym biblioteki (ew. aplikacje)
o przyszłych odchodzących funkcjach.

%package apidocs
Summary:	API documentation for Python debtcollector module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona debtcollector
Group:		Documentation

%description apidocs
API documentation for Pythona debtcollector module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona debtcollector.

%prep
%setup -q -n debtcollector-%{version}

%build
%py3_build

%if %{with tests}
stestr run
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
sphinx-build-3 -b html doc/source doc/build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/debtcollector/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py3_sitescriptdir}/debtcollector
%{py3_sitescriptdir}/debtcollector-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/build/html/{_static,contributor,install,reference,user,*.html,*.js}
%endif
