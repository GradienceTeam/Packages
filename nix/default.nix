{ lib
, meson
, ninja
, fetchFromGitHub
, gdk-pixbuf
, gettext
, glib
, gnome
, gnome-desktop
, gobject-introspection
, gsettings-desktop-schemas
, gtk4
, itstool
, libadwaita
, libportal-gtk4
, libsoup_3
, pkg-config
, python3Packages
, wrapGAppsHook
, blueprint-compiler
, desktop-file-utils
}:

python3Packages.buildPythonApplication rec {
  pname = "gradience";
  version = "0.4.1";
  format = "other";
  strictDeps = false; # https://github.com/NixOS/nixpkgs/issues/56943

  src = fetchFromGitHub {
    owner = "GradienceTeam";
    repo = "gradience";
    rev = version;
    sha256 = "sha256-xR3wPU0ax9U4995GckC8UGJqrUErd+jS5z3D/jWCdXQ=";
  };

  nativeBuildInputs = [
    gettext
    gobject-introspection
    itstool
    meson
    ninja
    pkg-config
    wrapGAppsHook
    blueprint-compiler
    desktop-file-utils
  ];

  buildInputs = [
    gdk-pixbuf
    glib
    gnome-desktop
    gnome.gnome-settings-daemon
    gnome.gnome-shell
    gnome.gnome-shell-extensions
    gnome.mutter
    gsettings-desktop-schemas
    gtk4
    libadwaita
    libportal-gtk4
    libsoup_3
    
  ];

  pythonPath = with python3Packages; [
    pygobject3
    anyascii
    cssutils
    sphinx-jinja
    lxml
    pillow
    pluggy
    regex
    svglib
    Yapsy
    libsass
    (
    buildPythonPackage rec {
      pname = "material-color-utilities-python";
      version = "0.1.5";
      src = fetchPypi {
        inherit pname version;
        sha256 = "sha256-PG8C585wWViFRHve83z3b9NijHyV+iGY2BdMJpyVH64=";
      };
      doCheck = false;
      propagatedBuildInputs = [
        pkgs.python3Packages.pillow
        pkgs.python3Packages.regex
      ];
    }
  )    
  ];
  
  dontWrapGApps = true;
  
  preFixup = ''
    makeWrapperArgs+=("''${gappsWrapperArgs[@]}")
  '';

  meta = with lib; {
    homepage = "https://gradienceteam.github.io";
    description = "Change the look of Adwaita, with ease";
    maintainers = ["0xMRTT"];
    license = licenses.gpl3Plus;
    platforms = platforms.linux;
  };
}
