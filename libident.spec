Summary:	LibIdent
Summary(pl):	LibIdent
Name:		libident
Version:	0.22
Release:	1
Copyright:	GPL
Group:		Libraries
Group(pl):	Biblioteki
Source:		ftp://ftp.lysator.liu.se/pub/ident/libs/%name-%version.tar.gz
Patch:		%name-compile-fix.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr

%description

%description -l pl

%prep
%setup -q

%patch -p1

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" linux

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_mandir}/man3,%{_includedir}}
make INSTROOT=$RPM_BUILD_ROOT%{_prefix} install

gzip -9 $RPM_BUILD_ROOT%{_mandir}/man3/*
gzip README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(644,root,root) %{_libdir}/libident.a

%attr(644,root,root) %{_includedir}/ident.h

%attr(644,root,root) %{_mandir}/man3/ident*gz
