Summary:	LibIdent - Library
Summary(pl):	LibIdent - Biblioteka
Name:		libident
Version:	0.22
Release:	2
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	Библиотеки
Group(uk):	Б╕бл╕отеки
Source0:	ftp://ftp.lysator.liu.se/pub/ident/libs/%name-%version.tar.gz
Patch0:		%{name}-DESTDIR.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibIdent is a library which provides ident support in application.

%description -l pl
LibIdent jest bibliotek╠ udostЙpniaj╠c╠ interfejs do usЁugi ident.

%package devel
Summary:	LibIdent - header files
Summary(pl):	LibIdent - pliki nagЁСwkowe
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name} = %{version}

%description devel
LibIdent - header files.

%description -l pl devel
LibIdent - pliki nagЁСwkowe.

%package static
Summary:	LibIdent - Static Library
Summary(pl):	LibIdent - Biblioteka statyczna
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name}-devel = %{version}

%description static
LibIdent - Static Library.

%description -l pl static
LibIdent - Biblioteka statyczna.

%prep
%setup -q
%patch0 -p1

%build
%{__make} CFLAGS="%{rpmcflags}" linux

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_mandir}/man3,%{_includedir}}

%{__make} INSTROOT=$RPM_BUILD_ROOT%{_prefix} install

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libident.so

%files devel
%defattr(644,root,root,755)
%doc *.gz
%{_includedir}/ident.h
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libident.a
