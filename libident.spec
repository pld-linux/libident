Summary:	LibIdent - Ident protocol client library
Summary(pl.UTF-8):	LibIdent - biblioteka kliencka dla protokołu Ident
Name:		libident
Version:	0.32
Release:	2
License:	Public Domain
Group:		Libraries
Source0:	http://www.remlab.net/files/libident/%{name}-%{version}.tar.bz2
# Source0-md5:	f567aaf43eb1fa60d15b87e09a7fca5d
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.7
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibIdent is a library which provides Ident protocol support in
application.

%description -l pl.UTF-8
LibIdent jest biblioteką udostępniającą interfejs do usługi protokołu
Ident.

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
Summary:	LibIdent - static Library
Summary(pl.UTF-8):	LibIdent - biblioteka statyczna
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
LibIdent - static Library.

%description static -l pl.UTF-8
LibIdent - biblioteka statyczna.

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no external dependencies
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libident.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README 
%attr(755,root,root) %{_libdir}/libident.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libident.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libident.so
%{_includedir}/ident.h
%{_mandir}/man3/ident.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libident.a
