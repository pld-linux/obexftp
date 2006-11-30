%include	/usr/lib/rpm/macros.perl
Summary:	File copying over the Object Exchange (OBEX) protocol
Summary(pl):	Kopiowanie plików z wykorzystaniem protoko³u Object Exchange (OBEX)
Name:		obexftp
Version:	0.20
Release:	2
License:	GPL v2
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/openobex/%{name}-%{version}.tar.bz2
# Source0-md5:	86224a7a1880c25e9ba0b8997a97d299
Patch0:		%{name}-no_server.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-perl.patch
Patch3:		%{name}-py-m4.patch
URL:		http://triq.net/obex/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bluez-libs-devel
BuildRequires:	libtool
BuildRequires:	openobex-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Free open source application for file copying over the Object Exchange
(OBEX) protocol.

%description -l pl
Wolnodostêpna aplikacja s³u¿±ca do kopiowania plików z wykorzystaniem
protoko³u Object Exchange (OBEX).

%package libs
Summary:	ObexFTP libraries
Summary(pl):	Biblioteki ObexFTP
Group:		Libraries

%description libs
ObexFTP libraries.

%description libs -l pl
Biblioteki ObexFTP.

%package devel
Summary:	Header files for ObexFTP
Summary(es):	Ficheros de cabecera para ObexFTP
Summary(pl):	Pliki nag³ówkowe ObexFTP
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	bluez-libs-devel
Requires:	openobex-devel

%description devel
The header files are only needed for development of programs based on
ObexFTP.

%description devel -l pl
W pakiecie tym znajduj± siê pliki nag³ówkowe, przeznaczone do
rozwijania programów bazuj±cych na bibliotekach ObexFTP.

%package static
Summary:	Static ObexFTP library
Summary(es):	Biblioteca estática de ObexFTP
Summary(pl):	Biblioteka statyczna ObexFTP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ObexFTP library.

%description static -l pl
Biblioteka statyczna ObexFTP.

%package -n perl-obexftp
Summary:	Perl binding for ObexFTP library
Summary(pl):	Wi±zanie Perla dla biblioteki ObexFTP
Group:		Development/Languages/Perl
Requires:	%{name}-libs = %{version}-%{release}

%description -n perl-obexftp
Perl binding for ObexFTP library.

%description -n perl-obexftp -l pl
Wi±zanie Perla dla biblioteki ObexFTP.

%package -n python-obexftp
Summary:	Python binding for ObexFTP library
Summary(pl):	Wi±zanie Pythona dla biblioteki ObexFTP
Group:		Libraries/Python
Requires:	%{name}-libs = %{version}-%{release}
%pyrequires_eq	python-libs

%description -n python-obexftp
Python binding for ObexFTP library.

%description -n python-obexftp -l pl
Wi±zanie Pythona dla biblioteki ObexFTP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/OBEXFTP/.packlist
rm -f $RPM_BUILD_ROOT%{py_sitedir}/obexftp/_obexftp.{la,a}
rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/obexftp/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/obexftp*.html README* NEWS THANKS TODO AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files -n perl-obexftp
%defattr(644,root,root,755)
%{perl_vendorarch}/OBEXFTP.pm
%dir %{perl_vendorarch}/auto/OBEXFTP
%attr(755,root,root) %{perl_vendorarch}/auto/OBEXFTP/OBEXFTP.so
%{perl_vendorarch}/auto/OBEXFTP/OBEXFTP.bs

%files -n python-obexftp
%defattr(644,root,root,755)
%dir %{py_sitedir}/obexftp
%attr(755,root,root) %{py_sitedir}/obexftp/_obexftp.so
%dir %{py_sitescriptdir}/obexftp
%{py_sitescriptdir}/obexftp/__init__.py[co]
