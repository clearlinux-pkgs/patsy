#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : patsy
Version  : 0.5.1
Release  : 10
URL      : https://files.pythonhosted.org/packages/49/c7/b971d8685c52512dbaa45bf8d076695432245a9f59509fb20a6c8e4ff69a/patsy-0.5.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/49/c7/b971d8685c52512dbaa45bf8d076695432245a9f59509fb20a6c8e4ff69a/patsy-0.5.1.tar.gz
Summary  : A Python package for describing statistical models and for building design matrices.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: patsy-license = %{version}-%{release}
Requires: patsy-python = %{version}-%{release}
Requires: patsy-python3 = %{version}-%{release}
Requires: ipython
Requires: jsonschema
Requires: mistune
Requires: numpy
Requires: pandas
Requires: scipy
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : numpy
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
(especially linear models, or models that have a linear component) and
        building design matrices. Patsy brings the convenience of `R

%package license
Summary: license components for the patsy package.
Group: Default

%description license
license components for the patsy package.


%package python
Summary: python components for the patsy package.
Group: Default
Requires: patsy-python3 = %{version}-%{release}

%description python
python components for the patsy package.


%package python3
Summary: python3 components for the patsy package.
Group: Default
Requires: python3-core

%description python3
python3 components for the patsy package.


%prep
%setup -q -n patsy-0.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1540764229
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/patsy
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/patsy/LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/patsy/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
