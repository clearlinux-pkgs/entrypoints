Name     : entrypoints
Version  : 0.2.2
Release  : 1
URL      : https://pypi.python.org/packages/f8/ad/0e77a853c745a15981ab51fa9a0cb4eca7a7a007b4c1970106ee6ba01e0c/entrypoints-0.2.2-py2.py3-none-any.whl
Source0  : https://pypi.python.org/packages/f8/ad/0e77a853c745a15981ab51fa9a0cb4eca7a7a007b4c1970106ee6ba01e0c/entrypoints-0.2.2-py2.py3-none-any.whl
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : python3-dev
BuildRequires : pip

%description
No detailed description available

%prep

%build
export LANG=C
export SOURCE_DATE_EPOCH=1486351168

%install
rm -rf %{buildroot}
pip3 install --no-deps  --root %{buildroot} %{SOURCE0}
for i in `find %{buildroot} -name "*.so" `; do rm $i; done

%files
%defattr(-,root,root,-)
/usr/lib/python3.6/site-packages
