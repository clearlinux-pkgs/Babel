#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Babel
Version  : 2.2.0
Release  : 27
URL      : https://pypi.python.org/packages/source/B/Babel/Babel-2.2.0.tar.gz
Source0  : https://pypi.python.org/packages/source/B/Babel/Babel-2.2.0.tar.gz
Summary  : Internationalization utilities
Group    : Development/Tools
License  : BSD-3-Clause
Requires: Babel-bin
Requires: Babel-python
BuildRequires : pbr
BuildRequires : pip
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


%package python
Summary: python components for the Babel package.
Group: Default
Provides: babel-python

%description python
python components for the Babel package.


%prep
%setup -q -n Babel-2.2.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test tests || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pybabel

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
