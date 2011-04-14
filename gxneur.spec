Name:		gxneur
Version:	0.12.0
Release:	%mkrel 2
License:	GPLv2
URL:		http://www.xneur.ru
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:	gtk2-devel libglade2-devel
BuildRequires:	xneur-devel = %{version}
BuildRequires:	libGConf2-devel GConf2
BuildRequires:	gettext-devel
Source:		%{name}-%{version}.tar.bz2
Patch0:		gxneur-0.12.0-cflags.patch
Requires:	xneur = %{version}
Group:		System/X11
Summary:	X Neural Switcher - GTK2 interface

%description
X Neural Switcher (http://www.xneur.ru).
Automatical switcher of keyboard layout (GTK2 frontend).

%prep
%setup -qn %{name}-%{version}
%patch0 -p0

%build
autoreconf -fi
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name

#small_hack
cp -f pixmaps/ru.png %{buildroot}%{_datadir}/%name/pixmaps/ru\(winkeys\).png

install -dm 755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%name.desktop << EOF
[Desktop Entry]
Name=GXNeur
GenericName=X Neural Switcher (GTK)
Comment=X Neural Switcher (xneur) allow you to convert any text, typed in wrong keyboard layout just in-place for any X pplication.
Icon=gxneur
Exec=gxneur
Terminal=false
Type=Application
Categories=GTK;GNOME;Utility;
StartupNotify=false
EOF

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_iconsdir}/hicolor/*/*/*
%{_datadir}/applications/*.desktop
