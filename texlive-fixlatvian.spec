%global tl_name fixlatvian
%global tl_revision 21631

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1a
Release:	%{tl_revision}.1
Summary:	Improve Latvian language support in XeLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/fixlatvian
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fixlatvian.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fixlatvian.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fixlatvian.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package offers improvement of the Latvian language support in
polyglossia, in particular in the area of the standard classes.

