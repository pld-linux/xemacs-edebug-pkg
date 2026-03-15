Summary:	An Emacs Lisp debugger
Summary(pl.UTF-8):	Debugger do Emacs Lispa
Name:		xemacs-edebug-pkg
%define 	srcname	edebug
Version:	1.24
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	http://ftp.xemacs.org/pub/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	e2f6b3ce224cab0cef4fd0dbbd5dd5a5
URL:		https://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-base-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An Emacs Lisp debugger.

%description -l pl.UTF-8
Debugger do Emacs Lispa.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/edebug/README lisp/edebug/ChangeLog
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
