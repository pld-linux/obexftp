Summary:	File copying over the Object Exchange (OBEX) protocol
Summary(pl):	Kopiowanie plików z wykorzystaniem protoko³u Object Exchange (OBEX)
Name:		obexftp
Version:	0.10.3
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/openobex/%{name}-%{version}.tar.gz
URL:		http://triq.net/obex/
BuildRequires:	openobex-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Free open source application for file copying over the Object Exchange
(OBEX) protocol.

%description
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
Requires:	%{name}-libs = %{version}

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
Requires:	%{name}-devel = %{version}

%description static
Static ObexFTP library.

%description static -l pl
Biblioteka statyczna ObexFTP.

%prep
%setup -q

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

%files
%defattr(644,root,root,755)
%doc doc/*.html doc/*.png README* THANKS TODO AUTHORS ChangeLog
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
