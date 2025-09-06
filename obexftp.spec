#
# Conditional build:
%bcond_without	static_libs	# static libraries

Summary:	File copying over the Object Exchange (OBEX) protocol
Summary(pl.UTF-8):	Kopiowanie plików z wykorzystaniem protokołu Object Exchange (OBEX)
Name:		obexftp
Version:	0.24.2
Release:	1
License:	GPL v2+ (server, bindings), LGPL v2+ (libraries)
Group:		Applications/Communications
Source0:	https://downloads.sourceforge.net/openobex/%{name}-%{version}-Source.tar.gz
# Source0-md5:	157a9d1b2ed220203f7084db906de73c
Patch0:		%{name}-python.patch
Patch1:		%{name}-perl.patch
URL:		http://dev.zuckschwerdt.org/openobex/wiki/ObexFtp/
BuildRequires:	asciidoc
BuildRequires:	bluez-libs-devel
BuildRequires:	gettext-tools
BuildRequires:	openobex-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	tcl-devel
BuildRequires:	xmlto
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Free open source application for file copying over the Object Exchange
(OBEX) protocol.

%description -l pl.UTF-8
Wolnodostępna aplikacja służąca do kopiowania plików z wykorzystaniem
protokołu Object Exchange (OBEX).

%package -n obexfs
Summary:	ObexFTP filesystem
Summary(pl.UTF-8):	System plików ObexFTP
Group:		Applications/System

%description -n obexfs
FUSE based filesystem using ObexFTP.

%description -n obexfs -l pl.UTF-8
System plików używający ObexFTP oparty na FUSE.

%package libs
Summary:	OBEX file transfer libraries
Summary(pl.UTF-8):	Biblioteki transmisji plików OBEX
License:	LGPL v2+
Group:		Libraries

%description libs
OBEX file transfer libraries.

%description libs -l pl.UTF-8
Biblioteki transmisji plików OBEX.

%package devel
Summary:	Header files for OBEX file transfer libraries
Summary(es.UTF-8):	Ficheros de cabecera para ObexFTP
Summary(pl.UTF-8):	Pliki nagłówkowe transmisji plików OBEX
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
Summary:	Static OBEX file transfer libraries
Summary(es.UTF-8):	Biblioteca estática de ObexFTP
Summary(pl.UTF-8):	Statyczne biblioteki transmisji plików OBEX
License:	LGPL v2+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static OBEX file transfer libraries.

%description static -l pl.UTF-8
Statyczne biblioteki transmisji plików OBEX.

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
%setup -q -n %{name}-%{version}-Source
%patch -P0 -p1
%patch -P1 -p1

%build
%if %{with static_libs}
install -d build-static
cd build-static
%cmake .. \
	-DBUILD_SHARED_LIBS=OFF \
	-DENABLE_PERL=OFF \
	-DENABLE_PYTHON=OFF \
	-DENABLE_RUBY=OFF

for dir in bfb multicobex obexftp ; do
	%{__make} -C $dir
done
cd ..
%endif

install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_INCLUDEDIR=include \
	-DCMAKE_INSTALL_LIBDIR=%{_lib} \
	-DENABLE_TCL=ON \
	-DPYTHON_EXECUTABLE=%{__python}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%if %{with static_libs}
for dir in bfb multicobex obexftp ; do
	%{__make} -C build-static/$dir install \
		DESTDIR=$RPM_BUILD_ROOT
done
%endif

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	-n tcl-obexftp -p /sbin/ldconfig
%postun	-n tcl-obexftp -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog License.txt NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/obexftp
%attr(755,root,root) %{_bindir}/obexftpd
%{_mandir}/man1/obexftp.1*
%{_mandir}/man1/obexftpd.1*

%files -n obexfs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/obexautofs
%attr(755,root,root) %{_bindir}/obexfs

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbfb.so.*.*.*
%ghost %{_libdir}/libbfb.so.1
%attr(755,root,root) %{_libdir}/libmulticobex.so.*.*.*
%ghost %{_libdir}/libmulticobex.so.1
%attr(755,root,root) %{_libdir}/libobexftp.so.*.*.*
%ghost %{_libdir}/libobexftp.so.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/libbfb.so
%{_libdir}/libmulticobex.so
%{_libdir}/libobexftp.so
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

%files -n python-obexftp
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_obexftp.so
%{py_sitedir}/obexftp.py[co]

%files -n ruby-obexftp
%defattr(644,root,root,755)
%attr(755,root,root) %{ruby_vendorarchdir}/obexftp.so

%files -n tcl-obexftp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/obexftp.so
