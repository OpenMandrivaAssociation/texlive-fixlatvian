# revision 21631
# category Package
# catalog-ctan /macros/xetex/latex/fixlatvian
# catalog-date 2011-03-06 19:31:04 +0100
# catalog-license lppl1.3
# catalog-version 1a
Name:		texlive-fixlatvian
Version:	1a
Release:	7
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1a-2
+ Revision: 751914
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1a-1
+ Revision: 718449
- texlive-fixlatvian
- texlive-fixlatvian
- texlive-fixlatvian
- texlive-fixlatvian

