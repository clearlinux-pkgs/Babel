#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Babel
Version  : 2.5.3
Release  : 52
URL      : https://pypi.debian.net/Babel/Babel-2.5.3.tar.gz
Source0  : https://pypi.debian.net/Babel/Babel-2.5.3.tar.gz
Summary  : Internationalization utilities
Group    : Development/Tools
License  : BSD-3-Clause
Requires: Babel-bin
Requires: Babel-python3
Requires: Babel-python
Requires: pytz
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : pytz
BuildRequires : setuptools

%description
Flask Sphinx Styles
===================
This repository contains sphinx styles for Flask and Flask related
projects.  To use this style in your Sphinx documentation, follow
this guide:

%package bin
Summary: bin components for the Babel package.
Group: Binaries

%description bin
bin components for the Babel package.


%package legacypython
Summary: legacypython components for the Babel package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the Babel package.


%package python
Summary: python components for the Babel package.
Group: Default
Requires: Babel-python3
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
%setup -q -n Babel-2.5.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1519050534
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test tests || :
%install
export SOURCE_DATE_EPOCH=1519050534
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pybabel

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
