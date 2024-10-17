Name:		texlive-ecv
Version:	24928
Release:	2
Summary:	A fancy Curriculum Vitae class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ecv
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ecv.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ecv.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ecv.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class provides an environment for creating a fancily laid
out tabular curriculum vitae inspired by the european
curriculum vitae. The distribution comes with a German and an
English template.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
