# $Revision: 1.2 $, $Date: 2003/08/06 16:03:01
Summary:	sisctrl - tool for SiS cards
Name:		sisctrl
Version:	0.0.20040306
Release:	0.2
License:	BSD ?
Group:		X11/Applications
Source0:	http://www.winischhofer.net/sis/%{name}-%{version}.tar.gz
# Source0-md5:	c9e51050ad0d8411d47b892de0b95a4e
URL:		http://www.winischhofer.net/linuxsisvga.shtml
BuildRequires:	XFree86-devel
BuildRequires:	gtk+2-devel
BuildRequires:	pkgconfig
# some randr BR should be here to allow this feature
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sisctrl is a tool for setting/changing some driver parameters during
runtime on a SiS 300, 315 or 330 series based machine/card.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install icons/64x64/sisctrl.png $RPM_BUILD_ROOT%{_pixmapsdir}
install extra/sisctrl.desktop $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_desktopdir}/*.desktop
%attr(644,root,root) %{_pixmapsdir}/*.png
%{_mandir}/man1/*.1*
