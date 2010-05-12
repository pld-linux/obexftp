%include	/usr/lib/rpm/macros.perl
Summary:	File copying over the Object Exchange (OBEX) protocol
Summary(pl.UTF-8):	Kopiowanie plików z wykorzystaniem protokołu Object Exchange (OBEX)
Name:		obexftp
Version:	0.23
Release:	1
License:	GPL v2+ (server, bindings), LGPL v2+ (libraries)
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/openobex/%{name}-%{version}.tar.bz2
# Source0-md5:	f20762061b68bc921e80be4aebc349eb
Patch0:		%{name}-no_server.patch
Patch1:		%{name}-perl.patch
Patch2:		%{name}-nostress.patch
Patch3:		%{name}-ruby1.9.patch
URL:		http://triq.net/obex/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bluez-libs-devel
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	openobex-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	tcl-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Free open source application for file copying over the Object Exchange
(OBEX) protocol.

%description -l pl.UTF-8
Wolnodostępna aplikacja służąca do kopiowania plików z wykorzystaniem
protokołu Object Exchange (OBEX).

%package libs
Summary:	ObexFTP libraries
Summary(pl.UTF-8):	Biblioteki ObexFTP
License:	LGPL v2+
Group:		Libraries

%description libs
ObexFTP libraries.

%description libs -l pl.UTF-8
Biblioteki ObexFTP.

%package devel
Summary:	Header files for ObexFTP
Summary(es.UTF-8):	Ficheros de cabecera para ObexFTP
Summary(pl.UTF-8):	Pliki nagłówkowe ObexFTP
License:	LGPL v2+
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	bluez-libs-devel
Requires:	openobex-devel

%description devel
The header files are only needed for development of programs based on
ObexFTP.

%description devel -l pl.UTF-8
W pakiecie tym znajdują się pliki nagłówkowe, przeznaczone do
rozwijania programów bazujących na bibliotekach ObexFTP.

%package static
Summary:	Static ObexFTP library
Summary(es.UTF-8):	Biblioteca estática de ObexFTP
Summary(pl.UTF-8):	Biblioteka statyczna ObexFTP
License:	LGPL v2+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ObexFTP library.

%description static -l pl.UTF-8
Biblioteka statyczna ObexFTP.

%package -n perl-obexftp
Summary:	Perl binding for ObexFTP library
Summary(pl.UTF-8):	Wiązanie Perla dla biblioteki ObexFTP
License:	GPL v2+
Group:		Development/Languages/Perl
Requires:	%{name}-libs = %{version}-%{release}

%description -n perl-obexftp
Perl binding for ObexFTP library.

%description -n perl-obexftp -l pl.UTF-8
Wiązanie Perla dla biblioteki ObexFTP.

%package -n python-obexftp
Summary:	Python binding for ObexFTP library
Summary(pl.UTF-8):	Wiązanie Pythona dla biblioteki ObexFTP
License:	GPL v2+
Group:		Libraries/Python
Requires:	%{name}-libs = %{version}-%{release}
%pyrequires_eq	python-libs

%description -n python-obexftp
Python binding for ObexFTP library.

%description -n python-obexftp -l pl.UTF-8
Wiązanie Pythona dla biblioteki ObexFTP.

%package -n ruby-obexftp
Summary:	Ruby binding for ObexFTP library
Summary(pl.UTF-8):	Wiązanie języka Ruby dla biblioteki ObexFTP
License:	GPL v2+
Group:		Development/Languages
Requires:	%{name}-libs = %{version}-%{release}
%{?ruby_mod_ver_requires_eq}

%description -n ruby-obexftp
Ruby binding for ObexFTP library.

%description -n ruby-obexftp -l pl.UTF-8
Wiązanie języka Ruby dla biblioteki ObexFTP.

%package -n tcl-obexftp
Summary:	Tcl binding for ObexFTP library
Summary(pl.UTF-8):	Wiązanie Tcl-a dla biblioteki ObexFTP
License:	GPL v2+
Group:		Development/Languages
Requires:	%{name}-libs = %{version}-%{release}
Requires:	tcl

%description -n tcl-obexftp
Tcl binding for ObexFTP library.

%description -n tcl-obexftp -l pl.UTF-8
Wiązanie Tcl-a dla biblioteki ObexFTP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# hack for -L/usr/%{_lib} before -L../../obexftp/.libs
ln -sf ../../obexftp/.libs/libobexftp.so swig/ruby

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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/obexftp.{la,a}
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/OBEXFTP/.packlist
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	-n tcl-obexftp -p /sbin/ldconfig
%postun	-n tcl-obexftp -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/obexftp*.html README* NEWS THANKS TODO AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/obexftp
%attr(755,root,root) %{_bindir}/obexftpd
%{_mandir}/man1/obexftp.1*
%{_mandir}/man1/obexftpd.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbfb.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbfb.so.0
%attr(755,root,root) %{_libdir}/libmulticobex.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmulticobex.so.1
%attr(755,root,root) %{_libdir}/libobexftp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libobexftp.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbfb.so
%attr(755,root,root) %{_libdir}/libmulticobex.so
%attr(755,root,root) %{_libdir}/libobexftp.so
%{_libdir}/libbfb.la
%{_libdir}/libmulticobex.la
%{_libdir}/libobexftp.la
%{_includedir}/bfb
%{_includedir}/multicobex
%{_includedir}/obexftp
%{_pkgconfigdir}/obexftp.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libbfb.a
%{_libdir}/libmulticobex.a
%{_libdir}/libobexftp.a

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
%{py_sitedir}/obexftp/__init__.py[co]
%{py_sitedir}/obexftp-*.egg-info

%files -n ruby-obexftp
%defattr(644,root,root,755)
%attr(755,root,root) %{ruby_sitearchdir}/obexftp.so

%files -n tcl-obexftp
%defattr(644,root,root,755)
# -avoid-version missing
%attr(755,root,root) %{_libdir}/obexftp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/obexftp.so.0
%attr(755,root,root) %{_libdir}/obexftp.so
