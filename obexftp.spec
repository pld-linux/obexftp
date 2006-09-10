Summary:	File copying over the Object Exchange (OBEX) protocol
Summary(pl):	Kopiowanie plik�w z wykorzystaniem protoko�u Object Exchange (OBEX)
Name:		obexftp
Version:	0.20
Release:	1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/openobex/%{name}-%{version}.tar.bz2
# Source0-md5:	86224a7a1880c25e9ba0b8997a97d299
Patch0:		%{name}-no_server.patch
URL:		http://triq.net/obex/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bluez-libs-devel
BuildRequires:	libtool
BuildRequires:	openobex-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         filterout_ld    (-Wl,)?--as-needed

%description
Free open source application for file copying over the Object Exchange
(OBEX) protocol.

%description -l pl
Wolnodost�pna aplikacja s�u��ca do kopiowania plik�w z wykorzystaniem
protoko�u Object Exchange (OBEX).

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
Summary(pl):	Pliki nag��wkowe ObexFTP
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
The header files are only needed for development of programs based on
ObexFTP.

%description devel -l pl
W pakiecie tym znajduj� si� pliki nag��wkowe, przeznaczone do
rozwijania program�w bazuj�cych na bibliotekach ObexFTP.

%package static
Summary:	Static ObexFTP library
Summary(es):	Biblioteca est�tica de ObexFTP
Summary(pl):	Biblioteka statyczna ObexFTP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ObexFTP library.

%description static -l pl
Biblioteka statyczna ObexFTP.

%prep
%setup -q
%patch0 -p1

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

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/obexftp* README* NEWS THANKS TODO AUTHORS ChangeLog
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
