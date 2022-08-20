Name:           python-anyascii
Version:        0.3.1
Release:        %autorelease
Summary:        Unicode to ASCII transliteration

License:        ISC
URL:            https://anyascii.com/
Source:         %{pypi_source anyascii}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Converts Unicode characters to their best ASCII representation

AnyAscii provides ASCII-only replacement strings for practically all Unicode
characters. Text is converted character-by-character without considering the
context. The mappings for each script are based on popular existing romanization
systems. Symbolic characters are converted based on their meaning or appearance.
All ASCII characters in the input are left unchanged, every other character is
replaced with printable ASCII characters. Unknown characters and some known
characters are replaced with an empty string and removed.
}

%description %_description

%package -n python3-anyascii
Summary:        %{summary}

%description -n python3-anyascii %_description


%prep
%autosetup -p1 -n anyascii-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files anyascii


%check
%pytest


%files -n python3-anyascii -f %{pyproject_files}
%doc README.md
%license LICENSE


%changelog
%autochangelog
