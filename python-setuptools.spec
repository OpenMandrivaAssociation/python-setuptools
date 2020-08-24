%define module setuptools
%define _xz_threads 0

Summary:	Python Distutils Enhancements
Name:		python-%{module}
Version:	49.6.0
Release:	1
License:	Zope Public License (ZPL)
Group:		Development/Python
Url:		https://pypi.org/project/setuptools/
Source0:	https://files.pythonhosted.org/packages/38/cc/db23dbe4efc464c3c0111fedf7d46de8888f05b09488d610f6f8ab6e2544/setuptools-49.6.0.zip
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-packaging
BuildRequires:	python-appdirs
Requires:	python-pkg-resources
%rename	python-distribute
Provides:	python3-distribute
Provides:	python3-setuptools = %{EVRD}
Provides:	python3egg(setuptools)
Provides:	python3egg(distribute)

%description
A collection of enhancements to the Python distutils that allow
you to more easily build and distribute Python packages, especially
ones that have dependencies on other packages.

%package -n python-pkg-resources
Summary:	Runtime module to access python resources
Group:		Development/Python
Conflicts:	python-setuptools < 0.6c9-2mdv
Provides:	python3-pkg-resources
Requires:	python-packaging
Requires:	python-appdirs

%description -n python-pkg-resources
Module used to find and manage Python package/version dependencies and access
bundled files and resources, including those inside of zipped .egg files.

%prep
%autosetup -n %{module}-%{version}

%build
export CFLAGS="%{optflags}"

%__python setup.py build

%check
#%__python setup.py test

%install
%__python setup.py install --root=%{buildroot}
find %{buildroot}%{python_sitelib} -name '*.exe' -delete

%files
%{_bindir}/easy_install
%{_bindir}/easy_install-%{py3_ver}
%{py_puresitedir}/*
%exclude %{py_puresitedir}/pkg_resources

%files -n python-pkg-resources
%{py_puresitedir}/pkg_resources
