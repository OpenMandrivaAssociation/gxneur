Name:		gxneur
Version:	0.17.0
Release:	1
License:	GPLv2
URL:		http://www.xneur.ru
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:	%{_lib}xneur-devel = %{version}
BuildRequires:	pkgconfig(gconf-2.0)
Source0:	%{name}-%{version}.tar.gz
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
./configure --prefix=/usr --libdir=%{_libdir}
%make

%install
%makeinstall
#small_hack
mkdir -p %{buildroot}%{_datadir}/%name/pixmaps/
pushd pixmaps
  for i in hicolor_apps_48x48_gxneur-*; do cp -f $i ${i/hicolor_apps_48x48_gxneur-/}; done
popd
cp -f pixmaps/ru.png %{buildroot}%{_datadir}/%name/pixmaps/ru\(winkeys\).png

install -dm 755 %{buildroot}%{_datadir}/applications
cat > %name.desktop << EOF
[Desktop Entry]
 Encoding=UTF-8
 Name=GXNeur
 GenericName=X Neural Switcher (GTK)
 Comment=X Neural Switcher (xneur) allow you to convert any text, typed in wrong keyboard layout just in-place for any X pplication.
 Icon=%{_datadir}/%{name}/pixmaps/gxneur.png
 Exec=gxneur --keyboard-properties="/usr/bin/kcmshell4 kcm_keyboard || /usr/bin/gnome-control-center"
 Terminal=false
 Type=Application
 Categories=GTK;GNOME;Application;Utility;
 StartupNotify=false
EOF
echo %{buildroot}%{_datadir}/applications/
install -m 0644 %name.desktop \
%{buildroot}%{_datadir}/applications/%name.desktop

#dirty hack for resolve conflict with hicolor-icon-theme

rm -f %{buildroot}%{_datadir}/icons/hicolor/icon-theme.cache
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/*
%{_iconsdir}/*
%{_datadir}/%{name}/*
%{_datadir}/applications/*.desktop
#%{_datadir}/%{name}/glade/*
#%{_iconsdir}/hicolor/*/*
#%{_datadir}/%{name}/pixmaps/*.png
%{_mandir}/man1/*
#% {_gnomedir}/share/icons/hicolor/*
