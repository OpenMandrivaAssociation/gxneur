%define _gnomedir	/usr
%define _datarootdir	%{_gnomedir}/share/gxneur
%define _pixmaps	%{_gnomedir}/share/gxneur/pixmaps
%define _locale		%{_datarootdir}/locale
%define rel 1


Name:		gxneur
Version:	0.11.1
Release:	%mkrel %{rel}
License:	GPLv2
URL:		http://www.xneur.ru
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:	gtk2-devel glib2-devel libglade2-devel
BuildRequires:  pcre-devel xneur-devel = %{version} libGConf2-devel
Source:		%{name}-%{version}.tar.bz2
Requires:	xneur = %{version}
Group:		System/X11
Summary:	X Neural Switcher - GTK2 interface

%description
X Neural Switcher (http://www.xneur.ru).
Automatical switcher of keyboard layout (GTK2 frontend).

%prep
%setup -n %{name}-%{version} -q

%build
./configure --prefix=%{_gnomedir} --libdir=%{_libdir}
make %{?jobs:-j %jobs}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
#small_hack
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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO
%{_gnomedir}/bin/*
%{_pixmaps}/*
%{_datadir}/applications/*.desktop
%{_datadir}/locale/*
%{_datarootdir}/glade/*
%{_gnomedir}/share/man/man1/*
%{_gnomedir}/share/icons/hicolor/*
