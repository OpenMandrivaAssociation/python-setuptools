%define module setuptools
%define _xz_threads 0

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
Version:	51.3.3
Release:	1
License:	Zope Public License (ZPL)
Group:		Development/Python
Url:		https://pypi.org/project/setuptools/
Source0:	https://files.pythonhosted.org/packages/96/66/1138b7ec901e86139c07900ce906c2f1e5c3400ee1cfd1e7ab3c776248c9/setuptools-51.3.3.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
%if %{without bootstrap}
BuildRequires:	python-packaging
%endif
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
%if %{without bootstrap}
Requires:	python-packaging
%endif
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
