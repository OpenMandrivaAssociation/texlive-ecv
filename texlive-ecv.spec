# revision 16097
# category Package
# catalog-ctan /macros/latex/contrib/ecv
# catalog-date 2009-10-22 11:02:28 +0200
# catalog-license other-free
# catalog-version 0.2
Name:		texlive-ecv
Version:	0.2
Release:	1
Summary:	A fancy Curriculum Vitae class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ecv
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ecv.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ecv.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ecv.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The class provides an environment for creating a fancily laid
out tabular curriculum vitae inspired by the european
curriculum vitae. The distribution comes with a German and an
English template.

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
%{_texmfdistdir}/tex/latex/ecv/ecv.cls
%{_texmfdistdir}/tex/latex/ecv/ecvEnglish.ldf
%{_texmfdistdir}/tex/latex/ecv/ecvGerman.ldf
%{_texmfdistdir}/tex/latex/ecv/ecvNLS.sty
%doc %{_texmfdistdir}/doc/latex/ecv/COPYING
%doc %{_texmfdistdir}/doc/latex/ecv/README
%doc %{_texmfdistdir}/doc/latex/ecv/docstrip.cfg
%doc %{_texmfdistdir}/doc/latex/ecv/ecv.pdf
%doc %{_texmfdistdir}/doc/latex/ecv/template/CV-template_de.pdf
%doc %{_texmfdistdir}/doc/latex/ecv/template/CV-template_de.tex
%doc %{_texmfdistdir}/doc/latex/ecv/template/CV-template_en.pdf
%doc %{_texmfdistdir}/doc/latex/ecv/template/CV-template_en.tex
%doc %{_texmfdistdir}/doc/latex/ecv/template/Makefile
%doc %{_texmfdistdir}/doc/latex/ecv/template/portrait.eps
#- source
%doc %{_texmfdistdir}/source/latex/ecv/ecv.dtx
%doc %{_texmfdistdir}/source/latex/ecv/ecv.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
