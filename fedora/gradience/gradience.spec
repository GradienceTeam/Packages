%global         forgeurl https://github.com/GradienceTeam/Gradience
%global         uuid com.github.GradienceTeam.Gradience

Name:           gradience
Version:        0.2.2
Release:        %autorelease
Summary:        Change the look of Adwaita, with ease
BuildArch:      noarch

%global         tag %{version}
%forgemeta

License:        GPL-3.0-or-later
URL:            https://gradienceteam.github.io/
Source0:        %{forgesource}

BuildRequires:  meson
BuildRequires:  blueprint-compiler
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.2
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(libportal-gtk4)
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-devel
BuildRequires:  python3dist(anyascii)
BuildRequires:  python3dist(material-color-utilities-python)
BuildRequires:  python3dist(svglib)
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme
Requires:       gtk4
Requires:       libadwaita >= 1.2
Requires:       libportal
Requires:       libportal-gtk4
Requires:       python3-gobject
Requires:       python3dist(anyascii)
Requires:       python3dist(material-color-utilities-python)
Requires:       python3dist(svglib)

%description
Gradience is a tool for customizing Libadwaita applications and the adw-gtk3 theme.

With Gradience you can:
* Change any color of Adwaita theme
* Apply Material 3 colors from wallpaper
* Use other users presets
* Change advanced options with CSS
* Extend functionality using plugins


%prep
%forgeautosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{uuid}.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{uuid}.desktop


%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/gradience
%{python3_sitelib}/gradience
%{_datadir}/gradience
%{_datadir}/appdata/%{uuid}.appdata.xml
%{_datadir}/applications/%{uuid}.desktop
%{_datadir}/glib-2.0/schemas/%{uuid}.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg

%changelog
%autochangelog
