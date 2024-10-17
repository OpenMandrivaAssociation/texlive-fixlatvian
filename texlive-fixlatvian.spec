Name:		texlive-fixlatvian
Version:	21631
Release:	2
Summary:	Improve Latvian language support in XeLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/fixlatvian
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixlatvian.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixlatvian.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixlatvian.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package offers improvement of the Latvian language support
in polyglossia, in particular in the area of the standard
classes.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/makeindex/fixlatvian/lv.ist
%{_texmfdistdir}/tex/xelatex/fixlatvian/fixlatvian.sty
%doc %{_texmfdistdir}/doc/xelatex/fixlatvian/Makefile
%doc %{_texmfdistdir}/doc/xelatex/fixlatvian/README
%doc %{_texmfdistdir}/doc/xelatex/fixlatvian/fixlatvian.pdf
#- source
%doc %{_texmfdistdir}/source/xelatex/fixlatvian/fixlatvian.dtx
%doc %{_texmfdistdir}/source/xelatex/fixlatvian/fixlatvian.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc source %{buildroot}%{_texmfdistdir}
