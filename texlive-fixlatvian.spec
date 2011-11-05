# revision 21631
# category Package
# catalog-ctan /macros/xetex/latex/fixlatvian
# catalog-date 2011-03-06 19:31:04 +0100
# catalog-license lppl1.3
# catalog-version 1a
Name:		texlive-fixlatvian
Version:	1a
Release:	1
Summary:	Improve Latvian language support in XeLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/latex/fixlatvian
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixlatvian.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixlatvian.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixlatvian.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package offers improvement of the Latvian language support
in polyglossia, in particular in the area of the standard
classes.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
