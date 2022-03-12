%define module setuptools

# Disable rpmlint checks while bootstrapping: rpmlint needs
# python-pkg_resources and will fail before it is built with the
# correct version of python. (This hits e.g. when updating python to
# a new major version)
%bcond_without bootstrap
%if %{with bootstrap}
%define _build_pkgcheck /bin/true
%define _build_pkgcheck_set /bin/true
%define _build_pkgcheck_srpm /bin/true
%endif

Summary:	Python Distutils Enhancements
Name:		python-%{module}
Version:	60.9.3
Release:	2
License:	Zope Public License (ZPL)
Group:		Development/Python
Url:		https://pypi.org/project/setuptools/
Source0:	https://files.pythonhosted.org/packages/source/s/setuptools/setuptools-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
%if %{without bootstrap}
BuildRequires:	python-packaging
%endif
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
%if %{without bootstrap}
Requires:	python-packaging
%endif

%description -n python-pkg-resources
Module used to find and manage Python package/version dependencies and access
bundled files and resources, including those inside of zipped .egg files.

%prep
%autosetup -n %{module}-%{version}

%build
export CFLAGS="%{optflags}"
%py_build

#check
#%__python setup.py test

%install
%py_install
find %{buildroot}%{python_sitelib} -name '*.exe' -delete

%files
%{py_puresitedir}/*
%exclude %{py_puresitedir}/pkg_resources

%files -n python-pkg-resources
%{py_puresitedir}/pkg_resources
