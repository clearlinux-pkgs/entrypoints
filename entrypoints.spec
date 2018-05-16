#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : entrypoints
Version  : 0.2.3
Release  : 9
URL      : http://pypi.debian.net/entrypoints/entrypoints-0.2.3.tar.gz
Source0  : http://pypi.debian.net/entrypoints/entrypoints-0.2.3.tar.gz
Summary  : Discover and load entry points from installed packages.
Group    : Development/Tools
License  : MIT
Requires: entrypoints-python3
Requires: entrypoints-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
No detailed description available

%package python
Summary: python components for the entrypoints package.
Group: Default
Requires: entrypoints-python3

%description python
python components for the entrypoints package.


%package python3
Summary: python3 components for the entrypoints package.
Group: Default
Requires: python3-core

%description python3
python3 components for the entrypoints package.


%prep
%setup -q -n entrypoints-0.2.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507153449
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
