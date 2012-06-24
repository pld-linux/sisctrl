# $Revision: 1.12 $, $Date: 2003/08/06 16:03:01
Summary:	sisctrl - tool for SiS cards
Summary(pl):	sisctrl - narz�dzie dla kart SiS
Name:		sisctrl
Version:	0.0.20051202
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.winischhofer.net/sis/%{name}-%{version}.tar.gz
# Source0-md5:	d9db755fe9fd40809b5c30d1ab286d62
URL:		http://www.winischhofer.net/linuxsisvga.shtml
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	pkgconfig
# some randr BR should be here to allow this feature
# in case of xlibs: libXrandr, libXv, libXxf86vm
# TODO: Xrandr is broken in XFree86, needs extra -lXrender -lX11 (or check fails)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sisctrl is a tool for setting/changing some driver parameters during
runtime on a SiS 300, 315 or 330 series based machine/card.

%description -l pl
sisctrl jest narz�dziem pozwalaj�cym zmienia� lub ustawia� niekt�re
parametry sterownika dla kart SiS 300, 315 lub 330 w czasie pracy
systemu.

%prep
%setup -q

%build
cp /usr/share/automake/config.sub .
%configure \
	--with-xv-path=/usr/X11R6/%{_lib}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install icons/48x48/sisctrl.png $RPM_BUILD_ROOT%{_pixmapsdir}
install extra/sisctrl.desktop $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
%{_mandir}/man1/*.1*
