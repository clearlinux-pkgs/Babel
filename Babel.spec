#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Babel
Version  : 2.6.0
Release  : 67
URL      : https://pypi.debian.net/Babel/Babel-2.6.0.tar.gz
Source0  : https://pypi.debian.net/Babel/Babel-2.6.0.tar.gz
Summary  : Babel randomly generates character strings based on context free grammars.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: Babel-bin = %{version}-%{release}
Requires: Babel-license = %{version}-%{release}
Requires: Babel-python = %{version}-%{release}
Requires: Babel-python3 = %{version}-%{release}
Requires: pytz
BuildRequires : buildreq-distutils3
BuildRequires : pytest
BuildRequires : pytz

%description
Flask Sphinx Styles
===================
This repository contains sphinx styles for Flask and Flask related
projects.  To use this style in your Sphinx documentation, follow
this guide:

%package bin
Summary: bin components for the Babel package.
Group: Binaries
Requires: Babel-license = %{version}-%{release}

%description bin
bin components for the Babel package.


%package license
Summary: license components for the Babel package.
Group: Default

%description license
license components for the Babel package.


%package python
Summary: python components for the Babel package.
Group: Default
Requires: Babel-python3 = %{version}-%{release}
Provides: babel-python

%description python
python components for the Babel package.


%package python3
Summary: python3 components for the Babel package.
Group: Default
Requires: python3-core

%description python3
python3 components for the Babel package.


%prep
%setup -q -n Babel-2.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554307953
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test tests || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Babel
cp LICENSE %{buildroot}/usr/share/package-licenses/Babel/LICENSE
cp docs/_themes/LICENSE %{buildroot}/usr/share/package-licenses/Babel/docs__themes_LICENSE
cp docs/license.rst %{buildroot}/usr/share/package-licenses/Babel/docs_license.rst
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pybabel

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Babel/LICENSE
/usr/share/package-licenses/Babel/docs__themes_LICENSE
/usr/share/package-licenses/Babel/docs_license.rst

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
