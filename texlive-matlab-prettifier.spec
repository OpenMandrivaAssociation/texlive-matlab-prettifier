Name:		texlive-matlab-prettifier
Version:	34323
Release:	1
Summary:	Pretty-print Matlab source code
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/matlab-prettifier
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/matlab-prettifier.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/matlab-prettifier.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/matlab-prettifier.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package extends the facilities of the listings package, to
pretty-print Matlab and Octave source code. (Note that support
of Octave syntax is not complete.)

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/matlab-prettifier
%{_texmfdistdir}/tex/latex/matlab-prettifier
%doc %{_texmfdistdir}/doc/latex/matlab-prettifier

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
