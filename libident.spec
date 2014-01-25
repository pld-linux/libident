Summary:	LibIdent - Library
Summary(pl.UTF-8):	LibIdent - Biblioteka
Name:		libident
Version:	0.32
Release:	1
License:	Public Domain
Group:		Libraries
Source0:	http://www.remlab.net/files/libident/%{name}-%{version}.tar.bz2
# Source0-md5:	f567aaf43eb1fa60d15b87e09a7fca5d
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibIdent is a library which provides ident support in application.

%description -l pl.UTF-8
LibIdent jest biblioteką udostępniającą interfejs do usługi ident.

%package devel
Summary:	LibIdent - header files
Summary(pl.UTF-8):	LibIdent - pliki nagłówkowe
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
LibIdent - header files.

%description devel -l pl.UTF-8
LibIdent - pliki nagłówkowe.

%package static
Summary:	LibIdent - Static Library
Summary(pl.UTF-8):	LibIdent - Biblioteka statyczna
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
LibIdent - Static Library.

%description static -l pl.UTF-8
LibIdent - Biblioteka statyczna.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I.
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_mandir}/man3,%{_includedir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README 
%attr(755,root,root) %{_libdir}/libident.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libident.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libident.so
%{_includedir}/ident.h
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libident.a
