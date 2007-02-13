Summary:	LibIdent - Library
Summary(pl.UTF-8):	LibIdent - Biblioteka
Name:		libident
Version:	0.22
Release:	5
License:	Public Domain
Group:		Libraries
Source0:	ftp://ftp.lysator.liu.se/pub/ident/libs/%{name}-%{version}.tar.gz
# Source0-md5:	218b6706e574ca5b41a0a675cf1860eb
Patch0:		%{name}-DESTDIR.patch
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
%patch0 -p1

%build
%{__make} all \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC -DHAVE_ANSIHEADERS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_mandir}/man3,%{_includedir}}

%{__make} install \
	INSTROOT=$RPM_BUILD_ROOT%{_prefix} \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libident.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libident.so
%{_includedir}/ident.h
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libident.a
