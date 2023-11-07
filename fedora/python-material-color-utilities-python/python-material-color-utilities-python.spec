%global         pypi_name material-color-utilities-python
%global         module material_color_utilities_python

Name:           python-%{pypi_name}
Version:        0.1.5
Release:        %autorelease
Summary:        Python port of material-color-utilities used for Material You colors

License:        Apache-2.0
URL:            https://github.com/avanishsubbiah/material-color-utilities-python
Source:         %{pypi_source %{pypi_name}}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  git-core

Patch0:         0001-Removing-Pillow-version-requirement.patch

%global _description %{expand:
Python port of material-color-utilities used for Material You colors.

Original source code:
https://github.com/material-foundation/material-color-utilities

NOTE: This is an unofficial port of material-color-utilities from JavaScript to
Python.
}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -S git -n %{pypi_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{module}


%check
%pyproject_check_import %{module}


%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.md


%changelog
%autochangelog
