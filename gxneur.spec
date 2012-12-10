%define _gnomedir	/usr
%define _datarootdir	%{_gnomedir}/share/gxneur
%define _pixmaps	%{_gnomedir}/share/gxneur/pixmaps
%define _locale		%{_datarootdir}/locale
%define rel 2


Name:		gxneur
Version:	0.16.0
Release:	%mkrel %{rel}
License:	GPLv2
URL:		http://www.xneur.ru
BuildRequires:	gtk2-devel pkgconfig(glib-2.0) pkgconfig(libglade-2.0)
BuildRequires:  pkgconfig(libpcre) %{_lib}xneur-devel = %{version} pkgconfig(gconf-2.0)
Source0:	http://dists.xneur.ru/release-%{version}/tgz/%{name}-%{version}.tar.bz2
Patch0:		trayicon_unused_env.patch
Requires:	xneur = %{version}
Group:		System/X11
Summary:	X Neural Switcher - GTK2 interface

%description
X Neural Switcher (http://www.xneur.ru).
Automatical switcher of keyboard layout (GTK2 frontend).

%prep
%setup -n %{name}-%{version} -q
#% patch0 -p0

%build
./configure --prefix=%{_gnomedir} --libdir=%{_libdir}
%make

%install
%makeinstall
#small_hack
mkdir -p %{buildroot}%{_datadir}/%name/pixmaps/
cp -f pixmaps/ru.png %{buildroot}%{_datadir}/%name/pixmaps/ru\(winkeys\).png

install -dm 755 %{buildroot}%{_datadir}/applications
cat > %name.desktop << EOF
[Desktop Entry]
 Encoding=UTF-8
 Name=GXNeur
 GenericName=X Neural Switcher (GTK)
 Comment=X Neural Switcher (xneur) allow you to convert any text, typed in wrong keyboard layout just in-place for any X pplication.
 Icon=%{_pixmaps}/gxneur.png
 Exec=gxneur
 Terminal=false
 Type=Application
 Categories=GTK;GNOME;Application;Utility;
 StartupNotify=false
EOF
install -m 0644 %name.desktop \
%{buildroot}%{_datadir}/applications/%name.desktop

#dirty hack for resolve conflict with hicolor-icon-theme

rm -f %{buildroot}%{_gnomedir}/share/icons/hicolor/icon-theme.cache
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README TODO
%{_gnomedir}/bin/*
%{_pixmaps}/*
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/glade/*
%{_iconsdir}/hicolor/*/*
%{_datadir}/%{name}/pixmaps/*.png
%{_mandir}/man1/*
#% {_gnomedir}/share/icons/hicolor/*
