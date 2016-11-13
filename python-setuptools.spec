%define module	setuptools
 
Summary:	Python Distutils Enhancements
Name:		python-%{module}
Version:	24.1.0
Release:	1
License:	Zope Public License (ZPL)
Group:		Development/Python
Url:		http://pypi.python.org/pypi/setuptools
Source0:	https://files.pythonhosted.org/packages/source/s/%{module}/%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
Requires:	python-devel
Requires:	python-pkg-resources
%rename	python-distribute
Provides:	python3-distribute
Provides:	python3egg(setuptools)
Provides:	python3egg(distribute)
%description
A collection of enhancements to the Python distutils that allow 
you to more easily build and distribute Python packages, especially 
ones that have dependencies on other packages.

%package -n python2-setuptools
Summary:        Python Distutils Enhancements
Group:          Development/Python
%rename python2-distribute
Provides:	pythonegg(setuptools)
Provides:	pythonegg(distribute)
BuildRequires:	pkgconfig(python2)

%package -n python-pkg-resources
Summary: Runtime module to access python resources
Group:	Development/Python
Conflicts: python-setuptools < 0.6c9-2mdv

%description -n python-pkg-resources
Module used to find and manage Python package/version dependencies and access
bundled files and resources, including those inside of zipped .egg files.

%package -n python2-pkg-resources
Summary: Runtime module to access python resources
Group:  Development/Python
Conflicts: python-setuptools < 0.6c9-2mdv
Conflicts: python-pkg-resources < 6.1

%description -n python-pkg-resources
Module used to find and manage Python package/version dependencies and access
bundled files and resources, including those inside of zipped .egg files.

%prep
%setup -qc -n setuptools-%{version}

mv setuptools-%{version} python3
cp -r python3 python2

%build
export CFLAGS="%{optflags}"

pushd python3
%__python setup.py build
popd

pushd python2
%__python2 setup.py build
popd

%check
#%__python setup.py test

%install
pushd python2
%__python2 setup.py install --root=%{buildroot}
popd

pushd python3
%__python setup.py install --root=%{buildroot}
popd

%files
%doc python3/*.rst
%{_bindir}/easy_install
%{_bindir}/easy_install-%{py3_ver}
%{py_puresitedir}/*
%exclude %{py_puresitedir}/pkg_resources

%files -n python-pkg-resources
%{py_puresitedir}/pkg_resources

%files -n python2-setuptools
%doc python2/*.rst
%{_bindir}/easy_install-%{py2_ver}
%{py2_puresitedir}/*
%exclude %{py2_puresitedir}/pkg_resources

%files -n python2-pkg-resources
%{py2_puresitedir}/pkg_resources
