Summary:	Library integrating clutter with Box2d
Summary(pl.UTF-8):	Biblioteka integrująca clutter z Box2d
Name:		clutter-box2d
Version:	0.10.0
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://source.clutter-project.org/sources/clutter-box2d/0.10/%{name}-%{version}.tar.bz2
# Source0-md5:	51618976ca6a5d536c4eac5f0e120d9d
URL:		http://www.clutter-project.org/
BuildRequires:	clutter-devel >= 1.0.0
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gobject-introspection-devel >= 0.6.3
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	pkgconfig
Requires:	clutter >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Clutter-Box2d is a glue layer between clutter and box2d that provides
a special group where the actors can be set to be static or dynamic in
regard to a physics simulation. The source tree currently contains an
embedded version of box2d trunk.

%description -l pl.UTF-8
Clutter-Box2d to warstwa łącząca biblioteki clutter i box2d,
udostępniająca specjalną grupę, gdzie można ustawić postaci jako
statyczne lub dynamiczne ze względu na symulację fizyki. Źródła
aktualnie zawierają wersję trunk biblioteki box2d.

%package devel
Summary:	Header files for clutter-box2d library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki clutter-box2d
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	clutter-devel >= 1.0.0

%description devel
Header files for clutter-box2d library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki clutter-box2d.

%package static
Summary:	Static clutter-box2d library
Summary(pl.UTF-8):	Statyczna biblioteka clutter-box2d
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static clutter-box2d library.

%description static -l pl.UTF-8
Statyczna biblioteka clutter-box2d.

%package apidocs
Summary:	clutter-box2d API documentation
Summary(pl.UTF-8):	Dokumentacja API clutter-box2d
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
clutter-box2d API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API clutter-box2d.

%prep
%setup -q

%build
%configure \
	--enable-gtk-doc \
	--enable-static \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libclutter-box2d-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclutter-box2d-0.10.so.0
%{_libdir}/girepository-1.0/ClutterBox2D-0.10.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclutter-box2d-0.10.so
%{_libdir}/libclutter-box2d-0.10.la
%{_includedir}/clutter-1.0/clutter-box2d
%{_pkgconfigdir}/clutter-box2d-0.10.pc
%{_datadir}/gir-1.0/ClutterBox2D-0.10.gir

%files static
%defattr(644,root,root,755)
%{_libdir}/libclutter-box2d-0.10.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/clutter-box2d
