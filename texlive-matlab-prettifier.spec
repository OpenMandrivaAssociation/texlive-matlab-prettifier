%global tl_name matlab-prettifier
%global tl_revision 34323

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	Pretty-print Matlab source code
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/matlab-prettifier
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/matlab-prettifier.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/matlab-prettifier.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/matlab-prettifier.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package extends the facilities of the listings package, to pretty-
print Matlab and Octave source code. (Note that support of Octave syntax
is not complete.)

