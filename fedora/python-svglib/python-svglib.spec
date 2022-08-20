Name:           python-svglib
Version:        1.4.1
Release:        %autorelease
Summary:        A pure-Python library for reading and converting SVG

# Berlin_location_map.svg and test_part.svg are under CC-BY-SA-3.0.
License:        LGPL-3.0-only
URL:            https://github.com/deeplook/svglib
Source:         %{pypi_source svglib}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Svglib is a pure-Python library for reading SVG files and converting them (to a
reasonable degree) to other formats using the ReportLab Open Source toolkit.

Used as a package you can read existing SVG files and convert them into
ReportLab Drawing objects that can be used in a variety of contexts, e.g. as
ReportLab Platypus Flowable objects or in RML. As a command-line tool it
converts SVG files into PDF ones (but adding other output formats like bitmap or
EPS is really easy and will be better supported, soon).

Tests include a huge W3C SVG test suite plus ca. 200 flags from Wikipedia and
some selected symbols from Wikipedia (with increasingly less pointing to missing
features).
}

%description %_description

%package -n python3-svglib
Summary:        %{summary}

%description -n python3-svglib %_description


%prep
%autosetup -p1 -n svglib-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files svglib


%check
# TODO: Solve tests before submitting to Fedora.
#pytest
%pyproject_check_import


%files -n python3-svglib -f %{pyproject_files}
%doc README.rst CHANGELOG.rst demos/
%license LICENSE.txt
%{_bindir}/svg2pdf
%{_mandir}/man1/svg2pdf.1.*


%changelog
%autochangelog
