Summary:	LibIdent - Library
Summary(pl):	LibIdent - Biblioteka
Name:		libident
Version:	0.22
Release:	1
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://ftp.lysator.liu.se/pub/ident/libs/%name-%version.tar.gz
Patch0:		%{name}-DESTDIR.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr

%description
LibIdent is a library which provides ident support in application.

%description -l pl
LibIdent jest biblioteką udostępniającą interfejs do usługi ident.

%package devel
Summary:	LibIdent - header files
Summary(pl):	LibIdent - pliki nagłówkowe
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
LibIdent - header files

%description -l pl devel
LibIdent - pliki nagłówkowe

%package static
Summary:	LibIdent - Static Library
Summary(pl):	LibIdent - Biblioteka statyczna
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
LibIdent - Static Library

%description -l pl static
LibIdent - Biblioteka statyczna

%prep
%setup -q

%patch -p1

%build
%{__make} CFLAGS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g}" linux

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_mandir}/man3,%{_includedir}}

%{__make} INSTROOT=$RPM_BUILD_ROOT%{_prefix} install

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
	README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%{_libdir}/libident.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/ident.h
%{_mandir}/man3/ident*gz

%files static
%defattr(644,root,root,755)
%{_libdir}/libident.a
