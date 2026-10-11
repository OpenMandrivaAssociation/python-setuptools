%define module setuptools

# Disable rpmlint checks while bootstrapping. The real rpmlint is not
# rebuilt yet, and setuptools 82 removed pkg_resources.
%bcond_without bootstrap
%if %{with bootstrap}
%define _build_pkgcheck /bin/true
%define _build_pkgcheck_set /bin/true
%define _build_pkgcheck_srpm /bin/true
%endif

Summary:	Python Distutils Enhancements
Name:		python-%{module}
Version:	84.0.0
Release:	1
License:	Zope Public License (ZPL)
Group:		Development/Python
Url:		https://pypi.org/project/setuptools/
Source0:	https://files.pythonhosted.org/packages/source/s/setuptools/setuptools-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(packaging)
# Make the dependency generator great again
Requires:	python%{pyver}dist(packaging)
# setuptools 82 removed pkg_resources. Drop the old subpackage on upgrade.
Obsoletes:	python-pkg-resources < 82
%rename	python-distribute
# For compatibility with packages built for other distros
Provides:	python3-distribute
# For compatibility with packages built for other distros
Provides:	python3-setuptools = %{EVRD}

%description
A collection of enhancements to the Python distutils that allow
you to more easily build and distribute Python packages, especially
ones that have dependencies on other packages.

%prep
%autosetup -n setuptools-%{version}

%build
export CFLAGS="%{optflags}"
%if %{with bootstrap}
python setup.py build
%else
%py_build
%endif

#check
#%__python setup.py test

%install
%if %{with bootstrap}
python setup.py install --skip-build --root "%{buildroot}"
%else
%py_install
%endif
find %{buildroot}%{python_sitelib} -name '*.exe' -delete

%files
%{py_puresitedir}/*
