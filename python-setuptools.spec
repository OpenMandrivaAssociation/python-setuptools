%define module setuptools
%define _xz_threads 0

Summary:	Python Distutils Enhancements
Name:		python-%{module}
Version:	45.0.0
Release:	1
License:	Zope Public License (ZPL)
Group:		Development/Python
Url:		https://pypi.org/project/setuptools/
Source0:	https://files.pythonhosted.org/packages/fd/76/3c7f726ed5c582019937f178d7478ce62716b7e8263344f1684cbe11ab3e/setuptools-45.0.0.zip
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

%package -n python2-setuptools
Summary:	Python Distutils Enhancements
Group:		Development/Python
%rename python2-distribute
Provides:	pythonegg(setuptools)
Provides:	pythonegg(distribute)
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-packaging
BuildRequires:	python2-appdirs

%description -n python2-setuptools
A collection of enhancements to the Python distutils that allow
you to more easily build and distribute Python packages, especially
ones that have dependencies on other packages.

%package -n python-pkg-resources
Summary:	Runtime module to access python resources
Group:		Development/Python
Conflicts:	python-setuptools < 0.6c9-2mdv
Requires:	python-packaging
Requires:	python-appdirs

%description -n python-pkg-resources
Module used to find and manage Python package/version dependencies and access
bundled files and resources, including those inside of zipped .egg files.

%package -n python2-pkg-resources
Summary:	Runtime module to access python resources
Group:		Development/Python
Conflicts:	python-setuptools < 0.6c9-2mdv
Conflicts:	python-pkg-resources < 6.1
Requires:	python2-packaging
Requires:	python2-appdirs

%description -n python2-pkg-resources
Module used to find and manage Python package/version dependencies and access
bundled files and resources, including those inside of zipped .egg files.

%prep
%setup -qc -n setuptools-%{version}

mv setuptools-%{version} python3
cp -r python3 python2

%build
export CFLAGS="%{optflags}"

cd python3
%__python setup.py build
cd -

cd python2
%__python2 setup.py build
cd -

%check
#%__python setup.py test

%install
cd python2
%__python2 setup.py install --root=%{buildroot}
cd -

cd python3
%__python setup.py install --root=%{buildroot}
cd -

find %{buildroot}%{python_sitelib} -name '*.exe' -delete

%files
%{_bindir}/easy_install
%{_bindir}/easy_install-%{py3_ver}
%{py_puresitedir}/*
%exclude %{py_puresitedir}/pkg_resources

%files -n python-pkg-resources
%{py_puresitedir}/pkg_resources

%files -n python2-setuptools
%{_bindir}/easy_install-%{py2_ver}
%{py2_puresitedir}/*
%exclude %{py2_puresitedir}/pkg_resources

%files -n python2-pkg-resources
%{py2_puresitedir}/pkg_resources
