%define		plugin	form
Summary:	jQuery Form Plugin
Name:		jquery-%{plugin}
Version:	2.94
Release:	1
License:	MIT / GPL
Group:		Applications/WWW
Source0:	https://github.com/malsup/form/tarball/master/%{name}-%{version}.tgz
# Source0-md5:	6f6a530e164d83b44de3a3c41ba68322
URL:		http://jquery.malsup.com/form/
BuildRequires:	closure-compiler
BuildRequires:	js
BuildRequires:	rpmbuild(macros) > 1.268
Requires:	jquery >= 1.3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
The jQuery Form Plugin allows you to easily and unobtrusively upgrade
HTML forms to use AJAX. The main methods, ajaxForm and ajaxSubmit,
gather information from the form element to determine how to manage
the submit process. Both of these methods support numerous options
which allows you to have full control over how the data is submitted.
Submitting a form with AJAX doesn't get any easier than this!

%prep
%setup -qc
mv *-%{plugin}-*/* .

%build
install -d build

# compress .js
js=jquery.%{plugin}.js
out=build/$js
%if 0%{!?debug:1}
closure-compiler --js $js --charset UTF-8 --js_output_file $out
js -C -f $out
%else
cp -p $js $out
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -p jquery.%{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.js
cp -p build/jquery.%{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.min.js
ln -s %{plugin}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
